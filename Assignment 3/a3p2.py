#!/usr/bin/env python3


def filteredString(list1, list2):
    #get rid of the same values that are present in both list1 and list2
    #create a list with the filtered values
    #print them
    pass
   


def squaredValues(list):
   #square the values in the list
   #create a new list of squared values
   #Print the list
    pass



def checkPangram(str):
    #given a string
    #check if the string is a pangram, look up google for definition of pangram
    #print "true" if pangram else "false"
    pass





if __name__ == '__main__':
    print("\nTest case for filtered(list, exception):\n\n case 1: a,s,e,q,f,ds; ds,s\n case 2: 0,12,102,0231,2,1; 0,1,12\n")
    list1 = ['a','s','e','q', 'f', 'ds']
    exceptList = ['ds','s']
    filteredString(list1, exceptList)
    print("\nTest case for squaredValues(list):\n\n case 1: 3,12,12,2,12\n case 2: 1,2,3,4,5\n")
    list1=[3,12,12,2,12]
    squaredValues(list1)
    list1=[1,2,3,4,5]
    squaredValues(list1)
    print("\nTest case for checkPangram(pangram):\n\n case 1: The quick brown fox jumps over the lazy dog\n case 2: mars jupiter panda oc local marjuipter\n")
    pangram = "The quick brown fox jumps over the lazy dog"
    checkPangram(pangram)
    pangram = "jupiter panda oc local marjuipter"
    checkPangram(pangram)
