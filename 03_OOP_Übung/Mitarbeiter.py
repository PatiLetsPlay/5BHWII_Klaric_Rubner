from Person import Person


class Mitarbeiter(Person):
    def __init__(self, firstname, lastname, birthdate, geschlecht, erkennungscode):
        super().__init__(firstname, lastname, birthdate, geschlecht)
        self.erkennungscode = erkennungscode

    def __str__(self):
        return (f"\n{super().__str__()}"
                f"\nMitarbeitercode: {self.erkennungscode}")



