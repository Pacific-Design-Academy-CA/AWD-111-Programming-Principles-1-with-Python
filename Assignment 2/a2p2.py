#!/usr/bin/env python3


def printMultipleLines(word, lines):
    ''' Input: word -> String: The word that needs to be printed multiple times
               lines -> Integer: Number of lines the word has to printed'''
    ''' Operation: print the word in as many new lines'''
    ''' Output: If word is "two" and lines is 2 then output,
        two
        two 
    '''
    ''' Invalid Input: If the value of lines is not greater than 0'''
    ''' Associated Test Case: testPrintMultipleLines()'''
    pass
   


def printAllNumberNotDivisible(number, lowerRange, upperRange):
    ''' Input: number->Integer: number is used to check for divisibilty
               lowerRange->Integer: lower limit of range
               upperRange->Integer: higher limit of range 
    '''
    ''' Output: Print all the numbers from lowerRange to higherRange that are not a multiple of number in new lines'''
    ''' Invalid Input: If lowerRange is less than 1'''
    ''' Associated Test Case: testPrintAllNumberNotDivisible()'''
    pass



def calculateDigitsAndLettersInString(string):
    ''' Input: string->Sting'''
    ''' Output: print the number of letters and digits in string in separate new lines
    for "darne23ll1" output:
        6
        3
    "'''
    ''' Invalid Input: None'''
    ''' Associated Test Case: testCalculateDigitsAndLettersInString'''
    pass


if __name__ == '__main__':
    
    print("Test case for printMultipleLines(word, lines):\n\n case 1: Python;5\n case 2: Loops;6\n case 3: while;-3\n")
    printMultipleLines("Python",5)
    printMultipleLines("Loops",6)
    printMultipleLines("while",-3)

    print("\nTest case for printAllNumberNotDivisible(number, range):\n\n case 1: 3;12\n case 2: 2;10\n case 3: 9;45\n")
    printAllNumberNotDivisible(3,9,13)
    printAllNumberNotDivisible(2,1,10)
    printAllNumberNotDivisible(9,-45, 21)

    print("\nTest case for calculateDigitsAndLettersInString(string):\n\n case 1: darne23ll1\n case 2: chri5top6he3\n case 3: jun10r\n")
    calculateDigitsAndLettersInString("darne23ll1")
    calculateDigitsAndLettersInString("chri5top6he3")
    calculateDigitsAndLettersInString("jun10r")

    
