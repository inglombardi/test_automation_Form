Suppose you have the Backend of a web form and you must check the insert operation of following attributes:
    - name and surname
    - email
A - You must develop a Python module to test the correct insert Operation, for example, considering these test cases:
    1. Name and Surname cannot exceed 255 length and contain digit or strange characters
    2. The email should have a correct domain, then "@" is needed
    3. A function that check if "self._name + '.' + self._surname" is equal to top part of the email before "@"

Writing tests before code clarifies the requirements to be implemented.

You must develop a Unittest module to test the system and threat exception.
