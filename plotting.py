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
shape=alt.Shape("species:N")                    

def format_plotdata(data, stats, Season):
    """
    creates a dataframe appropriate for plotting the desired density plan and section charts
    """
    seeddf = data.subdata

    #this for loop generates the plotting data
    choices = pd.DataFrame(
    (seeddf.index.values, 
        seeddf["common_name"], 
        seeddf["plants_per_meter"], 
        seeddf["ht"],
        seeddf["bloom_color"],
        seeddf["spring"],
        seeddf["summer"],
        seeddf["autumn"]),
            index=None).T.rename(columns={0: "species", 1: "common_name", 
            2: "plants_per_meter", 3:"ht", 4:"bloom_color", 5:"spring", 6:"summer", 7:"autumn"})


    species = []
    common_name= []
    bloom_color= []
    ht=[]
    spring=[]
    summer=[]
    autumn=[]
    x = []
    y = []
    for index, row in choices.iterrows():
        for i in range (0, row['plants_per_meter']):
            species.append(row["species"])
            common_name.append(row["common_name"])
            ht.append(row["ht"])
            bloom_color.append(row["bloom_color"])
            spring.append(row["spring"])
            summer.append(row["summer"])
            autumn.append(row["autumn"])
            x.append(random.uniform(0, 1))
            y.append(random.uniform(0, 1))
            
                
    source = pd.DataFrame((species, common_name, ht, bloom_color, spring, summer, autumn, x, y), index=None
            ).T.rename(columns={0:"species", 1:"common_name", 2:"ht", 3:"bloom_color", 4:"Spring", 5:"Summer", 6:"Autumn", 7:'x', 8:'y'})
    
    if Season=='Winter':
        source['bloom_color']= 'None'
        source['ht']*=.5
    else:    
        source.loc[source[f"{Season}"]==0, 'bloom_color'] = 'None'
        if Season=='Spring':
            source['ht']*=.3
    return source

def section_plot(data, stats, Season):
    """
    creates a visualization of  section/elevation of one square meter of seeded planting
    """
    source=format_plotdata(data, stats, Season)
    source2=source.loc[source['bloom_color'] != 'None']
    if Season=='Winter':
        scolor='#D6B08C'
    else:
        scolor='#7BB661'   
    #define the section elevation
    sectionstems = alt.Chart(data=source, title='Section Elevation of Proposed Planting').mark_bar(size=3, color=f'{scolor}').encode(
        x=alt.X('x:Q', axis=alt.Axis(title='1 meter')),
        y=alt.Y('ht:Q',axis=alt.Axis(title='height (feet)'), scale=alt.Scale(domain=(0, 8))),
        tooltip=['species:N', 'common_name:N']
        )

    sectionflowers = alt.Chart(data=source2).mark_point(filled=True, size=100).encode(
        x=alt.X('x:Q'),
        y=alt.Y('ht:Q'),
        color=color,
        shape=shape
    )    
    sectionelevation = (sectionstems+sectionflowers).properties(width=650, height=400).configure(background='#D3D3D3')

    return sectionelevation

def density_plot(data, stats, Season):
    """
    creates a visualization of one square meter of seeded planting in plan view
    """    
    source=format_plotdata(data, stats, Season)
    if Season=='Winter':
        pcolor=alt.Color('bloom_color:N',
                    scale = alt.Scale(domain=['Blue', 'Yellow', 'Purple', 'White', 'Red', 'Pink', 'Orange', 'Green', 'None'], 
                    range=['#D6B08C', '#CA8546', '#C9AA8D', '#BB6513', '#D7A36E', '#F2D4B7', '#A0856A', '#A97D51','#D6B08C']))
                    
    else:
        pcolor=color    
    #interactive highlight function
    highlight = alt.selection(type='single',
                                fields=['species', 'common_name'], empty="all")
    #define the density plot
    visualizeseeds = alt.Chart(data=source, title='Plan View of Proposed Planting').mark_point(filled=True, size=100).encode(
        x=alt.X('x', axis=alt.Axis(title='1 meter')),
        y=alt.Y('y', axis=alt.Axis(title='1 meter')),
        color=pcolor,
        shape=shape,
        tooltip=['species:N', 'common_name:N'],
    ).add_selection(
        highlight
    ).properties(width=650, height=515
    ).configure(background='#D3D3D3')
    
    return visualizeseeds

def format_chartdata(data, stats, season):
    """
    This function reformats the data for plotting.
    """
    seeddf=data.subdata
    
    #sort to only show forbs
    forbs = seeddf.loc[seeddf['forb'] == 1]
    #duplicate rows so that each plant (per square meter desired density) is its own row
    blooming=forbs.loc[np.repeat(forbs.index.values, forbs.plants_per_meter)]
    #create counts by bloom color 
    df1=blooming.groupby([f'{season}','bloom_color']).count().reset_index().rename(columns={'plants_per_meter':f'{season.upper()}'}).filter([f'{season}', 'bloom_color', f'{season.upper()}'])
    #remove extraneous data    
    df2=df1.loc[df1[f'{season}']==1].filter(['bloom_color', f'{season.upper()}']).set_index('bloom_color')

    return df2

def seasonality_chart(data, stats):
    """
    This function plots number of stems in bloom per square meter in each season to assess aesthetic quality and floral resource abundance.
    """
    
    spring=format_chartdata(data, stats, season='spring')
    summer=format_chartdata(data, stats, season='summer')
    autumn=format_chartdata(data, stats, season='autumn')

    source=pd.concat([spring, summer, autumn], axis=1).T.reset_index().rename(columns={'index':'season'}).melt('season')    
    
    seasonaldistribution = alt.Chart(data=source, title='Bloom Density by Season').mark_bar(size=100).encode(
        x=alt.X('season:N', sort=['SPRING', 'SUMMER', 'AUTUMN']),
        y=alt.Y('value:Q',axis=alt.Axis(title='number of plants per square meter in bloom')),
        color=color
        ).properties(width=650, height=400
        ).configure(background='#D3D3D3')

    return seasonaldistribution

    
