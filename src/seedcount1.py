#!usr/bin/env python

import numpy as np 
import pandas as pd
import toyplot
import streamlit as st


@st.cache
def seed_count():
    AWS_BUCKET_URL = "https://streamlit-demo-data.s3-us-west-2.amazonaws.com"
    df = pd.read_csv(AWS_BUCKET_URL + "/agri.csv.gz")
    return df.set_index("Region")

try:
    df = get_UN_data()
    countries = st.multiselect(
        "Choose countries", list(df.index), ["China", "United States of America"]
    )
    if not countries:
        st.error("Please select at least one country.")
    else:
        data = df.loc[countries]
        data /= 1000000.0
        st.write("### Gross Agricultural Production ($B)", data.sort_index())

        data = data.T.reset_index()
        data = pd.melt(data, id_vars=["index"]).rename(
            columns={"index": "year", "value": "Gross Agricultural Product ($B)"}
        )
        chart = (
            alt.Chart(data)
            .mark_area(opacity=0.3)
            .encode(
                x="year:T",
                y=alt.Y("Gross Agricultural Product ($B):Q", stack=None),
                color="Region:N",
            )
        )
        st.altair_chart(chart, use_container_width=True)
except urllib.error.URLError as e:
    st.error(
        """
        **This demo requires internet access.**

        Connection error: %s
    """
        % e.reason
    )
class Seeds:
    def __init__(self, species=None, plantsper=None):
        
        # store input params
        self.species = species
        self.plantsper = plantsper
        
        # will be used to store output results
        self.plantlist = None
        self.seedwt=None
        self.plot=None
        self.csv = None

    def seed_see(self):
        """
        This function plots the user's inputted seed densities to an interactive plot.
        """
        PASS
        return self.plot

    def seed_count(self):
        """
        This function calculates pounds of seeds needed for each species based on desired density.
        """
        PASS
        return self.seedwt

    def seed_buy (self):
        """
        This function stores results for all plants passed to seed count to csv.
        """
        PASS
        return self.csv


if __name__ == "__main__" :
   rec = Seeds(species="Solidago nemoralis", plantsper="4")  
   print(rec.seed_count())      
   print(rec.csv)
   print(rec.seed_see())