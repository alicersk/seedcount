# project
### Project Goal
My program will serve as a design tool for seed mix design (seed mixes for establishing novel habitat, for example, pollinator habitat in Dept of Transportation ROW), specifically in the Mid-Atlantic, but usable for any location if users don't mind entering in more of their own data. It should make seed mix design more accessible to designers and planners more comfortable 

## Code
Ideally, it will take input as a fillable online form with species name (botanical name or common name), desired seedlings per square meter (of each species), total area to be seeded, and whether the area will be planted in spring or fall. If they want to see a breakdown of floral resources available by month, they can select the seasonal analysis option. The program will find the values for each species of seeds/pound, % germination or % field emergence, months in bloom in the Mid-Atlantic, etc., by searching my dataset. If the dataset does not have the species, or any of the required information for the species (seeds per pound, and either germination percent or field emergence percent)it will give the user the option to input the values. The program will throw a warning if the seeding is outside of the recommended range of density, outside the recommended balance of forbs to grasses, or using plants requiring cold stratification in a spring planting. Then, using a combination of np.random (to assign random 'x' and 'y' coordinates to points for each seed) and toyplot, it will plot all the species desired densities on an interactive plot (users can hover over each symbol to see which species it represents and how many seedlings/m<sup>2</sup> of that species are expected) with different symbols mixed together in a random pattern to approximate a 1m by 1m area of the planting. If they selected the seasonal analysis option, they will also get a bar chart for plants per m<sup>2</sup> in bloom in each month so that they can see gaps in floral resource availability in their design. 

## Data
It will take either a csv or have an option as a fillable online form with species name (botanical name or common name), total area to be seeded, and desired seedlings per square meter, and planting season. The output will be both a visualization of the planting they entered in, including a seasonal analysis if that option was selected, and a csv in the following format:
```
Botanical Name, Common Name, seeds/pound, percent field emergence, pounds, percent by weight
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
