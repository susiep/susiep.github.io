#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Import libraries needed
import random
import sys
import agentframework
import csv


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
print ("Model\n Number of people: %s\n Number of iterations: %s\n Neighbourhood size: %s"% 
       (sys.argv[1], sys.argv[2], sys.argv[3])) 

#Creating the people
people = []                                                     #Make empty people list       
for i in range (num_of_people):                                 #For specified number of people
    people.append(agentframework.Person(orchard, people))       #Create an person from the framework and append to the list
    people[i].setx()                                            #Use set and get functions to safeguard the x,y variables
    people[i].getx()
    people[i].sety()
    people[i].gety()
    
#Run the model
for j in range(num_of_iterations):                          #For every iteration
    random.shuffle(people, random = None)                   #Shuffle the order the people are processed
    for i in range (num_of_people):                         #For every person
        people[i].move()                                    #Move the person
        people[i].pick_fruit()                               #Make them eat
        people[i].share_with_neighbours(neighbourhood)      #Allow them to share with their neighbours
        people[i].drop()                                    #Cultivate the orchard           

#Write out the csv file and save in same directory
csvfile = open('out.csv', 'w', newline='')
writer = csv.writer(csvfile, delimiter=',')
for row in orchard:
    writer.writerow(row)
csvfile.close()
