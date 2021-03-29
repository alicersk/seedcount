#!/usr/bin/env python

"""
Generate plots of data from Stats using altair
"""

import pandas as pd
import altair as alt

   



def generate_plots(data, stats):
    """

    """

    seeddf = data.subdata

    #this for loop generates the plotting data
    choices = pd.DataFrame(
        (seeddf.index.values, 
            seeddf["common_name"], 
            seeddf["plants_per_meter"], 
            seeddf["bloom_color"]),
             index=None).T.rename(columns={0: "species", 1: "common_name", 2: "plants_per_meter", 3:"bloom_color"})


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