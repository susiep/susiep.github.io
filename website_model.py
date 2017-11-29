#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 16:01:09 2017

@author: susiephilp
"""
#Import libraries needed
import random
import sys
import matplotlib.pyplot
import matplotlib.animation
import agentframework
import csv

#path to ffmpeg needed to save animation
matplotlib.pyplot.rcParams['animation.ffmpeg_path'] = '/usr/local/bin/ffmpeg'

#Creating the orchard environment
orchard = []                                            #Make empty orchard environment list
f = open('in.txt', newline='')                          #open in the in.txt file as f
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)    #read in f as a csv called reader
for row in reader:                                      #For every row in reader
    rowlist = []                                        #Create a new list
    for value in row:                                   #For every value in row
        rowlist.append(value)                           #Add the value to the row list
    orchard.append(rowlist)                             #When finished, append all the row lists to the environment list
f.close()                                               #Close the file

#Define model parameters
num_of_people = 10                                      #Define number of people
num_of_iterations = 100                                 #Define number of model iterations
neighbourhood = 30                                      #Define distance which people can interact with each other


#Command line arguments
#Allows model to be run from the command line by specifying the 3 parameters
sys.argv.extend([num_of_people, num_of_iterations, neighbourhood])
print ("Model\n Number of people: %s\n Number of iterations: %s\n Neighbourhood size: %s"% (sys.argv[1], sys.argv[2], sys.argv[3])) 

#Defining animation result parameters
fig =  matplotlib.pyplot.figure(figsize=(7, 7))         #Create the figure, called fig
matplotlib.pyplot.xlim(xmax = 300)                      #Define the size of the x axis
matplotlib.pyplot.ylim(ymax = 300)                      #Define the size of the y axis

#Creating the agents
people = []                                                     #Make empty people list       
for i in range (num_of_people):                                 #For specified number of people
    people.append(agentframework.Person(orchard, people))       #Create an person from the framework and append to the list
    

#Instructions for every animation frame
def update(frame_number):                                       #For each update
    fig.clear()                                                 #Clear the figure
    matplotlib.pyplot.xlim(xmax = 300)                          #Reset the x axis to 300
    matplotlib.pyplot.ylim(ymax = 300)                          #Reset the y axis to 300
    for j in range(num_of_iterations):                          #For every iteration
        random.shuffle(people, random = None)                   #Shuffle the order the people are processed
        for i in range (num_of_people):                         #For every person
            people[i].move()                                    #Move the person
            people[i].pick_fruit()                               #Make them eat
            people[i].share_with_neighbours(neighbourhood)      #Allow them to share with their neighbours
            people[i].drop()                                    #Cultivate the orchard           
    matplotlib.pyplot.imshow(orchard)                           #Show the orchard environment
    for i in range(num_of_people):                              #For every person load into animation frame
            matplotlib.pyplot.scatter(people[i].x,people[i].y, color = 'lightblue')

#Run the animation
animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations)
fig.show()
#Save the animation
animation.save('an.mp4', writer='imagemagick', dpi= 80, fps=5)