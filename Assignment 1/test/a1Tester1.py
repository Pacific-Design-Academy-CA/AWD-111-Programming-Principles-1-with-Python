#external module
from cmath import log
import math
from io import StringIO
from operator import imod
import unittest
from unittest.mock import patch

#local module
import a1p2

class TestOnePartOne(unittest.TestCase):

    def testCheckFloatingNumber(self):
        print("Test cases for checkFloatingNumber: \n case 1: 22.534124124\n case 2: 10.23325234\n")

        with patch('builtins.input', return_value=22.534124124), patch('sys.stdout', new = StringIO()) as fake_out:
            a1p2.printFloatingNumber()
            self.assertEqual(float(fake_out.getvalue().strip()), (22.53))
        with patch('builtins.input', return_value=10.23325234), patch('sys.stdout', new = StringIO()) as fake_out:
            a1p2.printFloatingNumber()
            self.assertEqual(float(fake_out.getvalue().strip()), (10.23))

    def testCheckSum(self):
        print("\nTest cases for checkSum: \n case 1: 2, 3\n case 2: 180, 33\n case 3: 0, 0\n case 4: 2, -9\n")
        self.assertEqual(5, a1p2.sum(2,3))
        self.assertEqual(213, a1p2.sum(180,33))
        self.assertEqual(0, a1p2.sum(0,0))
        self.assertEqual(-7, a1p2.sum(2,-9))

    def testAverage(self):
        print("\nTest cases for average(): \n case 1: 2, 3, 4\n case 2: 13, 32, 200\n case 3: 222, -257, 452\n case 4: 15, 22, -55\n")
        self.assertEqual(3, a1p2.average(2,3,4))
        self.assertEqual(81, a1p2.average(13,32,200))
        self.assertEqual(139, a1p2.average(222,-257,452))
        self.assertEqual(-6, a1p2.average(15,22,-55))

    def testSqrt(self):
        print("\nTest cases for squareRoot():\n case 1: 2\n case 2: 1445\n case 3: 221\n")
        self.assertEqual("{:.5f}".format(float(math.sqrt(2))),a1p2.squareRoot(2))
        self.assertEqual("{:.5f}".format(float(math.sqrt(1445))), a1p2.squareRoot(1445))
        self.assertEqual("{:.5f}".format(float(math.sqrt(221))), a1p2.squareRoot(221))

    def testVolumeSphere(self):
        print("\nTest cases for volumeSphere():\n case 1: 55\n case 2: 122\n case 3: 6\n")
        self.assertEqual(696909.97032, float(a1p2.volumeSphere(55)))
        self.assertEqual(7606206.31578, float(a1p2.volumeSphere(122)))
        self.assertEqual(904.77868, float(a1p2.volumeSphere(6)))

    def testAreaTriangle(self):
        print("\nTest cases for AreaTriangle(): \n case 1: 25, 60\n case 2: 122, 540\n case 3: 90.14324, 111.123213\n")
        self.assertEqual(750, float(a1p2.areaTriangle(25,60)))
        self.assertEqual(32940, float(a1p2.areaTriangle(122,540)))
        self.assertEqual(5008.50323, float(a1p2.areaTriangle(90.14324,111.123213)))
  
    def testSolveProblemOne(self):
        print("\nTest cases for solveProblemOne(): \n case 1: 16, 42\n case 2: -122, 540.22\n case 3: 90, 111\n")
        self.assertEqual(3364, float(a1p2.solveProblemOne(16, 42)))
        self.assertEqual(174907.9684, float(a1p2.solveProblemOne(-122,540.22)))
        self.assertEqual(40401, float(a1p2.solveProblemOne(90,111)))

    def testSolveProblemTwo(self):
        print("\nTest cases for solveProblemTwo():\n case 1: 16\n case 2: -122\n case 3: 111.22\n")
        self.assertEqual(4368, float(a1p2.solveProblemTwo(16)))
        self.assertEqual(-1801086, float(a1p2.solveProblemTwo(-122)))
        self.assertEqual(1388260.096248, float(a1p2.solveProblemTwo(111.22)))
    
    

if __name__ == "__main__":
    unittest.main()