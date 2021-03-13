#!usr/bin/env python

import numpy as np 
import pandas as pd
import toyplot
import streamlit as st
import os.path


@st.cache
class Seeds:
    def __init__(self, species=None, plantsper=None):
        
        # store input params
        self.species = species          #latin name
        self.plantsper = plantsper      #plants per square meter
        
        # will be used to store output results
        self.seeddf = None
        

    def seed_see(self):
        """
        This function plots the user's inputted seed densities to an interactive plot.
        """
        chart = (
            pass
        )
        
        st.toyplot_chart(chart, use_container_width=True)

        

    def seed_count(self):
        """
        This function calculates pounds of seeds needed for each species based on desired density entered into the webapp.
        """
        try: 
            #This is a placeholder for how to save the input from the webapp
            Speciesinput={}
            for species in input:
                if species not in Speciesinput:
                    Speciesinput[species]=plantsper
            
            #the csv with the source data
            df = pd.read_csv(os.path.abspath("seedcount/src/SEEDS.csv")
            df.index_col="Latin Name"
            #making a data frame by selecting rows of the source data based on which species were selected.
            #what I'm not sure how to do is how to also include a column from the inputted plantsper values (which represent
            #plants per meter squared)
            pd.concat(Speciesinput.values(), seeddf)
            seeddf = df.loc[[Speciesinput.keys], ["Latin Name", "Alternate Latin Name", "Common Name", "Seeds/lb", "GerminationRate", "Forb", "Fall Seeding Req"]]
            pd.concat(seeddf, Speciesinput, axis="Latin Name")

            #These calculation takes us from the inputted values to values that can be purchased. 
            #plants per square meter * square meters to acres conversion / germination rate * seeds per pound = 
            #how many seeds per pound you need per acre to get the number of plants desired per square meter
            seeddf["PoundsperAcre"]=seeddf.PlantsperMeter * seeddf."Seeds/lb" * 4046.86 / seeddf."Expected Percent Germination"
            
            #It's customary to include percent by weight as well to help scale the mix up or down from an acre
            seeddf["PercentbyWeight"] = seedf.PoundsperAcre / seeddf.PoundsperAcre.sum()
            
            if seeddf."Fall Seeding Req".sum() > 0:
                st.write("Some species on your list require cold stratification. Fall planting recommended; see table for species-level information.")

            #if seeddf."Forb".sum()/len(seeddf) > .60: <<calculation is not detailed enough
                #st.write("Consider adding more grasses or sedges to improve weed suppression and prevent erosion.")

            #if seeddf."Forb".sum()/len(seeddf) > .5: <<calculation is not detailed enough
                #st.write("Consider increasing density of ")    
            
            #This will show the output table on streamlit using st.write, and return the csv somehow
            seeddf.set_index("Latin Name")
                st.write("### Purchase List", seeddf.sort_index())
                return pd.write_csv(seeddf)

        except pd.error as e:
            st.error(
                """
                **This requires internet access.**

                Connection error: %s
            """
                % e.reason
            )    


if __name__ == "__main__" :
  