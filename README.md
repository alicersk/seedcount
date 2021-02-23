# project
### Project Goal
My program will serve as a design tool for seed mix design (seed mixes for establishing novel habitat, for example, pollinator habitat in Dept of Transportation ROW). 

## Code
It will take the input as either a csv or in an online fillable form and use pandas to calculate expected density for each species based on seeds/pound, [PLS (pure live seed) percentage](https://www.ernstseed.com/resources/bulk-vs-pure-live-seed-pls/), and field emergence percent if available. Then, using a combination of np.random (to assign random 'x' and 'y' coordinates to points for each seed) and toyplot, it will plot all the species expected densities on an interactive plot (users can hover over each symbol to see which species it represents and how many seedlings/m^2 of that species are expected) with different symbols mixed together in a random pattern to approximate a 1m by 1m area of the planting, or a 2m by 2m area. User will need to select a canvas size and can adjust symbols. The output seeds/meter squared, expected seedlings/m^2 of each species when it's symbol is hovered over, and as a table.


## Data

It will take either a csv or have an option as a fillable online form with species name, seeds per pound, and PLS. Output will be a csv of species, expected seedling density per species, seed density per species, and total seeds per m^2, and also interactive plots showing this information.


## Demo
