# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 21:25:08 2022

@author: JM
"""
import numpy as np
class OpticalELement:
    """Creates an optical element as an object"""
    def propagate_ray(self, ray):
        """
        

        Parameters
        ----------
        ray : Ray Object
            Ray to be propagated.

        Returns
        -------
        bool
            DESCRIPTION.
            
            
        Raises
        -------
        Exception: No intercept with lens
                   When ray doesn't intersect with spherical surface.
        Exception: Total Internal Reflection
                   If ray undergoes total internal reflection,
        Exception: Apperture of lens too small
                   When ray intersects with surface but the extent of lens is\
                       not enough.         
                   
        """
        #Obtain intercept with optical element
        intersection=self.intercept(ray)
        #Check if there is a valid intercept with the sphere
        if intersection is None:
            raise Exception("No intercept with lens")
        else:
            #Obtain new direction due to refraction by optical element
            returnRay=self.refraction3(ray)
            #Check that TIR doesn't occur
            if returnRay is None:
                raise Exception("Total Internal Reflection Occurs")
            else:
                newpos=ray.p()+intersection*ray.k()
                #Check if apperture is large enough
                if np.sqrt(newpos[0]**2+newpos[1]**2)>self.appertureRadius:
                    raise Exception("Apperture of lens too small")
                newk=returnRay
                ray.append(newpos,newk)
                return True
                
              
                

class SphericalRefraction(OpticalELement):
    """
    Creates a spherical surface as an optical element.
    
    """
    def __init__(self,z0,curvature,n1,n2,appertureRadius):
        """
        

        Parameters
        ----------
        z0 : Float
            Position of surface along the z-axis (Optical axis).
        curvature : Float
            The curvature of the surface.
        n1 : Float
            Refractive index of the material the ray is initially propagating\
                through.
        n2 : FLoat
            Refractive index of material ray is propagating through after\
                interaction with surface.
        appertureRadius : Float
            Apperture of the lens.

        Returns
        -------
        None.

        """
        self.z0=z0
        self.curvature=curvature
        self.n1=n1
        self.n2=n2
        self.appertureRadius=appertureRadius
        self.norm=[0,0,1]
        
    def intercept(self,ray):
        """
        Calculates distance to intercept point with lens from current point,\
            if any. Method varies depending on the nature of the curvature and\
                direction of ray propagation.

        Parameters
        ----------
        ray : Object of ray class
              Ray that needs to be propagated
    

        Returns
        -------
        l : The distance to intercept from current point
        
        
        """
        
        if self.curvature==0:
            #Deals with the intercept if curvature is 0. Treats surface as\
                #plane.
            zp=ray.p()[2]
            zk=ray.k()[2]
            l=(self.z0-zp)/zk
            newpos=ray.p()+ray.k()*l
            return l
        if ray.k()[2]>0:
            #Center of sphere if ray propagates in positive z direction.
            center=[0,0,self.z0+(1/self.curvature)]
        else:
            #Center of sphere if ray propagates in negative z direction.
            center=[0,0,self.z0-(1/self.curvature)]
        self.center=np.array(center)
        r=ray.p()-self.center
        dis=(np.dot(r,ray.k()))**2-((np.linalg.norm(r))**2-(1/self.curvature)\
                                    **2)
        if dis<0:
            #Physically corresponds to no intersections with the lens
            return None
        
        else:
            if dis>0:
               #Physically corresponds to 2 intersections with the lens
               a=(np.dot(-r,ray.k()))
               l1=np.dot(-r,ray.k())+np.sqrt(dis)
               l2=np.dot(-r,ray.k())-np.sqrt(dis)
               if self.curvature<0:
                   #If curvature is negative takes second intercept.\
                       #Ensures correct propagation direction.
                   l=l1
               else:
                   #If curvature is positive takes first intercept\
                       #Ensures correct propagation direction.
                   l=l2
               
            else:
                #Corresponds to tangential interaction with lens.
                l=-np.dot(r,ray.k()) 
            
        return l
    #Theoretical (hidden) click arrow on left near line number 158 to release-\
        #This was kept as proof of testing. It is not used beyond that.
    def refraction(self, ray):
        surfaceNormal=-self.intercept(ray)*ray.k()-((ray.p()-self.center))
        incidentDirection=ray.k()
        iMag=np.linalg.norm(incidentDirection)
        normMag=np.linalg.norm(surfaceNormal)
        i=np.array(incidentDirection)/iMag
        norm=np.array(surfaceNormal)/normMag
        theta=np.arccos(np.dot(i,norm))
        if np.sin(theta)>(self.n2/self.n1):
            #Corresponds to total internal reflection
            return None
        else:
            r=i-(np.dot(i,norm))*norm+(np.sqrt((self.n2)**2-(self.n1)**2+\
                                               (np.dot(i,norm))**2))*norm
            rMag=np.linalg.norm(r)
            r=r/rMag
        return r

    
    def refraction3(self,ray):
        """
        Calculates new ray direction due to refraction of ray at lens
        

        Parameters
        ----------
        ray : Object of ray class
              Ray that needs to be propagated
    

        Returns
        -------
        r : The new direction of the ray after refraction has occured
        
       

        """
        if self.curvature==0:
            #Deals with normal in the case the surface is planar
            surfaceNormal=(0,0,1)
        else:
            #Calculation of normal when curvature non zero
            center=[0,0,self.z0+(1/self.curvature)]
            self.center=np.array(center)
            surfaceNormal=-self.intercept(ray)*ray.k()-((ray.p()-self.center))
        i=ray.k()
        normMag=np.linalg.norm(surfaceNormal)
        norm=np.array(surfaceNormal)/normMag
        theta=np.arccos(np.dot(i,norm))
        if np.sin(theta)>(self.n2/self.n1):
            #Corresponds to total internal reflection
            return None
        else:
            if self.curvature<0:
                #If curvature is negative takes normal in opposite direction.\
                    #Equation always considers normal pointing towards lens
                
                norm=-norm
        
            ratio=self.n1/self.n2
            c=np.dot(norm,i)
            #Snell's Law in 3D. Reference:\
                #https://en.wikipedia.org/wiki/Snell%27s_law#cite_note-18
            r=ratio*i-(ratio*c-np.sqrt(1-(ratio**2)*(1-c**2)))*norm
            rmag=np.linalg.norm(r)   
            r=r/rmag
            return r
        

class OutputPlane(OpticalELement):
    """
    Creates an output plane for ray to be projected onto
    
    """
    def __init__(self,z0):
        """
        
        Parameters
        ----------
        z0 : Float
            Position of surface along optical axis.

        Returns
        -------
        None.

        """
        self.z0=z0
    def intercept(self,ray):
        """
        Calculates distance to intercept point with output plane from current\
            point
        

        Parameters
        ----------
        ray : Object of ray class
              Ray that needs to be propagated
    

        Returns
        -------
        l : The distance to intercept from current point
        
        """
        zp=ray.p()[2]
        zk=ray.k()[2]
        l=(self.z0-zp)/zk
        return l

    def propagate_ray(self, ray):
        "Propagates a ray through to the output plane"
        intersection=self.intercept(ray)
        newpos=ray.k()*intersection+ray.p()
        newk=ray.k()
        ray.append(newpos,newk)
        return True