# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 10:29:08 2022

@author: JM
"""

"""
This module contains the ray class.

"""
import numpy as np

class Ray:
    """
    Creates a ray as an object.
    
    """
    def __init__(self, position=[0,0,0], direction=[0,0,1]):
        """
        

        Parameters
        ----------
        position : Array
                  Initial Ray Position. The default is [0,0,0].
        direction :Array
                  Initial Ray Direction. The default is [0,0,1].

        Returns
        -------
        None.

        """
        self.points=[np.array(position)]
        kMag=np.linalg.norm(direction)
        self.direction=[np.array(direction)/kMag]
    
    def p(self):
        """Returns current position of ray"""
        return self.points[-1]
    
    def k(self):
        """Returns current direction of ray"""
        return self.direction[-1]
    
    def append(self, p, k):
        """
        Adds new point along ray
        

        Parameters
        ----------
        p : Numpy Array
            New position.
        k : Numpy Array
            New position's direction

        Returns
        -------
        None.

        """
        kMag=np.linalg.norm(k)
        
        self.points.append(np.array(p))
        self.direction.append(np.array(k)/kMag)
    
    def vertices(self):
        """Returns all the positions of the ray that it passes through as it\
            propagates"""
        return self.points

