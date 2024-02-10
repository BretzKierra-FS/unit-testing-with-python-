import unittest
import logging
from unittest.mock import patch
from grader import Grader
import grader_mock


# Logger to output test pass and fails
logging.basicConfig(filename='testlog.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

gr = Grader()

class Test(unittest.TestCase):

        # # Unit test sample from lecture # #
    # def test_gradeInfo_sample(self):
    #   self.assertEqual(gr.gradeInfo(), "You did not entered a grade number between 0 and 100.")
     
# Test for Statement Coverage
# Each statment is executed at least once
    def test_gradeInfo_invalid_input(self):
        with patch('builtins.input', side_effect=["John", "Homework", "abc"]):
            result = gr.gradeInfo()
            self.assertEqual(result, "You did not enter a grade number between 0 and 100.")
            if result == "You did not enter a grade number between 0 and 100.":
                logging.info("test_gradeInfo_invalid_input passed")
            else:
                logging.error("test_gradeInfo_invalid_input failed")

# Test for function coverage
#Checks if returned a str
    def test_gradeInfo_function(self):
        with patch('builtins.input', side_effect=["John", "Homework", "75"]):
            result = gr.gradeInfo()
            self.assertIsInstance(result, str)
            if isinstance(result, str):
                logging.info("test_gradeInfo_function passed")
            else:
                logging.error("test_gradeInfo_function failed")

# Test for conditional coverage
    def test_gradeInfo_conditional(self):
        with patch('builtins.input', side_effect=["John", "Homework", "65"]):
            expected_output = "Hello John\nYour letter grade for Homework assignment is as follows: D\nAssignment details:\nYou have met some of the assignment's requirements."
            result = gr.gradeInfo()
            self.assertEqual(result, expected_output)
            if result == expected_output:
                logging.info("test_gradeInfo_conditional passed")
            else:
                logging.error("test_gradeInfo_conditional failed")
                
 # Test for Branch Coverage
#Each point is executed with both true and false conditions
      ########      
    #   Note to Professor, my first take was to write a test for each grade type A, B, C.. but that was redondant...
    #   So, I looked up how to use mock data with unittest instead
    def test_gradeInfo_mock(self):
        for i, (input_values, expected_output) in enumerate(grader_mock.test_cases):
            with patch('builtins.input', side_effect=input_values):
                result = gr.gradeInfo()
                self.assertEqual(result, expected_output)
                if result == expected_output:
                    logging.info(f"test_gradeInfo_mock {i+1} passed")
                else:
                    logging.error(f"test_gradeInfo_mock {i+1} failed")
