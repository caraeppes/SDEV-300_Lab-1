"""
Cara Eppes
5/21/2024
SDEV 300
Lab 1

This is a program that allows the user to register to vote.
"""

import sys


class VoterRegistration:
    """Class for voter registration"""
    def __init__(self):
        """Initializes the voter registration"""
        self.first_name = None
        self.last_name = None
        self.age = None
        self.is_us_citizen = None
        self.state = None
        self.zipcode = None

    def register(self):
        """Function to register as a voter"""
        print("\nWelcome to the Voter Registration Application!")
        print("Enter 'exit registration' at any time to exit the application.\n")

        self.set_first_name()
        self.set_last_name()
        self.set_age()
        self.set_is_us_citizen()
        self.set_state()
        self.set_zipcode()
        self.registration_summary()

    def get_input(self, prompt):
        """Gets input from the user and checks if they have chosen to exit the registration"""
        user_input = input(prompt)
        if user_input.lower() == 'exit registration':
            self.exit_registration("")
        if user_input != '':
            return user_input
        # if response is blank, prompts user to try again
        print("Response cannot be blank.  Please try again.")
        return self.get_input(prompt)

    def exit_registration(self, message):
        """Prints a goodbye message and exits the application"""
        print(message + "Exiting registration.  Goodbye!")
        sys.exit()

    def set_first_name(self):
        """Sets first name from user input"""
        self.first_name = self.get_input("First name: ")
        self.validate_first_name()

    def set_last_name(self):
        """Sets last name from user input"""
        self.last_name = self.get_input("Last name: ")
        self.validate_last_name()

    def set_age(self):
        """Sets and validates age from user input"""
        age = self.get_input("Age: ")
        self.validate_age(age)

    def set_is_us_citizen(self):
        """Sets and validates US citizenship from user input"""
        self.is_us_citizen = self.get_input("U.S. citizen? (Y/N): ").upper()
        self.validate_is_us_citizen()

    def set_state(self):
        """Sets and validates state from user input"""
        self.state = self.get_input("State: ").upper()
        self.validate_state()

    def set_zipcode(self):
        """Sets and validates zipcode from user input"""
        self.zipcode = self.get_input("Zipcode: ")
        self.validate_zipcode_v2()

    def validate_first_name(self):
        """Validates first name only contains letters"""
        if not self.first_name.isalpha():
            print("Invalid first name.  Response can only contain letters.")
            self.set_first_name()

    def validate_last_name(self):
        """Validates last name only contains letters"""
        if not self.last_name.isalpha():
            print("Invalid last name.  Response can only contain letters.")
            self.set_last_name()

    def validate_age(self, age):
        """Validates provided age and exits program is user is less than 18 years old"""
        try:
            self.age = int(age)
        except ValueError:
            print("Invalid age.  Please enter a number.")
            self.set_age()
        if self.age < 0 or self.age > 120:
            print("Please enter an age from 0 to 120.")
            self.set_age()
        if self.age < 18:
            self.exit_registration("You must be at least 18 years old to register.  ")


    def validate_is_us_citizen(self):
        """Validates US citizenship response and exits program if user is not a citizen"""
        if self.is_us_citizen == 'N':
            self.exit_registration("You must be a U.S. citizen to register.  ")
        elif self.is_us_citizen != 'Y':
            print("Invalid response.  Please enter 'Y' or 'N'.")
            self.set_is_us_citizen()

    def validate_state(self):
        """Validates provided US state code"""
        state_codes = {'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FL', 'GA', 'HI', 'ID',
                       'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO',
                       'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA',
                       'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'}
        if self.state not in state_codes:
            print("Invalid response.  Please enter a valid U.S. state code.")
            self.set_state()

    def validate_zipcode(self):
        """Validate that provided zip code is a 5 or 9 digit number"""
        try:
            if len(self.zipcode) == 5 or len(self.zipcode) == 9:
                self.zipcode = int(self.zipcode)
            else:
                raise ValueError()
        except ValueError:
            print("Please enter a valid 5 or 9 digit U.S. zipcode.")
            self.set_zipcode()

    def validate_zipcode_v2(self):
        is_valid_zipcode = False
        while not is_valid_zipcode:
            if self.zipcode.isdigit() and (len(self.zipcode) == 5 or len(self.zipcode) == 9):
                is_valid_zipcode = True
            else:
                print("Please enter a valid 5 or 9 digit U.S. zipcode.")
                self.set_zipcode()


    def registration_summary(self):
        """Prints registration summary"""
        print("\nCongratulations! You have successfully completed your voter registration.\n")
        print("First Name:", self.first_name)
        print("Last Name:", self.last_name)
        print("Age:", self.age)
        print("U.S. Citizen:", self.is_us_citizen)
        print("State:", self.state)
        print("Zipcode:", self.zipcode)


def main():
    """Main function"""
    voter_registration = VoterRegistration()
    voter_registration.register()


main()
