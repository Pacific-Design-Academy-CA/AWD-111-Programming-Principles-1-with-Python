#external module

from io import StringIO
import unittest
from unittest.mock import patch

#local module
import a4p2

class TestFourPartTwo(unittest.TestCase):

    def testPrintNlinesFromFile(self):
        print("\nTest case for testPrintNlinesFromFile(fileName, nlines):\n\n case 1: 'plain.txt',3\n case 2: 'demo.txt',5\n")
        with patch('sys.stdout', new = StringIO()) as fake_out:
            a4p2.printNlinesFromFile("plain.txt",3)
            self.assertEqual((fake_out.getvalue().strip()), "What is\nPython\nlanguage?")
        with patch('sys.stdout', new = StringIO()) as fake_out:
            a4p2.printNlinesFromFile("demo.txt",5)
            self.assertEqual((fake_out.getvalue().strip()), "programming\nparadigms\nincluding\nobject-oriented\nimperative and")

    def testStoreNlinesFromFile(self):
        print("\nTest case for storeNlinesFromFile(fileName, nlines):\n\n case 1: 'plain.txt',3\n case 2: 'demo.txt',5\n")
        result = a4p2.storeNlinesFromFile("demo.txt",3)
        list1 = ["programming","paradigms","including"] 
        self.assertEqual(list1,result)
        result = a4p2.storeNlinesFromFile("plain.txt",5)
        list1 = ["What is", "Python", "language?","Python","general-purpose"]
        self.assertEqual(list1,result)
            
    def testFindLongestWordFromFile(self):
        print("\nTest case for findLongestWordFromFile('plain.txt'):\n\n case 1: 'plain.txt'\n case 2: 'demo.txt'\n")
        with patch('sys.stdout', new = StringIO()) as fake_out:
            a4p2.findLongestWordFromFile("plain.txt")
            self.assertEqual(fake_out.getvalue().strip(),"general-purpose")
        with patch('sys.stdout', new = StringIO()) as fake_out:
            a4p2.findLongestWordFromFile("demo.txt")
            self.assertEqual(fake_out.getvalue().strip(),"object-oriented")


            


    
if __name__ == "__main__":
    unittest.main()