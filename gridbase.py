import numpy as np
from math import sqrt


"""Create a surface centered in cero, return a Vector and Edges matricies"""
number_of_dimensions = 2 # x and y
l = 1 # lengh of the grid
n = 4 # Number of squares must be a even number 
step = l/n # Step
d = n/2 # Number of squares in one side; rigth, left of cero
number_of_verticies = (n)**number_of_dimensions
V = [x for x in np.arange(-l/2, (l/2)+step, step)]
V = [[x,y, (x**2)+(y**2)] for x in V for y in V] # here must be replace for de desired function of z 
verticies = np.asarray(V)

verticies_index = [x for x in range(0,verticies.shape[0])]
print(verticies_index)
edges = [[x,y] for x in verticies_index for y in verticies_index if ((x!=y) and (y!=x) and ((sqrt((verticies[x][0]-verticies[y][0])**2+(verticies[x][1]-verticies[y][1])**2))<=step))]
print(edges)
