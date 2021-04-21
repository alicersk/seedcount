# seedcount
### Project Goal
Seedcount will serve as a design tool for Mid-Atlantic Native seed mix design for establishing novel habitat, such as pollinator or grassland bird habitat, in an institutional, commercial, or residential setting. The plot is intended to help designers visualize the mix they are proposing. The table produces a seed mix with percentages by weight from inputted species and desired plant densities (in msquare yards). Plant list is drawn from species that are both native to the Mid-Atlantic region of the United States and are available to purchase from local seedhouses. 

### Code
It will use a streamlit webapp format to take input as a dropdown menu with the possible species, with a field for desired seedlings per square yard of each species, total area to be seeded, and whether the area will be planted in spring or fall.  The program will find the values for each species of seeds/pound, % germination or % field emergence, months in bloom in the Mid-Atlantic, etc., by searching the dataset (which is a csv). The program will throw a warning if the seeding is outside of the recommended range of density, outside the recommended balance of forbs to grasses, or using plants requiring cold stratification (i.e. requiring fall seeding). Then, using a combination of np.random (to assign random 'x' and 'y' coordinates to points for each seed) and toyplot, it will plot all the species desired densities on an interactive plot (users can hover over each symbol to see which species it represents and how many seedlings/m<sup>2</sup> of that species are expected) with different symbols mixed together in a random pattern to approximate a 5m by 5m area of the planting. 
If they selected the seasonal analysis option, they will also get a bar chart for plants per m<sup>2</sup> in bloom in each month so that they can see gaps in floral resource availability in their design. 
In addition to seeing the plot, the user will get a csv in the appropriate format to order a seed mix. This is pretty basic arithmetic, though some rounding and checking of numbers is necessary to ensure that species with extremely light seed show up in the percent-by-weight column (and also that an impossible to measure volume of seed is not being ordered- no one can weigh out .01 grams of Juncus effusus seed). 
The code itself uses pandas to read the csv and manipulate the dataframe with the user's seedmix. It is organized as a Class function (see ./src/seedcount.py). 

### Data
Users will select their choices from the webapp for species, then enter desired seedlings per square yard, total area to be seeded, and planting season. The output will be both a visualization of the planting they entered in, including a seasonal analysis if that option was selected, and a csv in the following format:
```
Latin Name, Common Name, seeds/pound, expected germination, pounds, percent by weight, Fall Planting Required 
Agrostis hyemalis, Winter Bentgrass, 8500000, 0.81, 0.06, 0.39%
Asclepias incarnata, Swamp Milkweed, 70000, 0.18, 1.61, 5.35%
Asclepias tuberosa, Butterfly Weed, 90720, 0.18, 1.24, 8.23%
Chamaecrista fasticulata, Partridge pea, 63504, 0.25, 1.27, 8.47%
Chelone obliqua, Turtlehead, 861840, 0.15, 0.16, 1.04%
Coreopsis lanceolata, Lanceleaf Coreopsis, 226800, 0.35, 0.25, 1.69%
Dalea purpureum, Purple Prairie Clover, 272160,	0.3, 0.25, 1.65%
...
```
The above represents a typical format of a file for specifying or purchasing a seed mix, which could be submitted as part of construction documentation or simply sent to a seed house. 

## Demo
User Input:
```
Helianthus angustifolius	1
Hordeum jubatum	5
Juncus effusus	15
Koesteleskya virginica	1
Penstemon digitalis 	5
...
Spring seeding ? YES
Seasonal analysis? YES
Total Area (in acres)? 8.2
```
Output: Plot, chart of seasonality.
```
WARNING: Helianthus angustifolius requires cold stratification. Seed in fall or cold stratify before seeding.
```
csv:
```
Helianthus angustifolius, Swamp Sunflower, 504000, 0.78, 0.01, 0.07%
Hordeum jubatum, Foxtail Barley, 192326.4, 0.4, 0.26, 0.02%
Juncus effusus, Soft Rush, 43,359,000, 0.05, 0.03, 0.19%
Koesteleskya virginica, Saltmarsh Mallow, 26000, 0.088, 1.77, 11.75%
Penstemon digitalis, White Beardtongue, 1360800, 0.25, 0.06, 0.40%
```
