class Person:
    def __init__(self, firstname, lastname, birthdate, geschlecht):
        self.firstname = firstname
        self.lastname = lastname
        self.birthdate = birthdate
        self.geschlecht = geschlecht

    def __str__(self):
        return f"Firstname: {self.firstname} " \
               f"Lastname: {self.lastname} "\
               f"\nBirthdate: {self.birthdate} "\
               f"Geschlecht: {self.geschlecht.value}"

    def print_name(self):
        print("Hello my name is " + self.firstname + " " + self.lastname)



