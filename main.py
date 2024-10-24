"""
Suppose you have the Backend of a web form and you must check the insert operation of following attributes:
    - name and surname
    - email
A - You must develop a Python module to test the correct insert Operation, for example, considering these test cases:
    1. Name and Surname cannot exceed 255 length and contain digit or strange characters
    2. The email should have a correct domain, then "@" is needed
    3. A function that check if "self._name + '.' + self._surname" is equal to top part of the email before "@"

Writing tests before code clarifies the requirements to be implemented.

You must develop a Unittest module to test the system and threat exception.


==============================
DOCUMENTATION ABOUT BUILTINS
==============================

The isalpha() method returns True if all the characters are alphabet letters (a-z).
"Company10".isalpha() ==> FALSE
"Company".isalpha() ==> TRUE
"Company#".isalpha() ==> FALSE


"""

import support_functions as toolkit
class Contact():
    def __init__(self, name: str, surname: str, email: str):
        # --- mandatory (The real tested part)
        self._name = name
        self._surname = surname
        self._email = email
        # --- optional
        self.valid = False

        if len(self._name) > 255 or not self._name.isalpha():
            raise ValueError("Name cannot exceed 255 characters and must contain only letters")

        if len(self._surname) > 255 or not self._surname.isalpha():
            raise ValueError("Surname cannot exceed 255 characters and must contain only letters")

        self.valid_email()


    # ---- Name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name):
        self._name = new_name

    # ---- Surname
    @property
    def surname(self):
        return self._surname
    @surname.setter
    def name(self, new_surname):
        self._surname = new_surname

    # ---- Email
    @property
    def email(self):
        return self._email

    # =================================
    #       Unittest support functions
    # =================================
    def valid_email(self):
        """ This method has been called by test_valid_email
        This method should call valid_name_surname and valid_domain subroutines
        :return: True or False
        """
        if self.valid_name_surname() == self.valid_domain(): # if True == True
            self.valid = True
            return True
        else:
            return False

    def valid_name_surname(self):
        """ This method has been called by test_email_name_surname_match
        for example:
            "nicola.lombardi@telit.com".split("@")
            ['nicola.lombardi', 'telit.com']
        :return: T or F
        """
        local_part = self._email.split('@')[0]
        expected_part = f"{self._name.lower()}.{self._surname.lower()}"
        if local_part != expected_part:
            raise ValueError("The name and surname do not match the email's local part")
        return True


    def valid_domain(self):
        email = self.email # getter
        domain = email.split('@')
        length = len(domain)
        if length <= 1:
            raise ValueError(f"The domain {domain} cannot have L={length}")
        return True



def print_hi(obj):
    """ A function that used an external module
    :param obj: whatever
    :return: None
    """
    print(f'Hi, {obj}')
    toolkit.display_obj(obj_attr_dict=obj.__dict__)


if __name__ == '__main__':
    c1 = Contact(name='Nicola', surname='Cognome', email='nicola00915@gmail.com')
    print_hi(obj=c1)

