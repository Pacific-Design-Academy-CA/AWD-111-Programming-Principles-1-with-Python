#external module

from io import StringIO
import unittest
from unittest.mock import patch

#local module
import a2p2

class TestTwoPartTwo(unittest.TestCase):

    def testPrintMultipleLines(self):
        print("\nTest case for printMultipleLines(word, lines):\n\n case 1: Python;5\n case 2: Loops;6\n case 3: while;-3\n")
        with patch('sys.stdout', new = StringIO()) as fake_out:
            a2p2.printMultipleLines("Python",5)
            self.assertEqual((fake_out.getvalue().strip()), "Python\nPython\nPython\nPython\nPython")
        with patch('sys.stdout', new = StringIO()) as fake_out:
            a2p2.printMultipleLines("Loops",6)
            self.assertEqual((fake_out.getvalue().strip()), "Loops\nLoops\nLoops\nLoops\nLoops\nLoops")
        with patch('sys.stdout', new = StringIO()) as fake_out:
            a2p2.printMultipleLines("while",-3)
            self.assertEqual((fake_out.getvalue().strip()), "Invalid Input")

    def testPrintAllNumbersNotDivisible(self):
        print("\nTest case for printAllNumberNotDivisible(number, range):\n\n case 1: 3;12\n case 2: 2;10\n case 3: 9;45\n")
        with patch('sys.stdout', new = StringIO()) as fake_out:
            a2p2.printAllNumberNotDivisible(3,9,13)
            self.assertEqual((fake_out.getvalue().strip()), "10\n11" )
        with patch('sys.stdout', new = StringIO()) as fake_out:
            a2p2.printAllNumberNotDivisible(2,1,10)
            self.assertEqual((fake_out.getvalue().strip()), "1\n3\n5\n7\n9" )
        with patch('sys.stdout', new = StringIO()) as fake_out:
            a2p2.printAllNumberNotDivisible(9,-45, 21)
            self.assertEqual((fake_out.getvalue().strip()), "Invalid Input" )


    def testCalculateDigitsAndLettersInString(self):
        print("\nTest case for calculateDigitsAndLettersInString(string):\n\n case 1: darne23ll1\n case 2: chri5top6he3\n case 3: jun10r\n")
        with patch('sys.stdout', new = StringIO()) as fake_out:
            a2p2.calculateDigitsAndLettersInString("darne23ll1")
            self.assertEqual((fake_out.getvalue().strip()), "7\n3")
        with patch('sys.stdout', new = StringIO()) as fake_out:
            a2p2.calculateDigitsAndLettersInString("chri5top6he3")
            self.assertEqual((fake_out.getvalue().strip()), "9\n3")
        with patch('sys.stdout', new = StringIO()) as fake_out:
            a2p2.calculateDigitsAndLettersInString("jun10r")
            self.assertEqual((fake_out.getvalue().strip()), "4\n2")
 


    
if __name__ == "__main__":
    unittest.main()