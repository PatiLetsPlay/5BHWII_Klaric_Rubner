import random
import random as rand
import sys


def karten_ziehen(wie_viele, counter):
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

    check_hand(alle_gezogenen, counter)
    return


def check_hand(alle_gezogen, counter):
    if royale_flush(alle_gezogen):
        counter["counter_royale_flush"] = counter.get("counter_royale_flush", 0) + 1
        counter["counter_straight_flush"] = counter.get("counter_straight_flush", 0) + 1
        pass
    elif straight_flush(alle_gezogen):
        counter["counter_straight_flush"] += 1
        pass
    elif vierling(alle_gezogen):
        counter["counter_vierling"] = counter.get("counter_vierling", 0) + 1
        pass
    elif fullhouse(alle_gezogen):
        counter["counter_full_house"] = counter.get("counter_full_house", 0) + 1
        pass
    elif flush(alle_gezogen):
        counter["counter_flush"] = counter.get("counter_flush", 0) + 1
        pass
    elif straight(alle_gezogen):
        counter["counter_straight"] += 1
        pass
    elif drilling(alle_gezogen):
        counter["counter_drilling"] = counter.get("counter_drilling", 0) + 1
        pass
    elif zweipaar(alle_gezogen):
        counter["counter2_paar"] = counter.get("counter2_paar", 0) + 1
        pass
    elif paar(alle_gezogen):
        counter["counter_paar"] = counter.get("counter_paar", 0) + 1
        pass
    else:
        counter["counter_highcard"] = counter.get("counter_highcard", 0) + 1


def paar(alle_gezogen):
    wie_oft_zahl_gezogen = [0 for _ in range(0, 13)]

    # alleGezogen wird durchgegangen und an der Stelle der gezogenene Zahl um 1 erhöht
    # gezogene Zahl 3 am Index 3 um 1 erhöhen
    for gezogen in alle_gezogen:
        wie_oft_zahl_gezogen[gezogen[1]] += 1
    wie_oft_zahl_gezogen.sort(reverse=True)

    # Paar
    if 2 in wie_oft_zahl_gezogen:
        return True
    return False


def zweipaar(alle_gezogen):
    wie_oft_zahl_gezogen = [0 for _ in range(0, 13)]

    # alleGezogen wird durchgegangen und an der Stelle der gezogenene Zahl um 1 erhöht
    # gezogene Zahl 3 am Index 3 um 1 erhöhen
    for gezogen in alle_gezogen:
        wie_oft_zahl_gezogen[gezogen[1]] += 1
    wie_oft_zahl_gezogen.sort(reverse=True)

    # Zwei Paar
    if wie_oft_zahl_gezogen[0] == 2 and wie_oft_zahl_gezogen[1] == 2:
        return True
    return False


def drilling(alle_gezogen):
    # liste die 13 Felder hat die alle mit 0 belegt werden
    wie_oft_zahl_gezogen = [0 for _ in range(0, 13)]

    # alleGezogen wird durchgegangen und an der Stelle der gezogenene Zahl um 1 erhöht
    # gezogene Zahl 3 am Index 3 um 1 erhöhen
    for gezogen in alle_gezogen:
        wie_oft_zahl_gezogen[gezogen[1]] += 1
    wie_oft_zahl_gezogen.sort(reverse=True)

    # Drilling
    if 3 in wie_oft_zahl_gezogen:
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
        return True

    return False


def fullhouse(alle_gezogen):
    # liste die 13 Felder hat die alle mit 0 belegt werden
    wie_oft_zahl_gezogen = [0 for _ in range(0, 13)]

    # alleGezogen wird durchgegangen und an der Stelle der gezogenene Zahl um 1 erhöht
    # gezogene Zahl 3 am Index 3 um 1 erhöhen
    for gezogen in alle_gezogen:
        wie_oft_zahl_gezogen[gezogen[1]] += 1
    wie_oft_zahl_gezogen.sort(reverse=True)

    # Full-house
    if wie_oft_zahl_gezogen[0] == 3 and wie_oft_zahl_gezogen[1] == 2:
        return True

    return False


def vierling(alle_gezogen):
    wie_oft_zahl_gezogen = [0 for _ in range(0, 13)]

    # alleGezogen wird durchgegangen und an der Stelle der gezogenene Zahl um 1 erhöht
    # gezogene Zahl 3 am Index 3 um 1 erhöhen
    for gezogen in alle_gezogen:
        wie_oft_zahl_gezogen[gezogen[1]] += 1
    wie_oft_zahl_gezogen.sort(reverse=True)

    # Vierling
    if 4 in wie_oft_zahl_gezogen:
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
        return True

    return False


def main():
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

    wie_viel = 5
    anzahl_ziehungen = int(sys.argv[1])

    for i in range(anzahl_ziehungen):
        karten_ziehen(wie_viel, counter)

    for k, v in counter.items():
        prozent_v = (v / anzahl_ziehungen) * 100
        print(str(k), str(prozent_v) + "%")


if __name__ == "__main__":
    main()
