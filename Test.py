# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 11:01:37 2022

@author: JM
"""
#Run block by block- Testing and Tasks
import matplotlib.pyplot as plt
import numpy as np
import RayTracer
import OpticalElements as oe
import Bundles
import RMS

r1=RayTracer.Ray()
assert all( r1.p() == np.array([0,0,0]) )
assert all( r1.k() == np.array([0,0,1]) )
r1.append([1,1,1],[1,1,1])
print(r1.p())
print(r1.k())
print(r1.vertices())
#Ray class test
#Checked if default values work as expected for attributes
#Checked if ray class methods work
#%%
r1=RayTracer.Ray(position=[0,0.3,0])
lens=oe.SphericalRefraction(5,5,1,1.6,0.1)
print(lens.intercept(r1))
#Intercept test with ray travelling in z hat direcetion
#Intercept when ray starts at [0,0,0] should be 5. Works-Normal Intercept
#Intercept when ray starts at [0,0,0.2] should be 5.2. Works-Tangential
#Intercept when ray starts at [0,0,>0.2] should be None. Works-No Intercept
#%%
r1=RayTracer.Ray(position=[0,0.2,0])
lens=oe.SphericalRefraction(1.8,5,1,1.6,2)
lens.intercept(r1)
print(lens.refraction(r1))
print(lens.refraction3(r1))
#Ray starting at [0,0,0], [0,0.1,0] and [0,0.2,0] have same new direction given\
    #by refraction and refraction3. Code matches theory.
#Verified refraction method works by comparing different formulas. refraction\
    #and refraction3 matches
#refraction3 was used from this point on. 
#%%
r1=RayTracer.Ray(position=[0,0.2,0])
lens=oe.SphericalRefraction(5,5,1,1.6,5)
lens.propagate_ray(r1)
plane=oe.OutputPlane(10)
plane.propagate_ray(r1)
print(r1.vertices())
#Verified output plane class works using ray travelling in z hat direcetion.
#Lens parameters (5,5,1,1.6,5)-->
#Position of ray [0,0.2,0]. Should propagate-tangential intersection. Works.
#Position of ray [0,>0.2,0]. Should have no intersect error. Works.
#Lens parameters (5,5,1,1.6,0.2)-->
#Position of ray [0,0.1,0]. Should propagate. Just within appeture. Works.
#Position of ray [0,0.2,0]. Should give appeture too small error. Works.
#Lens parameters (5,5,1.6,1,0.2)-->
#Position of ray [0,0.2,0]. Should fail as undergoes TIR. Works. 
#%%
#Task 9- Tracing few rays through specified surface
start=0
stop=30
rays=5
ypos=np.linspace(start,stop,rays)
arraysArray=[]
y=[]
z=[]
lens=oe.SphericalRefraction(100,0.03,1,1.5,50)
plane=oe.OutputPlane(200)
for j in range(rays):
    arraysArray.append([])
    y.append([])
    z.append([])

for x in range(rays):
    rayx=RayTracer.Ray(position=[0,ypos[x],0])
    lens.propagate_ray(rayx)
    plane.propagate_ray(rayx)
    arraysArray[x]=rayx.vertices()
    for i in range(3):
        y[x].append(arraysArray[x][i][1])
        z[x].append(arraysArray[x][i][2])
    plt.grid()
    plt.plot(z[x],y[x])
plt.xlabel("z (mm)")
plt.ylabel("y (mm)")
plt.show()        
#Shows convergence for positive curvature and divergence for negative curvature.
#Shows same behaviour for rays propagated in negative z direction. 
#%%
#Task 10- Focal length of specified surface
start=-0.1
stop=0.1
rays=10
ypos=np.linspace(start,stop,rays)
arraysArray=[]
y=[]
z=[]
lens=oe.SphericalRefraction(100,0.03,1,1.5,100)
plane=oe.OutputPlane(200)
for j in range(rays):
    arraysArray.append([])
    y.append([])
    z.append([])

for x in range(rays):
    rayx=RayTracer.Ray(position=[0,ypos[x],0],direction=[0,0,1])
    lens.propagate_ray(rayx)
    plane.propagate_ray(rayx)
    arraysArray[x]=rayx.vertices()
    for i in range(3):
        y[x].append(arraysArray[x][i][1])
        z[x].append(arraysArray[x][i][2])
    plt.grid()
    plt.plot(z[x],y[x])
plt.xlabel("z (mm)")
plt.ylabel("y (mm)")
plt.tight_layout()
plt.show()   
#Focal length f=100 mm. Matches theory.
#%%
#Task 11- Height of image test at output plane. Same specified surface.

#I adjusted these initial positions a lot arbitraily to get a spread. That's\
    #why a loop wasn't used initialisation.
r1=RayTracer.Ray(position=[0,0.1,0],direction=[0,0,1])
r2=RayTracer.Ray(position=[0,0.1,0],direction=[0,-0.0001,1])
r3=RayTracer.Ray(position=[0,0.1,0],direction=[0,-0.0002,1])

r4=RayTracer.Ray(position=[0,0.2,0])
r5=RayTracer.Ray(position=[0,0.2,0],direction=[0,-0.0001,1])
r6=RayTracer.Ray(position=[0,0.2,0],direction=[0,-0.0002,1])

r7=RayTracer.Ray(position=[0,0.3,0])
r8=RayTracer.Ray(position=[0,0.3,0],direction=[0,-0.0001,1])
r9=RayTracer.Ray(position=[0,0.3,0],direction=[0,-0.0002,1])

r10=RayTracer.Ray(position=[0,0.4,0])
r11=RayTracer.Ray(position=[0,0.4,0],direction=[0,-0.0001,1])
r12=RayTracer.Ray(position=[0,0.4,0],direction=[0,-0.0002,1])

r13=RayTracer.Ray(position=[0,0.5,0])
r14=RayTracer.Ray(position=[0,0.5,0],direction=[0,-0.0001,1])
r15=RayTracer.Ray(position=[0,0.5,0],direction=[0,-0.0002,1])
rays=[r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14,r15]#,r16,r17,r18]
arrays=[]
y=[]
z=[]
lens=oe.SphericalRefraction(150,0.03,1,1.5,25)
plane=oe.OutputPlane(330)
for i in range(len(rays)):
    arrays.append([])
    y.append([])
    z.append([])
for i in range(len(rays)):
    lens.propagate_ray(rays[i])
    plane.propagate_ray(rays[i])
    arrays[i]=rays[i].vertices()
    for j in range(3):
        y[i].append(arrays[i][j][1])
        z[i].append(arrays[i][j][2])
    plt.grid()
    plt.plot(z[i],y[i])
    print(y[i][2])

plt.xlabel("z (mm)")
plt.ylabel("y (mm)")
plt.tight_layout()
plt.show()
#Magnification of each image is -0.8. Matches theory (Lateral magnification).
#%%
#Task 12- Tracing bundle through same specified surface.
bundle1=Bundles.Bundle(0,5,6)
rays1,count=bundle1.GenerateBundle()

rayArray=[]
lensArray=[]
planesArray=[]
arraysArray=[]
x=[]
y=[]
z=[]
for i in range(count):
    lensArray.append([])
    planesArray.append([])
    arraysArray.append([])
    x.append([])
    y.append([])
    z.append([])
    
lens=oe.SphericalRefraction(100,0.03,1,1.5,10)   
plane=oe.OutputPlane(200)   
for n in range(count):
    lens.propagate_ray(rays1[n])
    plane.propagate_ray(rays1[n])
    arraysArray[n]=rays1[n].vertices()
    #print(arraysArray[0])
    for i in range(3):
        x[n].append(arraysArray[n][i][0])
        y[n].append(arraysArray[n][i][1])
        z[n].append(arraysArray[n][i][2])
    plt.grid()
    plt.plot(z[n],y[n],color="red")
plt.xlabel("z (mm)")
plt.ylabel("y (mm)")
plt.tight_layout()
plt.savefig("New Plot 3")
plt.show() 
#All rays in bundle meet at focal point. Matches previos observations.
#%%
#Task 13- Spot Diagram at focal plane for same specified surface.
bundle1=Bundles.Bundle(0,5,6)
rays1,count=bundle1.GenerateBundle()
lens=oe.SphericalRefraction(100,0.03,1,1.5,10)   
plane=oe.OutputPlane(200)
      
for n in range(count):
    lens.propagate_ray(rays1[n])
    plane.propagate_ray(rays1[n])

rad=RMS.SpotRadius(rays1)
RMS.SpotDiagram(rays1)
print("RMS Spot Radius: ", rad )
#%%
#Task 15 (flat surface first)-Paraxial Focal Point
start=-0.1
stop=0.1
rays=5
ypos=np.linspace(start,stop,rays)
rayArray=[]
arraysArray=[]
y=[]
z=[]
for i in range(rays):
    rayArray.append([])
    arraysArray.append([])
    y.append([])
    z.append([])
lens1=oe.SphericalRefraction(100,0,1,1.5168,10)
lens2=oe.SphericalRefraction(105,-0.02,1.5168,1,10)
planes=oe.OutputPlane(201.7)

for x in range(rays):
    rayArray[x]=RayTracer.Ray(position=[0,ypos[x],0],direction=[0,0,1])
    lens1.propagate_ray(rayArray[x])
    lens2.propagate_ray(rayArray[x])
    planes.propagate_ray(rayArray[x])
    arraysArray[x]=rayArray[x].vertices()
    #print(arraysArray)
    for i in range(4):
        y[x].append(arraysArray[x][i][1])
        z[x].append(arraysArray[x][i][2])
    plt.grid()
    plt.plot(z[x],y[x])
#plt.ylim(-0.005,0.005)
#plt.xlim(201,202)
plt.xlabel("z (mm)")
plt.ylabel("y (mm)")
plt.show() 
#Focal length  found to be f=99.2 mm.
#%%
#Task 15 (curved surface first)-Paraxial Focal Point
start=-0.1
stop=0.1
rays=5
ypos=np.linspace(start,stop,rays)
rayArray=[]
arraysArray=[]
y=[]
z=[]
for i in range(rays):
    rayArray.append([])
    arraysArray.append([])
    y.append([])
    z.append([])
lens1=oe.SphericalRefraction(100,0.02,1,1.5168,10)
lens2=oe.SphericalRefraction(105,0,1.5168,1,10)
planes=oe.OutputPlane(198.4)

for x in range(rays):
    rayArray[x]=RayTracer.Ray(position=[0,ypos[x],0],direction=[0,0,1])
    lens1.propagate_ray(rayArray[x])
    lens2.propagate_ray(rayArray[x])
    planes.propagate_ray(rayArray[x])
    arraysArray[x]=rayArray[x].vertices()
    #print(arraysArray)
    for i in range(4):
        y[x].append(arraysArray[x][i][1])
        z[x].append(arraysArray[x][i][2])
    plt.grid()
    plt.plot(z[x],y[x])
#plt.ylim(-0.005,0.005)
#plt.xlim(198,199)
plt.xlabel("z (mm)")
plt.ylabel("y (mm)")
plt.show()
#Focal length  found to be f=95.9 mm.
#%%
#Task 14/15- Incorporating Diffraction Limit.
appRad=np.linspace(0.1,10,100)
spotSize1=[]
spotSize2=[]
limit=[]
limit2=[]
for rad in appRad:
    bundle1=Bundles.Bundle(0,rad,6)
    bundle2=Bundles.Bundle(0,rad,6)
    rayArray,count=bundle1.GenerateBundle()
    rayArray2,count2=bundle2.GenerateBundle()
    firstlens1=oe.SphericalRefraction(100,0,1,1.5168,100)
    firstlens2=oe.SphericalRefraction(105,-0.02,1.5168,1,100)
    firstplane=oe.OutputPlane(201.7)
    secondlens1=oe.SphericalRefraction(100,0.02,1,1.5168,100)
    secondlens2=oe.SphericalRefraction(105,0,1.5168,1,100)
    secondplane=oe.OutputPlane(198.4)
    
    for n in range(count):
        firstlens1.propagate_ray(rayArray[n])
        firstlens2.propagate_ray(rayArray[n])
        firstplane.propagate_ray(rayArray[n])
        secondlens1.propagate_ray(rayArray2[n])
        secondlens2.propagate_ray(rayArray2[n])
        secondplane.propagate_ray(rayArray2[n])
    sRad=RMS.SpotRadius(rayArray)
    sRad2=RMS.SpotRadius(rayArray2)
    spotSize1.append(sRad*10E-3) 
    spotSize2.append(sRad2*10E-3)
    limit.append((588*10E-9)*(99.2/(2*rad)))
    limit2.append((588*10E-9)*(95.9/(2*rad)))

plt.plot(appRad,spotSize1,label="RMS Spot Radius (Flat Surface First)",color=\
         "Purple")
plt.plot(appRad,limit,"--", label="Diffraction Limit (Flat Surface First)",\
         color="blue")
plt.legend()
plt.xlabel("Beam Radius (mm)")
plt.ylabel("(m)")
plt.show()
plt.plot(appRad,spotSize2,label="RMS Spot Radius (Curved Surface First",color=\
         "Green")
plt.plot(appRad,limit2,"--", label="Diffraction Limit (Curved Surface First)",\
         color="red")
plt.legend()
plt.xlabel("Beam Radius (mm)")
plt.ylabel("(m)")
plt.show()
#Minimum beam apperture found to 3.265 mm for flat surface first planoconvex.
#Minimum beam apperture found to 4.770 mm for curved surface first planoconvex.
#%%
#Task 15 (flat surface first)- Spot Radius and Spot Diagram
#3.265mm beam gives minimum spot radius which stays within diffraction limit
bundle1=Bundles.Bundle(0,3.265,6)
rayArray,count=bundle1.GenerateBundle()
lens1=oe.SphericalRefraction(100,0,1,1.5168,10)
lens2=oe.SphericalRefraction(105,-0.02,1.5168,1,10)
plane=oe.OutputPlane(201.7)

for n in range(count):
    lens1.propagate_ray(rayArray[n])
    lens2.propagate_ray(rayArray[n])
    plane.propagate_ray(rayArray[n])

RMS.SpotDiagram(rayArray)
print("RMS Spot Radius:", RMS.SpotRadius(rayArray))    
    

#%%
#Task 15 (curved surface first)-Spot Radius and Spot Diagram
#4.770mm beam gives minimum spot radius which stays within diffraction limit
bundle1=Bundles.Bundle(0,4.770,6)
rayArray,count=bundle1.GenerateBundle()
lens1=oe.SphericalRefraction(100,0.02,1,1.5168,10)
lens2=oe.SphericalRefraction(105,0,1.5168,1,10)
plane=oe.OutputPlane(198.4)

for n in range(count):
    lens1.propagate_ray(rayArray[n])
    lens2.propagate_ray(rayArray[n])
    plane.propagate_ray(rayArray[n])
    
RMS.SpotDiagram(rayArray)
print("RMS Spot Radius:", RMS.SpotRadius(rayArray))
#%%
#Optimisation- Optimising Curvatures of Biconvex
import scipy.optimize as op
def lensOptimise(guess):
    """"Takes curvatures as parameters and returns RMS spot radius for beam\
        propagated through lens with those curvatures. Lens set to have focal\
            length f=100 mm. Beam has radius of 5 mm"""
    bundle1=Bundles.Bundle(0,5,6)
    rayArray,count=bundle1.GenerateBundle()
    curvature1,curvature2 = guess
    n=1.5168
    focusPoint=100
    arraysArray=[]
    x=[]
    y=[]
    z=[]
    SR1 = oe.SphericalRefraction(100,curvature1,1,1.5168,100)
    SR2 = oe.SphericalRefraction(105,curvature2,1.5168,1,100)
    OP = oe.OutputPlane(105+focusPoint)
    for n in range(count):
        SR1.propagate_ray(rayArray[n])
        SR2.propagate_ray(rayArray[n])
        OP.propagate_ray(rayArray[n])
    
    rms=RMS.SpotRadius(rayArray)
    return rms
