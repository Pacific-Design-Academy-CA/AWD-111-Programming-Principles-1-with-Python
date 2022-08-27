#external module

from io import StringIO
import unittest
from unittest.mock import patch

#local module
import a3p2

class TestThreePartTwo(unittest.TestCase):

    def testFilteredString(self):
        print("\nTest case for filtered(list, exception):\n\n case 1: a,s,e,q,f,ds; ds,s\n case 2: 0,12,102,0231,2,1; 0,1,12\n")
        list1 = ['a','s','e','q', 'f', 'ds']
        list2 = ['a','e','q','f']
        exceptList = ['ds','s']
        result = a3p2.filteredString(list1, exceptList)
        self.assertEqual(result, list2)
        list1 = [0,12,102,2,1] 
        list2 = [102,2]
        exceptList = [0,1,12]
        result = a3p2.filteredString(list1,exceptList)
        self.assertEqual(result, list2)

    def testSquaredValues(self):
        print("\nTest case for squaredValues(list):\n\n case 1: 3,12,12,2,12\n case 2: 1,2,3,4,5\n")
        list1=[3,12,12,2,12]
        list2=[9,144,144,4,144]
        result = a3p2.squaredValues(list1)
        self.assertEqual(result, list2)
        list1=[1,2,3,4,5]
        list2=[1,4,9,16,25]
        result = a3p2.squaredValues(list1)
        self.assertEqual(result, list2)
            
    def testPangram(self):
        print("\nTest case for checkPangram(pangram):\n\n case 1: The quick brown fox jumps over the lazy dog\n case 2: mars jupiter panda oc local marjuipter\n")
        pangram = "The quick brown fox jumps over the lazy dog"
        bool_ = a3p2.checkPangram(pangram)
        self.assertEqual(bool_, True)
        pangram = "jupiter panda oc local marjuipter"
        bool_ = a3p2.checkPangram(pangram)
        self.assertEqual(bool_, False)

    
if __name__ == "__main__":
    unittest.main()