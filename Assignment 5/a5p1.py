#!/usr/bin/env python3
import sys
import argparse

def printFormat():	
	pass


	#takes the inputFileName and returns a list of lines in the file
def input_line():
	pass
	
	
	#takes the list of inputLine and returns a list of words in the lines
def input_word(inputLine):
	pass
	
	
	
	#takes the exceptFileName and returns a list of words in the file
def except_word(exceptFileName):
	pass
	
	
	#takes the inputList and exceptList
def filter_words():
	pass	
	
def longest_word(uniqueWords):
	pass
	


def main():
	exceptFileName = None
	inputFileName  = None
	
		
	#calling function input_line() which returns 'lines' from the input file
	#inputLine is in lowercase
	inputLine=input_line(inputFileName)
	
	#calling function input_word() which returns all the words from the lines 
	inputList=input_word(inputLine)

	#calling function except_word() which returns all the words from the exception file
	exceptList=except_word(exceptFileName)
	
	#calling function unique_words() which returns all the unique words sorted alphabetically
	uniqueWords=filter_words(inputList,exceptList)
	
	#calling function longestWordLength() which returns the longest keyWord
	longestWordLength=longest_word(uniqueWords)	
			
	
if __name__=='__main__':
	main()
