#!/usr/bin/env python3


def reverseString(str):
    ''' Input: string -> String: The string that needs to be reversed '''
    ''' Operation: Reverse the given string'''
    ''' Output: If the string is "word",
        drow
    '''
    ''' Associated Test Case: testReverseString()'''
    pass
   


def printContentOfList(list):
    ''' Input: a list with some elements'''
    ''' Output: Print all the content of the list in separate lines'''
    ''' Associated Test Case: testPrintContentOfList()'''
    pass



def printCommonStrings(list1,list2):
    ''' Input: list1 & list2 are two lists with some strings'''
    ''' Output: print all the common strings between two lists
    separated by space,
    list1 = ["m","s2","kq","js"]
    list2 = ['ds','m','s2','kq','w']]
    output: "m kq"
    "'''
    ''' Invalid Input: None'''
    ''' Associated Test Case: testCalculateDigitsAndLettersInString'''
    pass

def listDivisibleByNumber(list1,number):
    #find all the numbers in list1 divisible by number
    #append it to a list
    #print the list
    pass

def uniqueElements(list1):  
    # print out the unique elements of list1
    pass
    





if __name__ == '__main__':
    print("\nTest case for reverseString(string):\n\n case 1: reverse\n case 2: jigsaw\n case 3: carefree\n")
    reverseString("reverse")
    reverseString("jigsaw")
    reverseString("carefree")
    print("\nTest case for printContentOfList(list):\n\n case 1: 3;12;12;2;2\n case 2: Mars;PDA;Victoria;Canada\n")
    list1=[3,12,12,2,2]
    printContentOfList(list1)
    list2=["Mariah","PDA","Victoria","Canada"]
    printContentOfList(list2)
    print("\nTest case for printCommonStrings(list1,list2):\n\n case 1: m,s2,kq,js; ds,m,s2,kq,w\n case 2: mars,jupiter,panda,local; l,o,c,local,mar,juipter\n")
    list1 = ["m","s2","kq","js"]
    list2 = ["ds","m","s2","kq","w"]
    printCommonStrings(list1,list2)
    list1 = ['mars','jupiter','panda','local']
    list2 = ['l','o','c','local','mar','juipter']
    printCommonStrings(list1,list2)
    print("\nTest case for listDivisibleByNumber(list1,number):\n\n case 1: 2,3,43,54,12,-2;2\n case 2: 0,0,0,2,1;-12\n")
    list1 = [2,3,43,54,12,-2,2]
    listDivisibleByNumber(list1,2)
    list1 = [0,0,0,2,1]
    listDivisibleByNumber(list1,-12)
    print("\nTest case for uniqueElements(list1):\n\n case 1: 2,3,43,54,12,-2\n case 2: 0,0,0,2,1\n case 3: m,1m,o2,m,m,m\n")
    list1 = [2,3,43,54,12,-2,2]
    uniqueElements(list1)
    list1 = [0,0,0,2,1]
    uniqueElements(list1)
    list1 = ['m','1m','o2','m','m','m']
    uniqueElements(list1)
