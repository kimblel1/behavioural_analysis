# %%
# first cell
import pandas as pd
import numpy as np
import math

data = pd.read_table('data/1-5hour_results.tsv', index_col=0)
print(data)
x_values_raw = data.loc[3:, 'X']
x_min = data.loc[1, 'X']
x_max = data.loc[2, 'X']

x_values = x_values_raw - x_min

# %%
# variance analysis

std = np.std(x_values)
var = np.var(x_values)

# %%
# function for network analysis

#pulling data and re-indexing so it starts with 0 not 3
xy_values = data.loc[3:, ['X', 'Y']]
xy_values = xy_values.reset_index(drop=True)

xy1 = xy_values.loc[0]
xy2 = xy_values.loc[1]

dist12 = math.dist(xy1, xy2)
print(dist12)

#function that determines distancde bteween to animals
def dist_2points(point1, point2):
    dist = math.dist(point1, point2)
    result = [point1.name, point2.name, dist]

    return(result)

#

#example use of function
dist01 = dist_2points(xy1, xy2)

# %%

#building the distance network between animals


distance_data = []

for i in xy_values.index:
    for j in xy_values.index:
        if(i == j):
            continue
        loop_animal_i = xy_values.loc[i, :]
        loop_animal_j = xy_values.loc[j, :]
    

        distance = dist_2points(loop_animal_i, loop_animal_j)
        print(distance)
        distance_data.append(distance)
# %%
