"""
Aufgabe Programmiere Lottoziehung als Methode:

random.getrand()

Algorithmus zum Zufallszahlenziehen muss so programmiert sein, dass keine
Zufallszahl zweimal gezogen werden kann.
Das heisst, wenn Sie alle 45 Zahlen ziehen mussten, Würden Sie den
Zufallszahlengenerator nur 45-mal benutzen dürfen.
̈
Ziehe die sechs Zahlen und gib Sie am Bildschirm aus
"""
import random as random

from matplotlib import pyplot as plt

numbers = []
drawnNumbers = {}
for i in range(46):
    numbers.append(i)
    drawnNumbers[i] = 0


def drawNumber(listOfNumbers, howManyDraws):
    for i in range(howManyDraws):
        toSwap = random.randint(0, 45 - i)
        listOfNumbers[toSwap], listOfNumbers[45 - i] = listOfNumbers[45 - i], listOfNumbers[toSwap]
    print(listOfNumbers[-6:])
    return listOfNumbers[-6:]


def statistic(howManyDraws):
    for i in range(howManyDraws):
        toCount = random.randint(0, 45)
        drawnNumbers[toCount] = drawnNumbers[toCount] + 1
    return drawnNumbers


drawNumber(numbers, 6)
data = statistic(1000000)

print("\nAlle gezogenene Nummern: " + str(drawnNumbers))
print("Die am häufigsten gezogene Zahl ist: " + str(max(drawnNumbers.items(), key=lambda x: x[1])))
print("Die am seltensten gezogene Zahl ist: " + str(min(drawnNumbers.items(), key=lambda x: x[1])))

names = list(data.keys())
values = list(data.values())

fig, axs = plt.subplots()
axs.bar(names, values)
fig.suptitle('Lottozeihungen')
axs.set_ylabel('Anzahl der gezogenen Zahlen')
axs.set_xlabel('Mögliche Zahlen')

plt.show()
