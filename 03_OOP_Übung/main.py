from Person import (Person, Geschlecht)
from Mitarbeiter import Mitarbeiter
from Abteilungsleiter import Abteilungsleiter
from Abteilung import Abteilung, Abteilungsname
from Firma import Firma
import datetime

p1 = Person("Max", "Mustermann",
            datetime.date(2000, 12, 12), Geschlecht.männlich)


m1 = Mitarbeiter("Felix", "Haider",
                 datetime.date(2004, 1, 23), Geschlecht.divers, "MI_2312")

a1 = Abteilungsleiter("Patrick", "Klaric", datetime.date(2004, 11, 29),
                      Geschlecht.kampfhelikopter, "AV_6666", "W_201")

a2 = Abteilungsleiter("Arsch", "Arsch", datetime.date(2004, 11, 29),
                      Geschlecht.kampfhelikopter, "AV_6666", "W_201")
m2 = Mitarbeiter("Anderer Arsch", "Anderer Arsch",
                 datetime.date(2004, 1, 23), Geschlecht.divers, "MI_2312")

abteilung = Abteilung(Abteilungsname.wirtschaft)
abteilung.addMitarbeiter(m1)
abteilung.addMitarbeiter(m2)
abteilung.addAbteilungsvorstand(a1)
abteilung.addAbteilungsvorstand(a2)

print(abteilung)

firma = Firma()
firma.addAbteilung(abteilung)
print(firma)
