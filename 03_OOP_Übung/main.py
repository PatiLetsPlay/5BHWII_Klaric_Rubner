from Person import Person
from Mitarbeiter import Mitarbeiter
from Abteilungsleiter import Abteilungsleiter
from Abteilung import Abteilung, Abteilungsname
from Firma import Firma
from Geschlecht import Geschlecht
import datetime


def main():
    firma = Firma("HTL GmbH")
    abteilung1 = Abteilung(Abteilungsname.wirtschaft)
    abteilung2 = Abteilung(Abteilungsname.biomedizin)

    p1 = Person("Max", "Mustermann", datetime.date(2000, 12, 12), Geschlecht.männlich)

    ma1 = Mitarbeiter("Felix", "Haider", datetime.date(2004, 1, 23), Geschlecht.männlich, "MI_2312")
    ma2 = Mitarbeiter("Bernd", "Brot", datetime.date(2000, 1, 30), Geschlecht.weiblich, "MI_9426")
    ma3 = Mitarbeiter("Sebastian", "Winter", datetime.date(2001, 5, 6), Geschlecht.divers, "MI_4521")
    ma4 = Mitarbeiter("Jon", "Dough",
                      datetime.date(205, 8, 15), Geschlecht.kampfhelikopter, "MI_3625")
    ma5 = Mitarbeiter("Jon", "Snow", datetime.date(1988, 2, 4), Geschlecht.not_specified, "MI_0214")


    a1 = Abteilungsleiter("Patrick", "Klaric", datetime.date(2004, 11, 29),
                          Geschlecht.männlich, "AV_6666", "W_201")

    a2 = Abteilungsleiter("Walter", "Frosch", datetime.date(1999, 5, 5),
                          Geschlecht.kampfhelikopter, "AV_5458", "B_152")

    abteilung1.addMitarbeiter(ma1)
    abteilung1.addMitarbeiter(ma2)
    abteilung1.addAbteilungsvorstand(a1)
    abteilung1.addAbteilungsvorstand(a2)

    abteilung2.addMitarbeiter(ma3)
    abteilung2.addMitarbeiter(ma4)
    abteilung2.addMitarbeiter(ma5)
    abteilung2.addAbteilungsvorstand(a2)

    firma.add_abteilung(abteilung1)
    firma.add_abteilung(abteilung2)

    print("Anzahl Abteilungsvorstände in Abteilung 1: " + str(abteilung1.anzahl_abteilungsvorstände()))
    print("Anzahl Mitarbeiter in Abteilung 1: " + str(abteilung1.anzahl_mitarbeiter()))

    print("Anzahl Abteilungsvorstände in Abteilung 2: " + str(abteilung2.anzahl_abteilungsvorstände()))
    print("Anzahl Mitarbeiter in Abteilung 2: " + str(abteilung2.anzahl_mitarbeiter()))

    print("Anzahl Abteilungen: " + str(firma.count_abteilungen()))
    print("Anzahl Abteilungsvorstände: " + str(firma.count_abteilungsvorstände()))
    print("Anzahl Mitarbeiter: " + str(firma.count_mitarbeiter()))
    print("Anzahl Mitarbeiter in der größten Abteilung: " + str(firma.mitarbeiterstärkste_Abteilung()))
    print("Geschlechterverteilung: " + str(firma.geschlechterverteilung()))


if __name__ == "__main__":
    main()
