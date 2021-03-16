# Paired-Programming on `seedcount`

## Goal of the project: 

The overall goal of the project is very clear - the app will help the user prepare a seed mix for planting a native meadow. The user will choose which species they want and input a desired density per square meter.`seedcount` will then calculate the amount of seed the user should buy for their desired species and densities along with a numnber of other useful tidbits, such as germination protocols (e.g. required cold stratification).
`seedcount` also gives the user tools to help them design a better mix. It will also display a graph that gives the user an idea of what the distribution of their chosen species looks like at the given densities. The user will also be able to visualize blooming times for their chosen mix. 


It would be nice to add a few summary sections to the proposal to make the structure of the project more clear, e.g:

Dependencies:
- `streamlit`: library for interactive webapp + free online hosting
- `pandas`: data will largely be manipulated as pandas sataframes
- `numpy`: for calculations
- `random`: for plotting
- `os`: for file navigation

Code:
- `seedcount.py`: calculations
- `streamlitapp.py`: code that runs the streamlit webapp
- `app.py`: this would have run your heroku app, but I think streamlit will do everythign you need without heroku
- `makesboxes.py`: this is a piece of code I wrote to generate the code that will create a list of species checkboxes on your `streamlit` app for the user to choose from. I believe you will be able to make `streamlit` display it nicely into 3-4 columns so it's not just one giant list. This code also keeps track of the user choices and write them to a `userchoices` list object.

*Note:* I think you may be able to have one .py file that is the one called by streamlit and all your calculations happen inside of it. 

Functions:
- `makeboxes`: generates the code for `streamlit` species checkboxes with formatting, inserts it into the streamlitapp.py code  
- `seedcount`: takes user input and calculates the quantity in lbs that the user should buy for the desired densities. Outputs 'purchaselist' object
- `visualizeseeds`: generates dataset using random (x,y) coordinates for the user choices. Then, generates an interactive graph of random seed distribution in 1x1 meter plot
- `bloomtimes`: generates a histogram showing bloom times of the chosen mix


## Data
I suggest you re-write this section a little so its clear what data you have stored within the app (SEEDS.csv), what data the user is providing (species list, densities), and what data is generated (purchaselist, visualizations)

## Code
You have a solid skeleton here, with all the necessary parts for a working python package. I added some extra information to your `setup.py`, but it was minor stuff. 

So far, the code is mostly skeleton code - but the structure is very clear. A few equations have been written and a few lines that instruct `streamlit` to write some text. 

Function suggestions: see above

## Code Constributions & Ideas
You're off to a great start here. It's hard to organize code when working with a new app like `streamlit` because you're learning as you go. I'm not sure what the best way to organize this code is, but I think you'll probably want to do everything in the same file that runs your streamlit app. I did not put functions into `streamlitapp.py` because I was just testing code, but I think it should be straightforward to just drop all your functions/class objects into it. 

I tested all my code (except the `streamlit` stuff) in a Jupyter Notebook and I have uploaded that notebook so you can reference it. 

I ended up writing a new file `streamlitapp.py` to test out `streamlit` code, since I couldn't test it in my Jupyter Notebook. Everytime you save the file you just need to refresh the browser running the app to see the changes. The code I wrote here does the following:
1. reads in your data from .csv files and does some cleaning/data-wrangling
2. creates a list of checkboxes for the user to choose from *more on this later*
3. saves the species the user chooses to a list `usrchoices` and also lists them in streamlit
4. generates a new dataframe with your seed metadata from the list provided by the user - this should get you started for adding all your calculations. 
5. generates an interactive graph of seed distribution in a 1x1 meter plot from the sample data you provided

#### Regarding #3 above

I think it is better to let the user choose from checkboxes rather than a drop-down menu, but it is completely up to you which method to go with. The code chunk is huge, but I've automated it. The `makeboxes.py` file uses the species in SEEDS.csv to generate streamlit code that makes a checkbox and instructs streamlit to add any checked box to a list. The code is saved to a `checkbooxes.txt` file (it overwrites everytime you run the code), which I just copy and pasted into `streamlitapp.py`. I'm sure there is a much more elegant way to write this so that it is more automated - perhaps Deren or another student can help with that. As I mentioned above, you should also be able to get streamlit to display this nicely using multiple columns. 

#### 5. graphing
I went with `altair` insteaf of `toyplot` because I couldn't confirm that `streamlit` supports `toyplot` and I also liked the interative features of `altair`. I use a loop to generate the datapoints based on the user input and then graph in a 1x1m plot. I made the graph interarctive by having it highlight a single species when you click on one of the data points. Click in a blank space to undo. You can play around with the graphing code in the Jupyter Notebook. 