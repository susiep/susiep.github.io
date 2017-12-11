#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Import libraries needed
import random

#Create the person class
class Person():                                         #Create the class called Person
    def __init__ (self, orchard, people):           #Give each person attributes for...
        self._x = None                #x location (random)
        self._y = None                  #y location (random)
        self.orchard = orchard                          #orchard
        self.apples = 0                            #Store of apples
        self.people = people                            #Information about the other agents.
        
    def getx(self):
        return self._x
    
    def setx(self):
        self._x = random.randint(0,300)
        
    def gety(self):
        return self._y
    
    def sety(self):
        self._y = random.randint(0,300)
        
    def __str__(self):                                  #When an person is printed, return information about their position and no of apples
        return ("At position ( %d , %d ) and has %d apples " % (self.x, self.y,self.apples))
    
    def move(self):                                     #Define the move function
        if self.apples < 100:                           #If they have collected less than 100 apples then they move quicker
            if random.random() < 0.5:
                self._x = (self._x + 3) % 300             #Create a random motion of 3 spaces in x 
            else:
                self._x = (self._x - 3) % 300
            if random.random() < 0.5:                   #Create a random motion of 3 spaces in y 
                self._y = (self._y + 3) % 300
            else:
                self._y = (self._y - 3) % 300
        else:                                           #If they have collected more than 100 they move slower
            if random.random() < 0.5:
                self._x = (self._x + 1) % 300             #Create a random motion of 1 space in x 
            else:
                self._x = (self._x - 1) % 300
            if random.random() < 0.5:                   #Create a random motion of 1 space in y
                self._y = (self._y + 1) % 300
            else:
                self._y = (self._y - 1) % 300
            
    def pick_fruit(self):                                       #Define the pick_fruit function
        if self.orchard[self._y][self._x] > 5:                    #When the tree has more than 5 apples
            self.orchard[self._y][self._x] -=5                #Take 5 apples from the tree
            self.apples += 5                                     
        else:                                                   #When the tree has less than 5 apples
            self.apples += self.orchard[self._y][self._x]       #Pick all the apples
            self.orchard[self._y][self._x] == 0               
             
    def distance_between(self, people):                         #Calculate the distance between 2 agents
        return ((self._x - people._x)**2) + ((self._y - people._y)**2)**0.5
    
    def share_with_neighbours(self, neighbourhood):             #Define the share_with_neighbours function
        for person in self.people:                              #For every person...
            distance = self.distance_between(person)            #Calculate the distance between them and the other people
            if distance == 0:                                   #If the other person is themselves...
                break                                           #ignore it
            elif distance <= neighbourhood:                     #If the distance is less that the specified neighbourhood
                average = ((self.apples + person.apples)//2)    #Share the apples equally between the two people
                self.apples = average
                person.apples = average
    
    def drop (self):                                            #Define the drop function
         if self.apples > 140:                                  #If the agent has more than 140 apples
             apples_dropped = random.randint(20,100)            
             self.apples -=  apples_dropped                     #They drop between 20 and 100 apples
             self.orchard[self._y][self._x] += apples_dropped     #And give some back to the environment
             

            
             

                
            
                