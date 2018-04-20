'''
Created on 20.04.2018

@author: kaiser
'''
import unittest
from utils import *
from functions import eliminate,only_choice

class Test(unittest.TestCase):


    def setUp(self):
        self.mSudokuStr = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
        self.sudoku = grid_values('..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..')

    def tearDown(self):
        pass


    def testOnlyChoice(self):
        sudoku1 = eliminate(self.sudoku)
        print("Eliminate Step:")
        print("")
        display(sudoku1)
        sudoku2 = only_choice(sudoku1)
        print("Only Choice Step:")
        print("")
        display(sudoku2)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()