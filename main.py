import random as rnd
from time import sleep as wait

while True:
    firsthalf = rnd.randrange(100, 999)
    secondhalf = rnd.randrange(100, 999)
    thirdhalf = rnd.randrange(100, 999)

    wait(1)

    print("+48" + " " + str(firsthalf) + " " + str(secondhalf) + " " + str(thirdhalf))


