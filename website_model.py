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

#Creating the environment
environment = []                                        #Make empty environment list
f = open('in.txt', newline='')                          #open in the in.txt file as f
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)    #read in f as a csv called reader
for row in reader:                                      #For every row in reader
    rowlist = []                                        #Create a new list
    for value in row:                                   #For every value in row
        rowlist.append(value)                           #Add the value to the row list
    environment.append(rowlist)                         #When finished, append all the row lists to the environment list
f.close()                                               #Close the file

#Define model parameters
num_of_agents = 10                                      #Define number of agents
num_of_iterations = 100                                 #Define number of model iterations
neighbourhood = 30                                      #Define distance which agents can interact with each other


#Command line arguments
#Allows model to be run from the command line by specifying the 3 parameters
sys.argv.extend([num_of_agents, num_of_iterations, neighbourhood])
print ("Model\n Number of agents: %s\n Number of iterations: %s\n Neighbourhood size: %s"% (sys.argv[1], sys.argv[2], sys.argv[3])) 

#Defining animation result parameters
fig =  matplotlib.pyplot.figure(figsize=(7, 7))         #Create the figure, called fig
matplotlib.pyplot.xlim(xmax = 300)                      #Define the size of the x axis
matplotlib.pyplot.ylim(ymax = 300)                      #Define the size of the y axis

#Creating the agents
agents = []                                                     #Make empty agent list       
for i in range (num_of_agents):                                 #For specified number of agents
    agents.append(agentframework.Agent(environment, agents))    #Create an agent from agent framework and append to the list
    

#Instructions for every animation frame
def update(frame_number):                                       #For each update
    fig.clear()                                                 #Clear the figure
    matplotlib.pyplot.xlim(xmax = 300)                          #Reset the x axis to 300
    matplotlib.pyplot.ylim(ymax = 300)                          #Reset the y axis to 300
    for j in range(num_of_iterations):                          #For every iteration
        random.shuffle(agents, random = None)                   #Shuffle the order the agents are processed
        for i in range (num_of_agents):                         #For every agent
            agents[i].move()                                    #Move the agent
            agents[i].eat()                                     #Make them eat
            agents[i].share_with_neighbours(neighbourhood)      #Allow them to share with their neighbours
            agents[i].vom()                                     #Allow them to throw up           
    matplotlib.pyplot.imshow(environment)                       #Show the environment
    for i in range(num_of_agents):                              #For every agent load into animation frame
            matplotlib.pyplot.scatter(agents[i].x,agents[i].y, color = 'lightblue')

#Run the animation
animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations)
fig.show()


