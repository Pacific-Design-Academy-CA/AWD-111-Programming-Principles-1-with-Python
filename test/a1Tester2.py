#external module
from datetime import datetime
import math
from io import StringIO
from operator import imod
import sys
import unittest
import calendar
from unittest.mock import patch

#local module
import helloWorld

class TestOnePartTwo(unittest.TestCase):

    def testCheckHelloWorld(self):
        print("\nTest case for hellowWorld():\n Expected Output: Hello World\n")
        with patch('sys.stdout', new = StringIO()) as fake_out:
            helloWorld.helloWorld()
            self.assertEqual((fake_out.getvalue().strip()), 'Hello World')

    def testDisplayCurrentDateTime(self):
        print("\nTest case for disPlayCurrentDateTime():\n Sample Output: 2022-04-12 12:23:43\n")
        with patch('sys.stdout', new = StringIO()) as fake_out:
            helloWorld.displayCurrentDateTime()
            self.assertEqual((fake_out.getvalue().strip()), datetime.now().strftime("%Y-%m-%d %H:%M:%S") )
   
    def testPythonVersion(self):
        print("\nTest case for checkPythonVersion():\n Sample Output of your python version: 3.9.7\n")
        with patch('sys.stdout', new = StringIO()) as fake_out:
            helloWorld.checkPythonVersion()
            self.assertEqual((fake_out.getvalue().strip()), sys.version)

    def testPrintCalendar(self):
        print("\nTest case for printCalendar():\n Sample Output:\n"+calendar.month(2022,9))
        with patch('sys.stdout', new = StringIO()) as fake_out:
            helloWorld.printCalendar(2022,11)
            self.assertNotEqual((fake_out.getvalue().strip()), calendar.month(2022,11))


if __name__ == "__main__":
    unittest.main()