"""
Hexagonal tiling library

F. Comitani @2017 
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import transforms
from matplotlib.patches import RegularPolygon
from matplotlib.collections import PatchCollection


def coorToHex(x,y):

    """Convert Cartesian coordinates to hexagonal tiling coordinates.

        Args:
            x (float): position along the x-axis of Cartesian coordinates.
            y (float): position along the y-axis of Cartesian coordinates.
            
        Returns:
            array: a 2d array containing the coordinates in the new space.
                
    """


    newy=y*2/np.sqrt(3)*3/4
    newx=x
    if y%2: newx+=0.5
    return [newx,newy]    
    

def plot_hex(fig, centers, weights):
    
    """Plot an hexagonal grid based on the nodes positions and color the tiles
       according to their weights.

        Args:
            fig (matplotlib figure object): the figure on which the hexagonal grid will be plotted.
            centers (list, float): array containing couples of coordinates for each cell 
                to be plotted in the Hexagonal tiling space.
            weights (list, float): array contaning informations on the weigths of each cell, 
                to be plotted as colors.
            
        Returns:
            ax (matplotlib axis object): the axis on which the hexagonal grid has been plotted.
                
    """

    ax = fig.add_subplot(111, aspect='equal')

    xpoints = [x[0]  for x in centers]
    ypoints = [x[1]  for x in centers]
    patches = []
    #is istance means that the first element is the type of the second one
    if any(isinstance(el, list) for el in weights) and len(weights[0])==3:
        cmap = plt.get_cmap('Greys')
        for x,y,w in zip(xpoints,ypoints,weights):
            hexagon = RegularPolygon((x,y), numVertices=6, radius=.95/np.sqrt(3), 
                                orientation=np.radians(0), 
                                facecolor=cmap(w))
            ax.add_patch(hexagon)

    else:
            
        cmap = plt.get_cmap('Greys')
        for x,y,w in zip(xpoints,ypoints,weights):
            hexagon = RegularPolygon((x,y), numVertices=6, radius=.95/np.sqrt(3), 
                                orientation=np.radians(0), 
                                facecolor=cmap(w))
            patches.append(hexagon) 

        p = PatchCollection(patches)
        p.set_array(np.array(weights))
        ax.add_collection(p)
        
    ax.axis('off')
    ax.autoscale_view()
    
    return ax
