# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 08:54:01 2022

@author: JM
"""
import matplotlib.pyplot as plt
import numpy as np
def SpotDiagram(rayArray):
    """
    Plots the spot diagram for a bundle of rays at the current position.

    Parameters
    ----------
    rayArray: Array
              Contains ray objects of which we need to plot the spot\
                  diagram of at current position.


    Returns
    -------
    None

    """
    x=[]
    y=[]
    for ray in rayArray:
        x.append(ray.vertices()[-1][0])
        y.append(ray.vertices()[-1][1])
    plt.grid()
    plt.plot(x,y,"o",color="red")
    plt.xlabel("x (mm)")
    plt.ylabel("y (mm)")
    plt.show()
    
def SpotRadius(rayArray):
    """
    Calculates the RMS spot radius for a bundle of rays at the current\
        position.

    Parameters
    ----------
    rayArray: Array
              Contains ray objects of which we need to calculate the spot\
                  radius of at the current position.


    Returns
    -------
    rad : Returns rms spot radius

    """
    sumOfSquares=0
    xcenter=0
    ycenter=0
    count=len(rayArray)
    for ray in rayArray:
        xcenter+=ray.p()[0]
        ycenter+=ray.p()[1]
    #Calculate the center x and y coordinates respectively.
    xcenter=xcenter/count
    ycenter=ycenter/count
    for ray in rayArray:
        #Reference:\
            #https://www.thepulsar.be/article/-devoptical-part-10--rms-spot-size/
        sumOfSquares+=((ray.p()[0]-xcenter)**2+(ray.p()[1]-ycenter)**2)
    rad=np.sqrt(sumOfSquares/count)
    return rad
