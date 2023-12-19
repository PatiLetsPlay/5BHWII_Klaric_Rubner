from Mitarbeiter import Mitarbeiter


class Abteilungsleiter(Mitarbeiter):
    def __init__(self, firstname, lastname, birthdate, geschlecht, erkennungscode, raumnummer):
        super().__init__(firstname, lastname, birthdate, geschlecht, erkennungscode)
        self.raumnummer = raumnummer

    def __str__(self):
        return (f"{super().__str__()}"
                f" Raumnummer: {self.raumnummer}")
