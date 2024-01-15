import random


def main():
    print("Iher Eingabe[Stein(1), Papier(2), Schere(3), Echse(4), Spock(5)]: ")
    userinput = input()

    botinput = random.randint(1, 5)
    print(botinput)

    if (userinput.isdigit()) and (userinput >= list(items.keys())[0] or userinput <= list(items.keys())[-1]):
        checkIfWon(userinput, botinput)
        weiterSpielen()
    else:
        print("Iher Eingabe war falsch!")
        weiterSpielen()


def checkIfWon(userinput, botinput):
    # Stein
    if (userinput == 1 and botinput == 3) or (userinput == 1 and botinput == 4):
        print("You won")
    elif (userinput == 1 and botinput == 3) or (userinput == 1 and botinput == 4):
        print("You lost")
    else:
        print("Unentschieden")

    # Papier
    if (userinput == 2 and botinput == 1) or (userinput == 2 and botinput == 5):
        print("You won")
    elif (userinput == 2 and botinput) == 3 or (userinput == 2 and botinput == 4):
        print("You lost")
    else:
        print("Unentschieden")

    # Schere
    if (userinput == 3 and botinput == 2) or (userinput == 3 and botinput == 4):
        print("You won")
    elif (userinput == 3 and botinput == 1) or (userinput == 3 and botinput == 5):
        print("You lost")
    else:
        print("Unentschieden")

    # Echse
    if (userinput == 4 and botinput == 2) or (userinput == 4 and botinput == 5):
        print("You won")
    elif (userinput == 4 and botinput == 1) or (userinput == 4 and botinput == 3):
        print("You lost")
    else:
        print("Unentschieden")

    # Spock
    if (userinput == 5 and botinput == 1) or (userinput == 5 and botinput == 3):
        print("You won")
    elif (userinput == 5 and botinput == 2) or (userinput == 5 and botinput == 4):
        print("You lost")
    else:
        print("Unentschieden")


def weiterSpielen():
    print("Weiterspielen [j/n]?")
    keep_playing_input = input()
    if keep_playing_input == 'j':
        main()
    else:
        pass


def rules():
    print("Regeln:")
    print("Schere schneidet Papier")
    print("Schere köpft Echse")
    print("Papier bedeckt Stein")
    print("Papier widerlegt Spock")
    print("Stein zerquetscht Echse")
    print("Stein schleift Schere")
    print("Echse vergiftet Spock")
    print("Echse frisst Papier")
    print("Spock zertrümmert Schere")
    print("Spock verdampft Stein \n")


if __name__ == "__main__":
    rules()
    items = {"Stein": 1, "Papier": 2, "Schere": 3, "Echse": 4, "Spock": 5}
    main()
