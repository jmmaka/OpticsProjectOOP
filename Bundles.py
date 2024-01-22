# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 20:53:42 2022

@author: JM
"""
import RayTracer
import numpy as np
import matplotlib.pyplot as plt
class Bundle:
    "Creates a bundle of rays with uniform ray density"
    def __init__(self,startr,stopr,rays,dotsPerRingAdded=6):
        """

        Parameters
        ----------
        startr : Float
            Starting value for rho coordinates in cylindrical polars.
        stopr : Float
            Maximum value for rho coordinates in cylindrical polars.
        rays : Integer
               Number of different equally spaced rho values. 
        dotsPerRingAdded : Integer, optional
            Number of dots rays added per successive rho value. The default is\
                6.

        Returns
        -------
        None.

        """
        self.startr=startr
        self.stopr=stopr
        self.start0=0
        self.stop0=2*np.pi
        self.rays=rays
        self.rings=dotsPerRingAdded+1
    def GenerateBundle(self,z0=0,direction=[0,0,1]):
        """
        Generates a bundle of rays by using the attributes of the bundle to 
        calculate the initial x and y coordinates of the rays. These are then 
        used to initialise an array of rays.

        Parameters
        ----------
        z0 :Float
            Position along the optical axis where the bundle starts. The\
                default is 0.
        direction :Array
                  Initial Ray Direction. The default is [0,0,1].
    

        Returns
        -------
        r1 : Returns an array which contains rays as objects of class ray type
        no : Returns number of rays in r1

        """
        self.xpos=[]
        self.ypos=[]
        #Generate list of possible rho values
        r=np.linspace(self.startr,self.stopr,self.rays)
        phi=[[0]]
        phicount=self.rings
        #Updates phi list to include a list possible equally spaced phi values\
            #at each rho
        #self.rings-1 phi values added to list each time
        for i in range(self.rays):
            phi.append(np.linspace(self.start0,self.stop0,phicount))
            phicount=(self.rings-1)+phicount
        #Conversion of every r and its possible phi values into cartesians\
            #coordinates
        for i in range(self.rays):
            maxIndex=len(phi[i])
            for j in range(maxIndex):
                self.xpos.append(r[i]*np.cos(phi[i][j]))
                self.ypos.append(r[i]*np.sin(phi[i][j]))
                
        r1=[]
        no=len(self.xpos)
        #Corrects for any floating point errors that occur due to finite\
            # precision of pi causing inability to correctly identify zeroes.
        for i in range(0,no):
            if self.ypos[i]>0:
                if self.ypos[i]<10E-10:
                    self.ypos[i]=0
            else:
                if self.ypos[i]>-10E-10:
                    self.ypos[i]=0
                
            if self.xpos[i]>0:   
                if self.xpos[i]<10E-10:
                    self.xpos[i]=0
            else:
                if self.xpos[i]>-10E-10:
                    self.xpos[i]=0
        #Initialising a list of rays with the initial positions found. This is\
            #bundle.
        for i in range(no):
            r1.append(RayTracer.Ray(position=[self.xpos[i],self.ypos[i],z0],\
                                    direction=direction))
        return r1,no
                