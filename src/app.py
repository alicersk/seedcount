#!usr/bin/env python

import pandas as pd
from fastapi import FastAPI
from src.seedcount import Seeds

# create the app as an instance of the fastAPI class
app = FastAPI()

# load the database once when the server starts
DATA = pd.read_csv(
    "https://eaton-lab.org/data/iris-data-dirty.csv",
    names=["species", "common_name", "seeds_per_pound", "germ_rate", "season"],
)

# create a root endpoint that say's hello
@app.get("/")
def root(n):
    "returns welcome message in JSON"
    return {"message": f"Ready to design a seed mix?"}

# create another endpoint for returning iris data
@app.get("/seedlist")
def seed_app(species=None):
    """
    docstrong
    """
    # get subset or full data
    if species is not None:
        data = DATA.loc[DATA.species == species, :]
    else:
        data = DATA

    # convert to JSON and return to endpoint
    sdata = data.to_json(orient="index")
    jdata = json.loads(sdata)
    return jdata

if __name__ == "__main__" :
   rec = Seeds(species="Solidago nemoralis", plantsper="4")  
   print(rec.seed_see())      
   print(rec.csv)