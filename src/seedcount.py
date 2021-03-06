#!usr/bin/env python

import numpy as np 
import pandas as pd
import toyplot

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