from enum import Enum


class Abteilung:
    def __init__(self, abteilungsname):
        self.abteilungsname = abteilungsname
        self.mitarbeiter = []
        self.abteilungsvorstand = None

    def __str__(self):
        mitarbeiter_str = ", ".join(str(mitarbeiter) for mitarbeiter in self.mitarbeiter)

        return (f"Abteilungsname: {self.abteilungsname} "
                f" Mitarbiter: {mitarbeiter_str}"
                f" Abteilungsvorstand: {self.abteilungsvorstand}")

    def addMitarbeiter(self, mitarbeiter):
        self.mitarbeiter.append(mitarbeiter)

    def addAbteilungsvorstand(self, abteilungsvorstand):
        if self.abteilungsvorstand is None:
            self.abteilungsvorstand = abteilungsvorstand
            self.addMitarbeiter(abteilungsvorstand)
        else:
            print("Schon ein Abteilungsvorstand vorhanden")

    def anzahl_mitarbeiter(self):
        return len(self.mitarbeiter)

    def anzahl_abteilungsvorstände(self):
        if self.abteilungsvorstand is not None:
            return 1
        else:
            return 0


class Abteilungsname(Enum):
    wirtschaft = "Wirtschaft"
    maschinenbau = "Maschinenbau"
    elektronik = "Elektronik"
    elektrotechnik = "Elektrotechnik"
    biomedizin = "Biomedizin"
