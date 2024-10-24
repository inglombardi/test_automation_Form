import datetime
import os
import json
import re
import socket
from binascii import hexlify

def display_obj(obj_attr_dict: dict):
    """
    :param obj_attr_dict: obj.__dict__
    :return: None
    """
    for key, val in obj_attr_dict.items():
        print(f"{key} : {val}")

def display_status_msg(string):
  print("**********************************************************************************************************************************************************************************")
  print(f"\t\t\t\t\t\t\t*****{string}*****")
  print("**********************************************************************************************************************************************************************************")


def printout(keyword = 'CONTACT INSERTION'):
    """ Printout of every single test
    @return: None
    """
    import datetime
    name_match = "Contact Insertion Errors: Management"
    display_status_msg(" TEST HEADER ")
    author = os.getenv('AUTHOR', '\nNicola Lombardi HW Engineer <nicola.lombardi@telit.it> Oscilloscope - owner ')
    current_date = datetime.datetime.now().strftime("%a %b %d %H:%M:%S %Y")
    print(f"\t\tAuthor(s): {author}")
    print(f"\t\tDate: {current_date}")
    print(f"\t\tTestPlan test: {name_match}")
    #current_file_py = os.path.basename(__file__).split('.')[0]
    #print("\t\tTest Name:", current_file_py)
    display_status_msg(" END TEST HEADER ")

def generate_log():
    """ Generate a log for each attempt to do a stability """
    start_time = datetime.datetime.now()
    filename = f"Test_{start_time.strftime('%Y%m%d_%H%M%S')}.txt"
    return filename

def initialize_log(log_file):
    """ This functions just writes the header on the log file """
    #log_file = 'test_log.txt'
    #if not os.path.exists(log_file):
    with open(log_file, 'w') as file:
            file.write(
                "--------------------------------------------------------------------------------------------------------------------------------------------------------------\n"
                "@Main Author of this test: Nicola Lombardi - HW Baseband - Telit Cinterion: Oscilloscope main author, Other Source Meter functionalities\n"
                "--------------------------------------------------------------------------------------------------------------------------------------------------------------\n"
                "@TestPlan: No Test Plan\n"
                "@TestName: Simple test\n"
                "@TestCase: Dummy version \n"
                "@Purpose: Development of a Software emulating a Contact Insertion in a Back Storage System\n"
                "@DateCreated: 29-05-2024\n"
                "@Patterns: Strategy, Single Responsibility Principle, State\n"
                "--------------------------------------------------------------------------------------------------------------------------------------------------------------\n"
            )

def create_and_write_log():
    f = generate_log()
    initialize_log(log_file=f)


if __name__ == '__main__':
    create_and_write_log()
    # Note that this function has not been used to avoid a useless filling of
    # test_... methods in "test_system.py"