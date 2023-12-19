from enum import Enum


class Abteilung:
    def __init__(self, abteilungsname):
        self.abteilungsname = abteilungsname
        self.mitarbeiter = []
        self.abteilungsvorstand = None

    def __str__(self):
        return (f"Abteilungsname: {self.abteilungsname} "
                f" Mitarbiter: {self.mitarbeiter}"
                f" Abteilungsvorstand: {self.abteilungsvorstand}")

    def addMitarbeiter(self, mitarbeiter):
        self.mitarbeiter.append(mitarbeiter)

    def addAbteilungsvorstand(self, abteilungsvorstand):
        if self.abteilungsvorstand is None:
            self.abteilungsvorstand = abteilungsvorstand


class Abteilungsname(Enum):
    wirtschaft = "Wirtschaft"
    maschinenbau = "Maschinenbau"
    elektronik = "Elektronik"
    elektrotechnik = "Elektrotechnik"
    biomedizin = "Biomedizin"
