#external module

from io import StringIO
import unittest
from unittest.mock import patch

#local module
import a4p1

class TestFourPartOne(unittest.TestCase):

    def testDivisibleElementsDict(self):
        print("\nTest case for divisibleElementsDict(dict, number):\n\n case 1: 12,3,122,32,33,124; 3\n case 2: 34,12,102,0231,2,1; 2\n")
        dict1 = {1:12,2:3,3:122,4:32,5:33,6:124}
        dict2 = [12,3,33]
        result = a4p1.divisibleElementsDict(dict1,3)
        self.assertEqual(result, dict2)
        dict1 = {1:34,2:12,3:102,4:0,5:2,6:1}
        dict2 = [34,12,102,0,2]
        result = a4p1.divisibleElementsDict(dict1,2)
        self.assertEqual(result, dict2)


            
    def testRemoveDuplicate(self):
        print("\nTest case for removeDuplicate(dict):\n\n case 1: {'fox':[22,3,1],'tim':[2,3,1,12],'max':[12,0,43]}\n case 2: {'jupiter':['mars','may'],'ninja':['may','day']}\n")
        dict1 = {'fox':22,'tim':22,'max':19,'mary':12,'jone':19}
        dict2 = {'fox':22,'max':19,'mary':12} 
        result = a4p1.removeDuplicate(dict1)
        self.assertEqual(result,dict2)
        dict1 = {'jupiter':'mars','plan':'may','ninja':'may','time':'day','rhyme':'day'}
        dict2 = {'jupiter':'mars','plan':'may','time':'day'} 
        result = a4p1.removeDuplicate(dict1)
        self.assertEqual(result,dict2)

    def testMaxKeyInDict(self):
        print("\nTest case for maxKeyInDict(dict):\n\n case 1: {'fox':22,'tim':100,'max':21,'leon':43,'amy':75}\n case 2: {1:-12,2:-31,3:10,4:12,6:21}\n")
        with patch('sys.stdout', new = StringIO()) as fake_out:
            dict1 = {'fox':22,'tim':100,'max':21,'leon':43,'amy':75} 
            a4p1.maxKeyInDict(dict1)
            self.assertEqual((fake_out.getvalue().strip()),"tim")
        with patch('sys.stdout', new = StringIO()) as fake_out:
            dict1 = {1:-12,2:-31,3:10,4:12,6:21}
            a4p1.maxKeyInDict(dict1)
            self.assertEqual((fake_out.getvalue().strip()),"6")

    def testMeanDict(self):
        print("\nTest case for meanDict(dict):\n\n case 1: {'fox':22,'tim':100,'max':21,'leon':43,'amy':75}\n case 2: {1:-12,2:-31,3:10,4:12,6:21}\n")
        with patch('sys.stdout', new = StringIO()) as fake_out:
            dict1 = {'fox':22,'tim':100,'max':21,'leon':43,'amy':75} 
            a4p1.meanDict(dict1)
            self.assertEqual((fake_out.getvalue().strip()),"52")
        with patch('sys.stdout', new = StringIO()) as fake_out:
            dict1 = {1:-12,2:-31,3:10,4:12,5:21,6:56}
            a4p1.meanDict(dict1)
            self.assertEqual((fake_out.getvalue().strip()),"9")
            


    
if __name__ == "__main__":
    unittest.main()