from Geschlecht import Geschlecht
class Firma:
    def __init__(self, companyname):
        self.companyname = companyname
        self.abteilungen = []

    def __str__(self):
        abteilungen_str = ", ".join(str(abteilungen) for abteilungen in self.abteilungen)
        return (f"Firma: {self.companyname} "
                f" Abteilungen: {abteilungen_str}")

    def add_abteilung(self, abteilung):
        self.abteilungen.append(abteilung)

    def count_mitarbeiter(self):
        counter = 0
        for i in self.abteilungen:
            counter += len(i.mitarbeiter)
        return counter

    def count_abteilungsvorstände(self):
        counter = 0
        for i in self.abteilungen:
            if i.abteilungsvorstand is not None:
                counter += 1
        return counter

    def count_abteilungen(self):
        return len(self.abteilungen)

    def mitarbeiterstärkste_Abteilung(self):
        größte = 0
        # name = ""
        for i in self.abteilungen:
            if len(i.mitarbeiter) > größte:
                größte = len(i.mitarbeiter)
                # name = i.abteilungsname.value
        return größte

    def geschlechterverteilung(self):
        geschlechter = []
        for i in self.abteilungen:
            for j in i.mitarbeiter:
                geschlechter.append(j.geschlecht)
        männlich = list(filter(lambda geschlecht: geschlecht == Geschlecht.männlich, geschlechter))
        weiblich = list(filter(lambda geschlecht: geschlecht == Geschlecht.weiblich, geschlechter))
        kampfhelikopter = list(filter(lambda geschlecht: geschlecht == Geschlecht.kampfhelikopter, geschlechter))
        divers = list(filter(lambda geschlecht: geschlecht == Geschlecht.divers, geschlechter))
        not_specified = list(filter(lambda geschlecht: geschlecht == Geschlecht.not_specified, geschlechter))

        geschlechterliste = {"männlich": len(männlich)/len(geschlechter) * 100,
                             "weiblich": len(weiblich)/len(geschlechter) * 100,
                             "kampfhelikopter": len(kampfhelikopter)/len(geschlechter) * 100,
                             "divers": len(divers)/len(geschlechter) * 100,
                             "not_specified": len(not_specified)/len(geschlechter) * 100}
        return geschlechterliste
