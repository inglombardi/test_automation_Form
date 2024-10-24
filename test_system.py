import unittest
from main import Contact
import support_functions as toolkit


"""
An automated test framework (e.g. Unittest) is a system that makes it easy to write 
executable tests and submit a set of tests for execution
 • As testing is automated, there is always a set of tests that can be quickly and easily executed
 – Whenever any functionality is added to the system, the tests can be run and 
    problems that the new  code has introduced can be caught immediately

To achieve this, unittest supports some important concepts:
 • testcase: Atest case is the smallest unit of testing. It checks for a specific response to a particular set
 of inputs. unittest provides a base class, TestCase, which may be used to create new test cases.
 • test fixture: A test fixture represents the preparation needed to perform one or more tests, and any
 associate cleanup actions. This may involve, for example, creating temporary or proxy databases,
 directories, or starting a server process.
 • testsuite: Atest suite aggregate tests that should be executed together. It is a collection of test cases,
 test suites, or both.
 • testrunner: Atest runner is a component which orchestrates the execution of tests and provides the
 outcome to the user. The runner may use a graphical interface, a textual interface, or return a
 special value to indicate the results of executing the tests.  
    
AssertTrue : assertRaises ensures that the expected exception is actually thrown

    
"""

class TestContactInsertion(unittest.TestCase):
    # __________________________________________
    #       Sample definitions
    # __________________________________________
    def setUp(self):
        """Set up test data"""

        # First Sample (valid)
        """ Sample for test_valid_contact_insertion just to check if the Module create the data structure  """
        # Self here -> This is the local context of the TestContactInsertion (GETTER AND SETTERN MISSING AND NOT NEEDED)
        self.valid_name = "Nicola"
        self.valid_surname = "Lombardi"
        self.valid_email = "nicola.lombardi@gmail.com"

        # Other Sample ( Emulating the customer )
        self.invalid_email_no_at = "nicolalombardi.com" # '.' forgotten
        self.invalid_name = "Nicola007" # name with digits
        self.invalid_surname = "Lombardi@#" # surname correct but email with '#'

        """ Sample for test_name_surname_length just to check if the Module checks for wrong lengths """
        self.long_name = "N" * 256 # > 255
        self.long_surname = "L" * 256


    def test_valid_contact_insertion(self):
        """Test valid insertion of contact"""
        # Creation of the CORRECT SAMPLE
        contact = Contact(name=self.valid_name, surname=self.valid_surname, email=self.valid_email)

        # Do the check with the CORRECT SAMPLE
        self.assertEqual(contact.name, self.valid_name)
        self.assertEqual(contact.surname, self.valid_surname)
        self.assertEqual(contact.email, self.valid_email)

    def test_name_surname_length(self):
        """Test that name and surname cannot exceed 255 characters"""
        with self.assertRaises(ValueError): # LONG NAME CASE
            Contact(name=self.long_name, surname=self.valid_surname, email=self.valid_email)

        with self.assertRaises(ValueError): # LONG SURNAME CASE
            Contact(name=self.valid_name, surname=self.long_surname, email=self.valid_email)

    def test_name_surname_no_digits_or_special_chars(self):
        """Test that name and surname cannot contain digits or special characters"""
        with self.assertRaises(ValueError): # DIGIT INTO NAME STRING
            Contact(name=self.invalid_name, surname=self.valid_surname, email=self.valid_email)

        with self.assertRaises(ValueError): # STRANGE CHAR INTO SURNAME STRING
            Contact(name=self.valid_name, surname=self.invalid_surname, email=self.valid_email)

    def test_valid_email(self):
        """Test that email has a correct domain (contains '@')"""
        contact = Contact(name=self.valid_name, surname=self.valid_surname, email=self.valid_email)
        self.assertTrue(contact.valid_email())

        # Test invalid email
        with self.assertRaises(ValueError):
            Contact(name=self.valid_name, surname=self.valid_surname, email=self.invalid_email_no_at)

    def test_email_name_surname_match(self):
        """Test that 'name.surname' matches the top part of the email before '@'"""
        contact = Contact(name=self.valid_name, surname=self.valid_surname, email=self.valid_email)
        self.assertTrue(contact.valid_name_surname())


if __name__ == '__main__':
    toolkit.printout()
    log_file = toolkit.generate_log()
    toolkit.initialize_log(log_file=log_file)
    #unittest.main()