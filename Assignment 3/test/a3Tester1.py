#external module

from io import StringIO
import unittest
from unittest.mock import patch

#local module
import a3p1

class TestThreePartOne(unittest.TestCase):

    def testReverseString(self):
        print("\nTest case for reverseString(string):\n\n case 1: reverse\n case 2: jigsaw\n case 3: carefree\n")
        result = a3p1.reverseString("reverse")
        self.assertEqual(result, "esrever")
        result = a3p1.reverseString("jigsaw")
        self.assertEqual(result,"wasgij")
        result = a3p1.reverseString("carefree")
        self.assertEqual(result,"eerferac")

    def testPrintContentOfList(self):
        print("\nTest case for printContentOfList(list):\n\n case 1: 3;12;12;2;2\n case 2: Mars;PDA;Victoria;Canada\n")
        with patch('sys.stdout', new = StringIO()) as fake_out:
            list1=[3,12,12,2,2]
            a3p1.printContentOfList(list1)
            self.assertEqual((fake_out.getvalue().strip()), "3\n12\n12\n2\n2" )
        with patch('sys.stdout', new = StringIO()) as fake_out:
            list2=["Mariah","PDA","Victoria","Canada"]
            a3p1.printContentOfList(list2)
            self.assertEqual((fake_out.getvalue().strip()), "Mariah\nPDA\nVictoria\nCanada" )
            
    def testPrintCommonStrings(self):
        print("\nTest case for printCommonStrings(list1,list2):\n\n case 1: m,s2,kq,js; ds,m,s2,kq,w\n case 2: mars,jupiter,panda,local; l,o,c,local,mar,juipter\n")
        with patch('sys.stdout', new = StringIO()) as fake_out:
            list1 = ["m","s2","kq","js"]
            list2 = ["ds","m","s2","kq","w"]
            a3p1.printCommonStrings(list1,list2)
            self.assertEqual(fake_out.getvalue().strip(),"m\ns2\nkq")
        with patch('sys.stdout', new = StringIO()) as fake_out:
            list1 = ['mars','jupiter','panda','local']
            list2 = ['l','o','c','local','mar','juipter']
            a3p1.printCommonStrings(list1,list2)
            self.assertEqual(fake_out.getvalue().strip(), "local")
    
    def testListDivisibleByNumber(self):
        print("\nTest case for listDivisibleByNumber(list1,number):\n\n case 1: 2,3,43,54,12,-2;2\n case 2: 0,0,0,2,1;-12\n")
        list1 = [2,3,43,54,12,-2,2]
        list2 = [2,54,12,-2,2]
        result = a3p1.listDivisibleByNumber(list1,2)
        self.assertEqual(list2,result)
        list1 = [0,0,0,2,1]
        list2 = [0,0,0]
        result = a3p1.listDivisibleByNumber(list1,-12)
        self.assertEqual(list2,result)

    def testUniqueElements(self):
        print("\nTest case for uniqueElements(list1):\n\n case 1: 2,3,43,54,12,-2\n case 2: 0,0,0,2,1\n case 3: m,1m,o2,m,m,m\n")
        list1 = [2,3,43,54,12,-2,2]
        list2 = [2,3,43,54,12,-2]
        result = a3p1.uniqueElements(list1)
        self.assertEqual(list2,result)
        list1 = [0,0,0,2,1]
        list2 = [0,2,1]
        result = a3p1.uniqueElements(list1)
        self.assertEqual(list2,result)
        list1 = ['m','1m','o2','m','m','m']
        list2 = ['m','1m','o2']
        result = a3p1.uniqueElements(list1)
        self.assertEqual(list2,result)

    
if __name__ == "__main__":
    unittest.main()