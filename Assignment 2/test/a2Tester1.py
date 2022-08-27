#external module

from io import StringIO
import unittest
from unittest.mock import patch

#local module
import a2p1

class TestTwoPartOne(unittest.TestCase):

    def testCheckLegalVotingAge(self):
        print("\nTest case for checkLegalVotingAge(age):\n\n case 1: 19\n case 2: 14\n")
        with patch('sys.stdout', new = StringIO()) as fake_out:
            a2p1.checkLegalVotingAge(19)
            self.assertEqual((fake_out.getvalue().strip()), 'True')
        with patch('sys.stdout', new = StringIO()) as fake_out:
            a2p1.checkLegalVotingAge(14)
            self.assertEqual((fake_out.getvalue().strip()), 'False')

    def testCheckIfNumberEvenOrOdd(self):
        print("\nTest case for checkIfNumberEvenOrOdd(number):\n\n case 1: 222\n case 2: -123\n case 3: 45\n")
        with patch('sys.stdout', new = StringIO()) as fake_out:
            a2p1.checkIfNumberEvenOrOdd(222)
            self.assertEqual((fake_out.getvalue().strip()), "Even" )
        with patch('sys.stdout', new = StringIO()) as fake_out:
            a2p1.checkIfNumberEvenOrOdd(-123)
            self.assertEqual((fake_out.getvalue().strip()), "Odd" )
        with patch('sys.stdout', new = StringIO()) as fake_out:
            a2p1.checkIfNumberEvenOrOdd(45)
            self.assertEqual((fake_out.getvalue().strip()), "Odd" )

    def testCheckIfDivisible(self):
        print("\nTest case for checkIfDivisible(numOne, numTwo, numThree):\n\n case 1:: 5;4;20\n case 2: 11;13;143\n case 3: -9;8;33\n")
        with patch('sys.stdout', new = StringIO()) as fake_out:
            a2p1.checkIfDivisible(5,4,20)
            self.assertEqual((fake_out.getvalue().strip()), "True")
        with patch('sys.stdout', new = StringIO()) as fake_out:
            a2p1.checkIfDivisible(11,13,143)
            self.assertEqual((fake_out.getvalue().strip()), "True")
        with patch('sys.stdout', new = StringIO()) as fake_out:
            a2p1.checkIfDivisible(-9,8,33)
            self.assertEqual((fake_out.getvalue().strip()), "False")

    def testGradeCalculator(self):
        print("\nTest case for gradeCalculator(score):\n\n case 1: 0.6\n case 2: 0.92\n case 3: .76\n")
        with patch('sys.stdout', new = StringIO()) as fake_out:
            a2p1.gradeCalculator(0.6)
            self.assertEqual((fake_out.getvalue().strip()), "D")
        with patch('sys.stdout', new = StringIO()) as fake_out:
            a2p1.gradeCalculator(0.92)
            self.assertEqual((fake_out.getvalue().strip()), "A")
        with patch('sys.stdout', new = StringIO()) as fake_out:
            a2p1.gradeCalculator(0.76)
            self.assertEqual((fake_out.getvalue().strip()), "C")

    def testCheckLeapYear(self):
        print("\nTest case for checkLeapYear(year):\n\n case 1: 2004\n case 2: 2012\n case 3: 1223\n case 4: 1982\n")
        with patch('sys.stdout', new = StringIO()) as fake_out:
            a2p1.checkLeapYear(2004)
            self.assertEqual((fake_out.getvalue().strip()), "Leap Year")
        with patch('sys.stdout', new = StringIO()) as fake_out:
            a2p1.checkLeapYear(2012)
            self.assertEqual((fake_out.getvalue().strip()), "Leap Year")
        with patch('sys.stdout', new = StringIO()) as fake_out:
            a2p1.checkLeapYear(1223)
            self.assertEqual((fake_out.getvalue().strip()), "Common Year")
        with patch('sys.stdout', new = StringIO()) as fake_out:
            a2p1.checkLeapYear(1982)
            self.assertEqual((fake_out.getvalue().strip()), "Common Year")

    def testCheckSubStringInString(self):
        print("\nTest case for checkSubStringInString(string, subString):\n\n case 1: manchester;chest\n case 2: pomodoro;tomato\n case 3: jamesbond;bon\n")
        with patch('sys.stdout', new = StringIO()) as fake_out:
            a2p1.checkSubString("manchester","chest")
            self.assertEqual((fake_out.getvalue().strip()), "Present")
        with patch('sys.stdout', new = StringIO()) as fake_out:
            a2p1.checkSubString("pomodoro","tomato")
            self.assertEqual((fake_out.getvalue().strip()), "Absent")
        with patch('sys.stdout', new = StringIO()) as fake_out:
            a2p1.checkSubString("jamesbond","bon")
            self.assertEqual((fake_out.getvalue().strip()), "Present")


    def testStringManipulationOne(self):
        print("\nTest case for checkStringManipulationOne(string):\n\n case 1: LebronJames\n case 2: JustinTrudeau\n")
        with patch('sys.stdout', new = StringIO()) as fake_out:
            a2p1.stringManipulationOne("LebronJames")
            self.assertEqual((fake_out.getvalue().strip()), "Lees")
        with patch('sys.stdout', new = StringIO()) as fake_out:
            a2p1.stringManipulationOne("JustinTrudeau")
            self.assertEqual((fake_out.getvalue().strip()), "Juau")   
    
    


    
if __name__ == "__main__":
    unittest.main()