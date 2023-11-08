import random
import random as rand

wie_viel = 5
anzahl_ziehungen = 1000000

counter = {
    "counter_highcard": 0,
    "counter_paar": 0,
    "counter2_paar": 0,
    "counter_drilling": 0,
    "counter_straight": 0,
    "counter_flush": 0,
    "counter_full_house": 0,
    "counter_vierling": 0,
    "counter_straight_flush": 0,
    "counter_royale_flush": 0
}


def karten_ziehen(wie_viele):
    alle_gezogenen = []
    alle = list(range(0, 52))
    gezogen = random.sample(alle, wie_viele)
    for soll in gezogen:
        farbe = soll // 13
        zahl = soll % 13

        # print("Farbe: " + str(farbe) + " Zahl: " + str(zahl))
        alle_gezogenen.append((farbe, zahl))

    # print(str(alle_gezogenen) + "\n")

    # print(str(alle_gezogenen) + "\n")

    check_hand(alle_gezogenen)
    return


def check_hand(alle_gezogen):
    if royale_flush(alle_gezogen):
        pass
    elif straight_flush(alle_gezogen):
        pass
    elif fullhouse_vierling(alle_gezogen):
        pass
    elif flush(alle_gezogen):
        pass
    elif straight(alle_gezogen):
        pass
    elif paar_2paar_drilling(alle_gezogen):
        pass
    else:
        counter["counter_highcard"] = counter.get("counter_highcard", 0) + 1


def paar_2paar_drilling(alle_gezogen):
    # liste die 13 Felder hat die alle mit 0 belegt werden
    wie_oft_zahl_gezogen = [0 for _ in range(0, 13)]

    # alleGezogen wird durchgegangen und an der Stelle der gezogenene Zahl um 1 erhöht
    # gezogene Zahl 3 am Index 3 um 1 erhöhen
    for gezogen in alle_gezogen:
        wie_oft_zahl_gezogen[gezogen[1]] += 1
    wie_oft_zahl_gezogen.sort(reverse=True)

    # Drilling
    if 3 in wie_oft_zahl_gezogen:
        counter["counter_drilling"] = counter.get("counter_drilling", 0) + 1
        return True

    # Zwei Paar
    elif wie_oft_zahl_gezogen[0] == 2 and wie_oft_zahl_gezogen[1] == 2:
        counter["counter2_paar"] = counter.get("counter2_paar", 0) + 1
        return True

    # Paar
    elif 2 in wie_oft_zahl_gezogen:
        counter["counter_paar"] += 1
        return True

    return False


def straight(alle_gezogen):
    wie_oft_zahl_gezogen = [0 for _ in range(0, 13)]

    for gezogen in alle_gezogen:
        wie_oft_zahl_gezogen[gezogen[1]] += 1

    # look for straight
    for i in range(9):
        if wie_oft_zahl_gezogen[0 + i] == 1 \
                and wie_oft_zahl_gezogen[1 + i] == 1 \
                and wie_oft_zahl_gezogen[2 + i] == 1 \
                and wie_oft_zahl_gezogen[3 + i] == 1 \
                and wie_oft_zahl_gezogen[(i + 4) % 13] == 1:
            counter["counter_straight"] += 1
            return True

    return False


def flush(alle_gezogen):
    # liste die 4 Felder hat die alle mit 0 belegt werden
    wie_oft_farbe_gezogen = [0 for _ in range(0, 4)]
    # alleGezogen wird durchgegangen und an der Stelle der gezogenene Farbe um 1 erhöht
    # gezogene Farbe 3 am Index 3 um 1 erhöhen
    for gezogen in alle_gezogen:
        wie_oft_farbe_gezogen[gezogen[0]] += 1

    wie_oft_farbe_gezogen.sort(reverse=True)
    if wie_oft_farbe_gezogen[0] == 5:
        counter["counter_flush"] = counter.get("counter_flush", 0) + 1
        return True

    return False


def fullhouse_vierling(alle_gezogen):
    # liste die 13 Felder hat die alle mit 0 belegt werden
    wie_oft_zahl_gezogen = [0 for _ in range(0, 13)]

    # alleGezogen wird durchgegangen und an der Stelle der gezogenene Zahl um 1 erhöht
    # gezogene Zahl 3 am Index 3 um 1 erhöhen
    for gezogen in alle_gezogen:
        wie_oft_zahl_gezogen[gezogen[1]] += 1
    wie_oft_zahl_gezogen.sort(reverse=True)

    # Vierling
    if 4 in wie_oft_zahl_gezogen:
        counter["counter_vierling"] = counter.get("counter_vierling", 0) + 1
        return True

    # Full-house
    elif wie_oft_zahl_gezogen[0] == 3 and wie_oft_zahl_gezogen[1] == 2:
        counter["counter_full_house"] = counter.get("counter_full_house", 0) + 1
        return True

    return False


def straight_flush(alle_gezogen):
    wie_oft_zahl_gezogen = [0 for _ in range(0, 13)]
    wie_oft_farbe_gezogen = [0 for _ in range(0, 4)]

    for gezogen in alle_gezogen:
        wie_oft_zahl_gezogen[gezogen[1]] += 1
        wie_oft_farbe_gezogen[gezogen[0]] += 1

    wie_oft_farbe_gezogen.sort(reverse=True)

    # look for straight flush
    for i in range(9):
        if (wie_oft_zahl_gezogen[i] == 1
            and wie_oft_zahl_gezogen[1 + i] == 1
            and wie_oft_zahl_gezogen[2 + i] == 1
            and wie_oft_zahl_gezogen[3 + i] == 1
            and wie_oft_zahl_gezogen[(i + 4) % 13] == 1) \
                and wie_oft_farbe_gezogen[0] == 5:
            counter["counter_straight_flush"] += 1
            return True
    return False


def royale_flush(alle_gezogen):
    wie_oft_zahl_gezogen = [0 for _ in range(0, 13)]
    wie_oft_farbe_gezogen = [0 for _ in range(0, 4)]

    for gezogen in alle_gezogen:
        wie_oft_zahl_gezogen[gezogen[1]] += 1
        wie_oft_farbe_gezogen[gezogen[0]] += 1

    wie_oft_farbe_gezogen.sort(reverse=True)

    if (wie_oft_zahl_gezogen[0]
        and wie_oft_zahl_gezogen[9]
        and wie_oft_zahl_gezogen[10]
        and wie_oft_zahl_gezogen[11]
        and wie_oft_zahl_gezogen[12]) \
            and \
            (wie_oft_farbe_gezogen[0] == 5
             or wie_oft_farbe_gezogen[1] == 5
             or wie_oft_farbe_gezogen[2] == 5
             or wie_oft_farbe_gezogen[3] == 5):
        counter["counter_royale_flush"] = counter.get("counter_royale_flush", 0) + 1
        counter["counter_straight_flush"] = counter.get("counter_straight_flush", 0) + 1
        return True

    return False


for i in range(anzahl_ziehungen):
    karten_ziehen(wie_viel)

for k, v in counter.items():
    prozent_v = (v / anzahl_ziehungen) * 100
    print(str(k), str(prozent_v) + "%")
