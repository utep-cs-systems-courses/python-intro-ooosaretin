# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 18:18:05 2020

@author: wenro
"""
import string
#Open a text file
textFile = open("speech.txt", "r")
#Create an empty dictionary
makeDictionary = dict()
#Traverse through each lines in the text file
for eachLine in textFile:
    #Removes any spaces and new lines
    eachLine = eachLine.strip()
    #Made all the words lower case
    eachLine = eachLine.lower()
    #Removes any punctuations 
    eachLine = eachLine.translate(eachLine.maketrans("","", string.punctuation))
    #Put each words in their own lines
    allWords = eachLine.split()
    #Traverse through all the words
    for eachWord in allWords:
        #Check if the word exist in the dictionary list
        if eachWord in makeDictionary:
            #If so, then it adds one to the word
            makeDictionary[eachWord] = makeDictionary[eachWord] + 1
        else:
            #If it is not so, then it equals one intead
            makeDictionary[eachWord] = 1
#Print out the results in descending order
for outputWord in sorted(makeDictionary.keys(), reverse=True):
    print(outputWord, " ", makeDictionary[outputWord])