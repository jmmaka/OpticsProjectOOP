In this project I have coded an Optical Ray Tracer using Object Oriented Programming on Python.


List of Modules (Files):
RayTracer.py
OpticalElements.py
Bundles.py
RMS.py
Test.py


RayTracer.py:
This module contains the Ray class. Rays can be instantiated and then methods can be used to obtain the current direction, current position, append new positions and directions and return all the positions of the ray during propagation.


OpticalElements.py:
This module contains the OpticalElement class along with SphericalRefraction and OutputPlane subclasses. Apart from instantiating the optical elements, there are methods to find the intercept of the ray with the element, refract the ray and change its direction (if it is a refractor) and most importantly, propagate the ray through the surface using the “propagate_ray” method.


Important: There is a hidden block of code for a method called “refraction.” This contains a basic theoretical output for refraction which was used purely for testing purposes of the real method used for the rest of the system “refraction3”. It is kept there for proof of testing.


Bundles.py:
This module contains the bundle class. It allows for a bundle to be instantiated with specific properties as given by parameters and then uses the GenerateBundle method to create a uniform density bundle as an array of rays with properties.


RMS.py:
This module contains the SpotDiagram procedure which plots the spot diagram for a bundle given as an array of rays at the current point. It also contains the SpotRadius function which takes in a bundle as an array of rays and evaluates the RMS spot radius.


Test.py:
This creates separated blocks of code for every task with relevant comments. It contains all the proof of testing and covers all tasks in the script in order with brief explanation and listing of key results.