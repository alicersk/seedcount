#!/usr/bin/env python

"""
Generate plots of data from Stats using altair
"""

import pandas as pd
import altair as alt
import random
import numpy as np  
import streamlit as st

color=alt.Color('bloom_color:N',
                    scale = alt.Scale(domain=['Blue', 'Yellow', 'Purple', 'White', 'Red', 'Pink', 'Orange', 'Green', 'None'], 
                    range=['#5218FA', '#FFD300', '#BD33A4', '#F8F8FF', '#B31B1B', '#E4717A', '#ED872D', '#ACE1AF','#7BB661']),
                    legend = alt.Legend(title="Bloom Color"))

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


    #define the density plot
    #define the density plot
    visualizeseeds = alt.Chart(source).mark_point(filled=True, size=100).encode(
        x=alt.X('x', axis=alt.Axis(title='1 meter')),
        y=alt.Y('y', axis=alt.Axis(title='1 meter')),
        color=color,
        shape='species:N',
        tooltip=['species:N', 'common_name:N'],
    ).add_selection(
        highlight
    ).properties(width=650, height=500
    ).configure(background='#D3D3D3')
    
    return visualizeseeds


def seasonality_chart(data, stats):
    """
    This function plots number of stems in bloom per square meter in each season to assess aesthetic quality and floral resource abundance.
    """
    seeddf=data.subdata
    #define seasonality chart
   
    forbs = seeddf.loc[seeddf['forb'] == 1]
    blooming=forbs.loc[np.repeat(forbs.index.values, forbs.plants_per_meter)]
    spring=blooming.groupby(['spring', 'bloom_color']).count().reset_index().rename(columns={'plants_per_meter':'SPRING'}).filter(['spring','bloom_color', 'SPRING'])
    spring2=spring.loc[spring['spring']==1].filter(['bloom_color', 'SPRING']).set_index('bloom_color')
    summer=blooming.groupby(['summer', 'bloom_color']).count().reset_index().rename(columns={'common_name':'SUMMER'}).filter(['summer', 'bloom_color', 'SUMMER'])
    summer2=summer.loc[summer['summer']==1].filter(['bloom_color', 'SUMMER']).set_index('bloom_color')
    autumn=blooming.groupby(['autumn', 'bloom_color']).count().reset_index().rename(columns={'common_name':'AUTUMN'}).filter(['autumn', 'bloom_color', 'AUTUMN'])
    autumn2=autumn.loc[autumn['autumn']==1].filter(['bloom_color', 'AUTUMN']).set_index('bloom_color')
    
    source=pd.concat([spring2, summer2, autumn2], axis=1).T.reset_index().rename(columns={'index':'season'}).melt('season')       
    
    seasonaldistribution = alt.Chart(source).mark_bar(size=100).encode(
        x=alt.X('season:N', sort=['SPRING', 'SUMMER', 'AUTUMN']),
        y=alt.Y('value:Q',axis=alt.Axis(title='number of plants per square meter in bloom')),
        color=color
    ).properties(width=650, height=400
    ).configure(background='#D3D3D3')

    return seasonaldistribution