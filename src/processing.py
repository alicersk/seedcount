#!/usr/bin/env python

"""
DATA processing for seedcount app
"""

import os
import pandas as pd


# get file from absolute path relative to here.
SEEDS = os.path.join(os.path.dirname(__file__), "SEEDS.csv")


class SeedData:
    def __init__(self):

        # the full dataset       
        self.data = pd.read_csv(SEEDS)
        self.data = self.data.set_index("species")

        # the dataset currently being displayed
        self.subdata = None



class Stats:
    """
    These calculation takes us from the inputted values to values that 
    can be purchased.
    """
    def __init__(self, data):

        # stats data
        self.subdata = data.subdata
        self.data = pd.DataFrame(
            index=data.subdata.index,
            columns=[
                "plants_per_meter",
                "seeds_per_lb",
                "germ_rate",
                "pounds_per_acre",
                "percent_by_weight",
                "seeds_per_meter",
            ]
        )

        # existing data
        self.data.plants_per_meter = data.subdata.plants_per_meter
        self.data.seeds_per_lb = data.subdata.seeds_per_lb
        self.data.germ_rate = data.subdata.germ_rate

        # computed numbers to be filled
        self.purchaselist = None

        # do computation
        self.compute()
 

    def compute(self):
        """
        ...
        """
        # plants per square meter * square meters to acres conversion / germination rate * seeds per pound = 
        # how many seeds per pound you need per acre to get the number of plants desired per square meter
        self.data["pounds_per_acre"] = (
            self.data["plants_per_meter"] / self.data["seeds_per_lb"] * 
            4046.86 / self.data["germ_rate"]
        )
                
        # It's customary to include percent by weight as well to help 
        # scale the mix up or down from an acre
        self.data["percent_by_weight"] = (
            self.data.pounds_per_acre / self.data.pounds_per_acre.sum()
        )

        self.data["seeds_per_meter"] = (
            self.data.plants_per_meter / self.data.germ_rate
        )

        self.purchaselist = self.data.filter([
            "common_name", "seeds_per_lb", 
            "pounds_per_acre", "percent_by_weight",
            ], axis=1)
