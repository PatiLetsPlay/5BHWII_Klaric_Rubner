class Firma:
    def __init__(self):
        self.abteilungen = []

    def __str__(self):
        return f"Abteilungen: {self.abteilungen} "

    def addAbteilung(self, abteilung):
        self.abteilungen.append(abteilung)