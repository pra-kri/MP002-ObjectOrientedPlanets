"""
Created on Tue Mar 27 12:55:28 2018

@author: krishnap
"""
# Python practice 
# OOP Planet Motion simulation  (no gravity...yet)


import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

plt.axis([-50,50,-50,50])

#plt.ion is for turning on the 'interactive mode' in matplotlib
#allows plot to be updated in real time, so technically its not a proper 'animation'...
plt.ion()

class OOP_body:
    def __init__(self, Rad, angvel, parent_body = None):
        self.Radius = Rad
        self.wstar = angvel
        self.parent = parent_body
        
    def getX(self, time):
        if self.parent == None:
            return (self.Radius * np.cos(self.wstar * time))
        else:    
            return (self.parent.getX(time) + (self.Radius * np.cos(self.wstar * time)))
        # x = Rcos(wt)        
        
    def getY(self, time):
        if self.parent == None:
            return (self.Radius * np.sin(self.wstar * time))
        else:
            return (self.parent.getY(time) + (self.Radius * np.sin(self.wstar * time)))
        # y = Rsin(wt)
       
    def position(self):
        for time in np.arange(0, 2.5, 0.02):
            x_pos = self.getX(time)
            y_pos = self.getY(time)
            print('%f, %f' %(x_pos, y_pos))            
            plt.scatter(x_pos, y_pos)
            # pauses for a bit until jumping to the next iteration.
            plt.pause(0.01)
            


        

    
star = OOP_body(30.0, 2)
#star.position()
planet = OOP_body(14.0, 7, star)
#planet.position()
moon = OOP_body(7.0, 12, planet)
moon_moon = OOP_body(3, 10, moon)
moon_moon_moon = OOP_body(1, 60, moon_moon)
# works until here. numbers are fine, need to figure out how to plot this stuff...
star.position()
planet.position()
moon.position()
moon_moon.position()
moon_moon_moon.position()

'''
##### extra stuff to incorporate: animation, properly, instead of just updating with ion()
fig = plt.figure() 
ani = animation.FuncAnimation(fig, moon.position(), interval=1000)
plt.show()

[/] DONE - rewrote code all into 1 single object. (Before, there were multiple objects.)
Got rid of OOP_planet, OOP_moon and jsut keep OOP_body, but wiht an extra input: parent = None as default.

'''
