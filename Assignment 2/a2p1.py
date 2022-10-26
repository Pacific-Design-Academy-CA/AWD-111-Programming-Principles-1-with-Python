#!/usr/bin/env python3


def checkLegalVotingAge(age):
    ''' Input: An integer representing age '''
    ''' Output: If legal age for voting print "True" else "False"'''
    ''' Invalid Input: Anything else that's not greater than 0"'''
    ''' Associated Test Case: testCheckLegalVotingAge()'''
    pass
   


def checkIfNumberEvenOrOdd(number):
    ''' Input: An integer'''
    ''' Output: If even print "Even" else "Odd"'''
    ''' Invalid Input: None'''
    ''' Associated Test Case: testCheckIfNumberEvenorOdd()'''
    pass



def checkIfDivisible(numOne, numTwo, numThree):
    ''' Input: 3 integers'''
    ''' Output: check if numThree is divisible by both numOne and numTwo.
        If divisible by both the numbers print "True" else print "False" "'''
    ''' Invalid Input: None'''
    ''' Associated Test Case: testCheckIfDivisible()'''
    pass


def gradeCalculator(score):
    ''' Input: Acquired score'''
    ''' Output: Output the grade based one the following table:
        Score  Grade
        >= 0.9 A
        >= 0.8 B
        >= 0.7 C
        >= 0.6 D
        < 0.6  F
    "'''
    ''' Associated Test Case: testChecGradeCalculator()'''
    pass


def checkLeapYear(year):
    ''' Input: Given year '''
    ''' Output: If leap year print "True" else "False" '''
    ''' Associated Test Case: testCheckLeapYear() '''
    pass   


def checkSubString(string, subString):
    ''' Input: Given a string and a sub-string '''
    ''' Output: If sub-string present in string print "Present" else "Absent" '''
    ''' Invalid Input: None '''
    ''' Associated Test Case: testCheckSubStringInString() '''
    pass


def stringManipulationOne(string):
    ''' Input: A given String '''
    ''' Operation: Creat a new string using first 2 chars and last 2 chars of string'''
    ''' Output: If String is "PeterParker" output is "Peer" '''
    ''' Invalid Input: If a string length is less than 2 print "Invalid Input" '''
    ''' Associated Test Case: testStringManipulationOne() '''
    pass


if __name__ == '__main__':
    print("\nTest case for checkLegalVotingAge(age):\n\n case 1: 19\n case 2: 14\n")
    checkLegalVotingAge(19)
    checkLegalVotingAge(14)
    print("\nTest case for checkIfNumberEvenOrOdd(number):\n\n case 1: 222\n case 2: -123\n case 3: 45\n")
    checkIfNumberEvenOrOdd(222)
    checkIfNumberEvenOrOdd(-123)
    checkIfNumberEvenOrOdd(45)
    print("\nTest case for checkIfDivisible(numOne, numTwo, numThree):\n\n case 1:: 5;4;20\n case 2: 11;13;143\n case 3: -9;8;33\n")
    checkIfDivisible(5,4,20)
    checkIfDivisible(11,13,143)
    checkIfDivisible(-9,8,33)
    print("\nTest case for gradeCalculator(score):\n\n case 1: 0.6\n case 2: 0.92\n case 3: .76\n")
    gradeCalculator(0.6)
    gradeCalculator(0.92)
    gradeCalculator(0.76)
    print("\nTest case for checkLeapYear(year):\n\n case 1: 2004\n case 2: 2012\n case 3: 1223\n case 4: 1982\n")
    checkLeapYear(2004)
    checkLeapYear(2012)
    checkLeapYear(1223)
    checkLeapYear(1982)
    print("\nTest case for checkSubStringInString(string, subString):\n\n case 1: manchester;chest\n case 2: pomodoro;tomato\n case 3: jamesbond;bon\n")
    checkSubString("manchester","chest")
    checkSubString("pomodoro","tomato")
    checkSubString("jamesbond","bon")

    print("\nTest case for checkStringManipulationOne(string):\n\n case 1: LebronJames\n case 2: JustinTrudeau\n")
    stringManipulationOne("LebronJames") 
    stringManipulationOne("JustinTrudeau")
