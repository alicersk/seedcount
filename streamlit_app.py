#!/usr/bin/env python

"""
To run, paste into terminal: streamlit run app.py
"""

import streamlit as st
import pandas as pd
import base64
from processing import SeedData, Stats
from plotting import density_plot, seasonality_chart, section_plot



@st.cache(allow_output_mutation=True)
def load_data_once():
    """ only load the data once and cache it """
    return SeedData()


def write_header():
    """ write the title and instructions """
    st.title("Seed Count")
    st.write((
        "Welcome!"
        " Seed Count is a tool for designing native (and adapted) seed mixes for use in the Mid-Atlantic."
        "Please begin by selecting the soil moisture level of the site for which you are designing the seed mix, "
        "then enter your desired plant density for each species (in plants per square yard) from the sidebar to the left."
        "Keep an eye on the warnings, in yellow, which can help ensure your seed mix will be successful."
        "Click the question mark to the right of each species name to learn more about it."
        "Use the section/elevation and plan visualizations to assess and re-adjust your design if necessary- the "
        "seasonal slider will help compare the predicted aesthetic in different seasons. When you are satisfied that your"
        "proposed planting meets your requirements, scroll to the bottom to download it as a CSV which can be formatted as a table"
        "or submitted directly for purchase. The pounds per acre value will allow you to calculate the amount you need based on the area of your site."
    ))


def sidebar_moisture_selector(data):
    """ a selector of the moisture type """
    
    moisture_value = st.sidebar.selectbox(
        "Choose a soil moisture level", 
        ('ALL', 'Dry to Average Soil', 'Consistently Moist Soil', 'Saturated Soil'),
    )
    st.sidebar.write("* indicates non-native species")
    # resets .subdata selection from .data
    if moisture_value != "ALL":
        data.subdata = data.data[data.data.habitat == moisture_value].copy()
    else:
        data.subdata = data.data.copy()

    st.sidebar.write ("* indicates non-native species")
    return moisture_value

def display_seeds(data):
    """
    record and display user selections
    """
    # create input for each spp in subdata
    usrchoices = {}
    for spp in data.subdata.index:

        # get data for label and tooltip
        common_name = data.subdata.at[spp, "common_name"]
        ht = data.subdata.at[spp, "ht"]
        if data.subdata.at[spp, 'bloom_color'] != 'None':
            bloom_color=data.subdata.at[spp, "bloom_color"]
           
        seasonl=[]
        if data.subdata.at[spp, "spring"]==1:
            seasonl.append("Spring")
        if data.subdata.at[spp, "summer"]==1:
            seasonl.append("Summer")
        if data.subdata.at[spp, "autumn"]==1:
            seasonl.append("Autumn")
        
        season = ', '.join(map(str, seasonl))    

        #write helpstring
        if season:
            helpstring=f"height={ht} ft; bloom season={season}; bloom color={bloom_color}"
        else:
            helpstring=f"height={ht} ft"       

        # create a number input
        count = st.sidebar.number_input(
            f"{spp}  ({common_name})",
            min_value=0, 
            max_value=500, 
            step=1,
            help=helpstring
        )
        if count:
            usrchoices[spp] = count

    # convert dict to df for displaying as a table
    usrchoicesdf = pd.DataFrame.from_dict(
        usrchoices, 
        orient="index", 
        columns=["plants_per_yard"],
    )

    # display
    if usrchoicesdf.size:
        st.write("#### You selected:")
        st.table(usrchoicesdf)

    # subselect these plants from dataset
    data.subdata = data.subdata.loc[usrchoicesdf.index, :]
    data.subdata = pd.concat([data.subdata, usrchoicesdf], axis=1)


def display_warnings(data, stats):
    """
    Show warnings in warning boxes
    """
    if data.subdata.fall.sum() > 0:
        st.warning((
            "**Cold Stratification Required**: Some species on your list "
            "require cold stratification. Fall planting recommended to "
            "reduce dormancy and improve establishment."
        ))

    forbs_density = data.subdata[data.subdata.forb == 1].plants_per_yard.sum()
    all_density = data.subdata.plants_per_yard.sum()
    if forbs_density / all_density > 0.6:
        st.warning((
            "**Forb Density is High**: Consider adding more grasses or "
            "sedges to improve weed suppression and prevent erosion, "
            "especially if your site is sloped."
        ))

    if stats.data.seeds_per_yard.sum() < 400.0: 
        st.warning(
            "**Not Enough Plants**: Consider increasing number of plants for better weed "
            "suppression and erosion control."
        )

    if stats.data.seeds_per_yard.sum() > 1200.0:
        st.warning(
            "**Too Many Plants**: Consider decreasing number of plants to reduce competition and maintain "
            "diversity."
        )





def display_plot(data, stats):
    """
    Create plots from function in plotting module
    
    """
    st.write("### Use the slider to visualize your design in different seasons. Scroll down for plan view.")
    season = st.select_slider("Choose a season to visualize", options=['Spring', 'Summer', 'Autumn', 'Winter'])
    st.altair_chart(section_plot(data, stats, Season=f'{season}'), use_container_width=False)
    st.altair_chart(density_plot(data, stats, Season=f'{season}'), use_container_width=False)  
    st.altair_chart(seasonality_chart(data, stats), use_container_width=False) 
    

def display_purchase_info(stats):
    """
    show table and info boxes
    """
    st.write("### Seed Mix Specification")
    st.table(stats.purchaselist.sort_index())
    st.info(
        "The seeding rate of your mix is **{:.2f} pounds per acre**."
        .format(stats.data.pounds_per_acre.sum())
    )
    st.info(
        "Spread the seedmix with an equal volume of a bulking agent (non-clumping kitty litter, rice hulls or clean sand), "
        "and with 25 lbs per acre of common oats (Avena sativa), cereal rye (Secale cereale) or winter wheat (Triticum aestivum). "
        "Roll or press seeds into soil to ensure good seed-to-soil contact but do not bury. Cover with weed-free wheat or oat straw."
    )
    
    

def download_link(data, stats, moisture_value):
    """
    Generates a link to download the Seed Mix Specification as a csv
    """
    object_to_download=stats.purchaselist.reset_index().rename(columns={'index':'latin_name'})
    
    download_filename= f'Seed Mix - {moisture_value}.csv'

    object_to_download = object_to_download.to_csv(index=False)

    # some strings <-> bytes conversions necessary here
    b64 = base64.b64encode(object_to_download.encode()).decode()

    tmp_download_link= f'<a href="data:file/txt;base64,{b64}" download="{download_filename}"><input type="button" value="Download Seed Mix as CSV"></a>'   

    st.markdown(tmp_download_link, unsafe_allow_html=True)    



if __name__ == "__main__":
    
    # load the data once.
    data = load_data_once()

    # Title and instructions
    write_header()

    # Sidebar for selecting soil moisture level
    moisture_value = sidebar_moisture_selector(data)
    
    # Display selected plants
    display_seeds(data)

    # calculate Stats    
    stats = Stats(data)

    # only do this latter stuff if some selections were made
    if stats.data.size:

        # Display warnings
        display_warnings(data, stats)

        # display plots
        display_plot(data, stats) 

        # Display purchase list info
        display_purchase_info(stats)

        # Make downloadable csv of results
        download_link(data, stats, moisture_value)
        

        
