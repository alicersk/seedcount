# project
### Project Goal
My program will serve as a design tool for seed mix design (seed mixes for establishing novel habitat, for example, pollinator habitat in Dept of Transportation ROW). 

## Code
It will take the input as either a csv or in an online fillable form and use pandas to calculate expected density for each species based on seeds/pound, [PLS (pure live seed) percentage](https://www.ernstseed.com/resources/bulk-vs-pure-live-seed-pls/), and field emergence percent if available. Then, using a combination of np.random (to assign random 'x' and 'y' coordinates to points for each seed) and toyplot, it will plot all the species expected densities on an interactive plot (users can hover over each symbol to see which species it represents and how many seedlings/m^2 of that species are expected) with different symbols mixed together in a random pattern to approximate a 1m by 1m area of the planting, or a 2m by 2m area. User will need to select a canvas size and can adjust symbols. The output seeds/meter squared, expected seedlings/m^2 of each species when it's symbol is hovered over, and as a table. If it were possible to query a database to get season of bloom for each species for a given region and be able to toggle between seasons to see floral resource availability, and also show a bar chart for bloom density per m^2 in each month, that would be ideal, but might be beyond me. Assigning color of symbol could be done randomly, or based on flower color if the color is included in the common name.


## Data

It will take either a csv or have an option as a fillable online form with species name, seeds per pound, and PLS percent or percent field emergence. Output will be a csv of species, expected seedling density per species, seed density per species, and total seeds per m^2, and also interactive plots showing this information.
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
The above represents a typical format of a data file for creating/purchasing a seed mix. Not all fields would be used or needed by the program, and some vary and can be included if needed, for example, calculating based on PLS or field emergence depending which value is included (field emergence data provides a more accurate calculation but it not available as often as PLS percent). Non-optional fields would be Botanical Name, seeds/pound, PLS or percent field emergence, and pounds of seed. Total area to be seeded would default to 1 acre, with option to put in a different value.  

## Demo