j=op.fmin_tnc(lensOptimise,[0.0003,-0.0003], approx_grad=True, bounds=\
              ([0,0.05],[-0.05,0]),maxfun=250)
#Range of initial guesses tried to get global minimum.
#Global minimum when guesses of 0.001 and -0.001 used. Gives optimal curvatures\
    #of 0.1351 and -0.00548.
#%%
#Optimisation- Diffraction limit with ideal curvatures.
appRad=np.linspace(0.1,10,100)
spotSize=[]
limit=[]
for rad in appRad:
    bundle1=Bundles.Bundle(0,rad,6)
    rayArray,count=bundle1.GenerateBundle()
    lens1=oe.SphericalRefraction(100,0.01351,1,1.5168,100)
    lens2=oe.SphericalRefraction(105,-0.00548,1.5168,1,100)
    plane=oe.OutputPlane(205)
    for n in range(count):
        lens1.propagate_ray(rayArray[n])
        lens2.propagate_ray(rayArray[n])
        plane.propagate_ray(rayArray[n])
            #print(arraysArray)
#RMS.SpotDiagram(rayArray)
    sRad=RMS.SpotRadius(rayArray)
    spotSize.append(sRad*10E-3) 
    limit.append((588*10E-9)*(100/(2*rad)))
plt.plot(appRad,spotSize,label="RMS Spot Radius")
plt.plot(appRad,limit, label="Diffraction Limit")
plt.legend()
plt.xlabel("Beam Radius (mm)")
plt.ylabel("(m)")
plt.show()
#Minimum beam apperture found to 5.776 mm
#%%
#Optimisation- Spot Diagram and Spot Radius
#5.776 mm beam gives minimum spot radius which stays within diffraction limit
bundle1=Bundles.Bundle(0,5.776,6)
rayArray,count=bundle1.GenerateBundle()
lens1=oe.SphericalRefraction(100,0.01351,1,1.5168,100)
lens2=oe.SphericalRefraction(105, -0.00548,1.5168,1,100)
plane=oe.OutputPlane(205)
for n in range(count):
    lens1.propagate_ray(rayArray[n])
    lens2.propagate_ray(rayArray[n])
    plane.propagate_ray(rayArray[n])       
        #print(arraysArray)
RMS.SpotDiagram(rayArray)
print("RMS Spot Radius:",RMS.SpotRadius(rayArray))



    