#!/usr/bin/env python3
import math


def printFloatingNumber():
    ''' Input: Ask the user for a floating number input '''
    ''' Print: Print the floating number '''
   


def sum(x,y):
    ''' Parameters: two numbers X and Y, Variables: Non-negative integers '''
    ''' Return: Sum of X and Y, Variables: Non-negative integers '''
    return 0



def average(x,y,z):
    ''' Parameters: Three numbers X, Y & Z, Variables: Non-negative integers '''
    ''' Return: Average of X,Y & Z, Variables: Integer '''
    return 0


def squareRoot(x):
    ''' Parameters: X '''
    ''' Return: square root of x upto 5 decimal places '''
    return 0


def volumeSphere(radius): 
    ''' Parameters: Radius of the sphere, Variable: Non-negative Integer'''
    ''' Return: Volume of the sphere, Variable:  Non-negative Floating point upto 5 decimal places'''
    return 0



def areaTriangle(base, height):
    ''' Parameters: Base & Height of the triangle, Variables: Non-negative Floating point upto 5 decimal places'''
    ''' Return: Area of the triangle, Variables: Non-negative Floating point upto 5 decimal places'''
    return 0

def solveProblemOne(x,y):
    ''' Parameters: X and Y, Solve: (X+Y)(X+Y), Variables: Integers/Floating point '''
    ''' Return:  If x : 2, y : 3, ans: 25, Variables: Float'''
    return 0


def solveProblemTwo(x):
    ''' Parameters: X, Solve: X + X^2 (x raised to the power of 2) + X^3(x raised to the power of 3), Variables: Integers/Floating point'''
    ''' Return: If X: 3, ans: 3 + 3^2 + 3^3 = 39, Variables:  Float'''
    return 0


if __name__ == '__main__':

    #1 output of printFloatingNumber()
    print("\t#1 printFloatingNumber()\t\n")
    printFloatingNumber()

    #2 output of sum()
    print("\t#2 sum()\t\n")
    x, y = 2,3
    sum_output = sum(x,y)
    print("Sum of",x,"&",y,":",sum_output)
    x, y = 180,33
    sum_output = sum(x,y)
    print("Sum of",x,"&",y,":",sum_output)
    x, y = 0,0
    sum_output = sum(x,y)
    print("Sum of",x,"&",y,":",sum_output)
    x, y = 2,-9
    sum_output = sum(x,y)
    print("Sum of",x,"&",y,":",sum_output)

    #3 output of average()
    x,y,z = 2,3,4
    print("\t#3 average()\t\n")
    average_output = average(x,y,z)
    print("Average of",x,"&",y,"&",z,":",average_output)
    x,y,z = 13,32,200
    average_output = average(222,-257,452)
    print("Average of",x,"&",y,"&",z,":",average_output)
    x,y,z = 2,3,4
    average_output = average(15,22,-55)
    print("Average of",x,"&",y,"&",z,":",average_output)

    #4 output of squareRoot()
    print("\t#4 squareRoot()\t\n")
    x = 2
    sqre_output = squareRoot(x)
    print("Square root of",x,":",sqre_output)
    x = 1445
    sqre_output = squareRoot(x)
    print("Square root of",x,":",sqre_output)
    x = 221
    sqre_output = squareRoot(x)
    print("Square root of",x,":",sqre_output)

    #5 output of volumeSphere()
    print("\t#5 volumeSphere()\t\n")
    x = 55
    volume_output = volumeSphere(x)
    print("Volume of Sphere with radius",x,":",volume_output)
    x = 122
    volume_output = volumeSphere(x)
    print("Volume of Sphere with radius",x,":",volume_output)
    x = 6
    volume_output = volumeSphere(x)
    print("Volume of Sphere with radius",x,":",volume_output)

    #6 output of areaTriangle()
    print("\t#6 areaTriangle()\t\n")
    x,y = 25,60
    area_output = areaTriangle(x,y)
    print("Area of a triangle with base",x," & height",y,":",area_output)
    x,y = 122,540
    area_output = areaTriangle(x,y)
    print("Area of a triangle with base",x," & height",y,":",area_output)
    x,y = 90.14324,111.123213
    area_output = areaTriangle(x,y)
    print("Area of a triangle with base",x," & height",y,":",area_output)

    #7 output of solveProblemOne()
    print("\t#7 solveProblemOne()\t\n")
    x,y = 16, 42
    problemOne_output = solveProblemOne(x,y)
    print("Solve problem one output with",x,"&",y,":",problemOne_output)
    x,y = -122, 540.22
    problemOne_output = solveProblemOne(x,y)
    print("Solve problem one output with",x,"&",y,":",problemOne_output)
    x,y = 90, 111
    problemOne_output = solveProblemOne(x,y)
    print("Solve problem one output with",x,"&",y,":",problemOne_output)
    

    #8 output of solveProblemTwo()
    print("\t#6 solveProblemTwo()\t\n")
    x = 16
    problemTwo_output = solveProblemTwo(x)
    print("Solve problem two output with",x,":",problemTwo_output)
    x = -122
    problemTwo_output = solveProblemTwo(x)
    print("Solve problem two output with",x,":",problemTwo_output)
    x = 111.22
    problemTwo_output = solveProblemTwo(x)
    print("Solve problem two output with",x,":",problemTwo_output)
    
