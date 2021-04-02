#!/usr/bin/env python

"""
Generate plots of data from Stats using altair
"""

import pandas as pd
import altair as alt
import random
   



def density_plot(data, stats):
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
        for i in range (0, row['plants_per_meter']):
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
        color=alt.Color(color, legend=None),
        tooltip=['species:N', 'common_name:N'],
    ).add_selection(
        highlight
    ).properties(width=500, height=500)
    
    return visualizeseeds


def seasonality_chart(data, stats):
    """
    This function plots number of stems in bloom per square meter in each season to assess aesthetic quality and floral resource abundance.
    """
    seeddf=data.subdata
    #define seasonality chart
   
    choices = seeddf.loc[seeddf['forb'] == 1]

    species=[]
    season= []
    color= []

    for index, row in choices.iterrows():
            for i in range (0, row['plants_per_meter']):
                color.append(row["bloom_color"])
                species.append(index)
                if row["spring"]==1 and row["summer"]==0 and row["autumn"]==0:
                    season.append("spring")
                elif row["summer"]==1 and row ["spring"]==0 and row ["autumn"]==0:
                    season.append("summer")
                elif row["autumn"]==1 and row ["spring"]==0 and row ["summer"]==0:
                    season.append("autumn")
                elif row["spring"]==1 and row ["summer"]==1 and row["autumn"]==1:
                    season.append("spring")
                    season.append("summer")
                    season.append("autumn")
                    color.append(row["bloom_color"])
                    color.append(row["bloom_color"])
                    color.append(row["bloom_color"])
                    species.append(index)
                    species.append(index)
                    species.append(index)
                elif row["spring"]==1 and row ["summer"]==1 and row["autumn"]==0:
                    season.append("spring")
                    season.append("summer")
                    color.append(row["bloom_color"])
                    color.append(row["bloom_color"])
                    species.append(index) 
                    species.append(index)
                elif row["spring"]==0 and row ["summer"]==1 and row["autumn"]==1:
                    season.append("summer")
                    season.append("autumn")
                    color.append(row["bloom_color"])
                    color.append(row["bloom_color"])
                    species.append(index) 
                    species.append(index)
    
    source = pd.DataFrame((species,season, color), index=None).T

    seasonaldistribution = alt.Chart(source).mark_bar(size=100).encode(
        x="season",
        y="species",
        color="color"
    ).properties(width=500, height=300)

    return seasonaldistribution
    