#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 15:01:21 2017

@author: susiephilp
"""
#Import libraries needed
import random

#Create the agent class
class Agent():                                          #Create the class called Agent
    def __init__ (self, environment, agents):           #Give each agent attributes for...
        self.x = random.randint(0,300)                  #x location (random)
        self.y = random.randint(0,300)                  #y location (random)
        self.environment = environment                  #environment
        self.store = 0                                  #Food store
        self.agents = agents                            #Information about the other agents.
        
    def __str__(self):                                  #When an agent is printed, return information about their position and store 
        return ("At position ( %d , %d ) and has a store value of %d" % (self.x, self.y,self.store))
    
    def move(self):                                     #Define the move function
        if self.store < 1000:                           #If they have eaten less than 1000
            if random.random() < 0.5:
                self.x = (self.x + 1) % 300             #Create a random motion of 1 space in x 
            else:
                self.x = (self.x - 1) % 300
            if random.random() < 0.5:                   #Create a random motion of 1 space in y 
                self.y = (self.y + 1) % 300
            else:
                self.y = (self.y - 1) % 300
        else:                                           #If they have eaten more than 1000
            if random.random() < 0.5:
                self.x = (self.x + 3) % 300             #Create a random motion of 3 spaces in x 
            else:
                self.x = (self.x - 3) % 300
            if random.random() < 0.5:                   #Create a random motion of 3 spaces in y
                self.y = (self.y + 3) % 300
            else:
                self.y = (self.y - 3) % 300
            
    def eat(self):                                              #Define the eat function
        if self.environment[self.y][self.x] > 10:               #When the environment has more than 10
            self.environment[self.y][self.x] -=10               #Take 10 from the environment
            self.store += 10                                    #Add 10 to the store
        else:                                                   #When the environment has less than 10
            self.store += self.environment[self.x][self.y]      #Add the environment to the store 
            self.environment[self.y][self.x] == 0               #Make the environment 0
             
    def distance_between(self, agents):                         #Calculate the distance between 2 agents
        return ((self.x - agents.x)**2) + ((self.y - agents.y)**2)**0.5
    
    def share_with_neighbours(self, neighbourhood):             #Define the share_with_neighbours function
        for agent in self.agents:                               #For every agent...
            distance = self.distance_between(agent)             #Calculate the distance between them and the other agents
            if distance == 0:                                   #If the other agent is themselves...
                break                                           #ignore it
            elif distance <= neighbourhood:                     #If the distance is less that the specified neighbourhood
                average = ((self.store + agent.store)//2)       #Share the store equally between the two agents
                self.store = average
                agent.store = average
    
    def vom (self):                                             #Define the vom function
         if self.store > 1200:                                  #If the agent has eaten more than 1200
             self.store -= 400                                  #They reduce their store
             self.environment[self.y][self.x] += 200            #And give some back to the environment
             

            
             

                
            
                