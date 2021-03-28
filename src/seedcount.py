#!usr/bin/env python

import streamlit as st
import pandas as pd
import random
import altair as alt


#To run, paste into terminal: streamlit run seedcount.py

"""
# Seed Count
Please begin by selecting your soil moisture level and desired species from the sidebar to the left.
"""

#Loading CSV
DATA = pd.read_csv('SEEDS.csv')


#Sidebar for selecting soil moisture level
moisture_value = st.sidebar.selectbox("Choose a soil moisture level",('ALL', 'Dry to Average Soil', 'Consistently Moist Soil', 'Saturated Soil'))

def data_filtering(habitat):
    "This function takes input from the drop-down menu and returns the selected subset of the dataframe."
    a1 = DATA.copy(deep = True)
    a1 = a1[a1['habitat'] == habitat]
    return a1

#selections
if moisture_value == "ALL":
	moisture_filtered = DATA
else:
	moisture_filtered = data_filtering(moisture_value)

#create empty dictionary to store choices
usrchoices = {}

#Displaying the options to 
for x in moisture_filtered['species']:
    count = st.sidebar.number_input(f"{x}  ({DATA['common_name'][DATA['species']==x].values[0]})",min_value=0, max_value=500, step=1)
    if count !=0:
        usrchoices[x]=count


##make a new data frame with the dictionary of user choices and relevant data from SEEDS
DATA=DATA.set_index("species")

usrchoicesdf=pd.DataFrame.from_dict(usrchoices, orient="index", columns=["plants_per_meter"])

st.write("You chose:", usrchoicesdf)

usrseed =DATA.loc[usrchoicesdf.index,]

seeddf=pd.concat([usrseed, usrchoicesdf], axis=1)


#These calculation takes us from the inputted values to values that can be purchased. 
#plants per square meter * square meters to acres conversion / germination rate * seeds per pound = 
#how many seeds per pound you need per acre to get the number of plants desired per square meter
seeddf["pounds_per_acre"]=seeddf["plants_per_meter"] / seeddf["seeds_per_lb"] * 4046.86 / seeddf["germ_rate"]
            
#It's customary to include percent by weight as well to help scale the mix up or down from an acre
seeddf["percent_by_weight"] = seeddf.pounds_per_acre / seeddf.pounds_per_acre.sum()
            
if seeddf.fall.sum() > 0:
	st.write("Some species on your list require cold stratification. Fall planting recommended to reduce dormancy and improve establishment.")


if seeddf.loc[seeddf['forb']==1].plants_per_meter.sum()/seeddf.plants_per_meter.sum() > .60:
    st.write("Consider adding more grasses or sedges to improve weed suppression and prevent erosion, especially if your site is sloped.")

seeddf.seeds_per_meter= seeddf.plants_per_meter / seeddf.germ_rate 
if seeddf.seeds_per_meter.sum()<400.0: 
    st.write("Consider increasing number of plants for better weed suppression and erosion control.")    

if seeddf.seeds_per_meter.sum()>1200.0:
	st.write("Consider decreasing desired density of plants to maintain diversity.")
#This will show the output table on streamlit using st.write
purchaselist=seeddf.filter([ "common_name", "seeds_per_lb", "pounds_per_acre", "percent_by_weight"], axis=1)

st.write("### Purchase List", purchaselist.sort_index())
st.write("The seeding rate of your mix is {} pounds per acre".format(seeddf.pounds_per_acre.sum().round(3)))
st.write("Seed with an equal volume of bulking agent, such as kitty litter, and an appropiate nurse crop from the list below.")

st.write("Here is a visualization of your desired species density:")


#this for loop generates the plotting data
choices=pd.DataFrame((seeddf.index.values, seeddf["common_name"], seeddf["plants_per_meter"], seeddf["bloom_color"]), index=None).T.rename(columns={0: "species", 1: "common_name", 2: "plants_per_meter", 3:"bloom_color"})


species = []
common_name= []
bloom_color= []
x = []
y = []
for index, row in choices.iterrows():
    for i in range (1, row['plants_per_meter']):
        species.append(row["species"])
        common_name.append(row["common_name"])
        x.append(random.uniform(0, 1))
        y.append(random.uniform(0, 1))
        bloom_color.append(row["bloom_color"])
        
metercalc = pd.DataFrame((species, common_name, bloom_color, x, y), index=None).T.rename(columns={0:"species", 1:"common_name", 2:"bloom_color", 3:"x", 4:"y"})

#build the altair chart

#define datasource 
source = metercalc
#interactive highlight function
highlight = alt.selection(type='single',
                          fields=['species', 'common_name'], empty="all")
#color
color = alt.condition(highlight,
                      alt.Color('species:N', scale=alt.Scale(scheme='spectral')),
                      alt.value('lightgray'))

#define the density plot
visualizeseeds = alt.Chart(source).mark_point(filled=True, size=100).encode(
    x=alt.X('x', axis=alt.Axis(title='1 meter')),
    y=alt.Y('y', axis=alt.Axis(title='1 meter')),
    color=alt.Color('bloom_color', legend=None),
    tooltip=['species:N', 'common_name:N'],
).add_selection(
    highlight
).properties(width=500, height=500)

#call altair chart with streamlit
st.altair_chart(visualizeseeds, use_container_width=False)

#define seasonality chart
source = pd.DataFrame({'season':["spring", "summer", "fall"], 'number of species in bloom' : [seeddf.spring.sum(), seeddf.summer.sum(), seeddf.autumn.sum()]})

seasonaldistribution = alt.Chart(source).mark_bar(size=100, color='Green').encode(
    x="season",
    y="number of species in bloom",
).properties(width=500, height=300)
#call seasonality chart with streamlit
st.altair_chart(seasonaldistribution)    