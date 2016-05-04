# Create a test module for your case change program
#     import your case change program
# create a test case class
#     write a test for your snake case to camel case functions
#     run the test via PyCharms testing run config
#
# * test your other transformations in the case change
# * test one of the tic tac toe board classes
# *duplicate those tests for the other board classes
#~~~~~~~~~~~~~~~~

import unittest
import encapsulation


class TestEncapsulation(unittest.TestCase):

    def test_list_board_place(self):
        board1 = encapsulation.ListListTTTBoard()
        board1.place(0, 2, 'F')
        assert board1.rows[2][0] == 'F'

TestCaseConversion.test_list_board_place(unittest.TestCase)









import case_conversion

class TestCaseConversion(unittest.TestCase):

    def test_word_to_title(self):
        word = 'this is my word'
        expected = 'This Is My Word'
        assert case_conversion.word_to_title(word) == expected

TestCaseConversion.test_word_to_title(unittest.TestCase)



















    #
