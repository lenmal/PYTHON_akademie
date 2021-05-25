import random


def fce_hra():
    def fce_pozdrav():
        pozdrav = "Hi there!"
        instrukce = """I've generated a random 4 digit number for you. 
Let's play a bulls and cows game."""
        return print(pozdrav, oddelovac * 55, instrukce, oddelovac * 55, sep='\n')

    def fce_hadanka():
        seznam = []
        hadanka = ""
        while len(seznam) < 4:
            number = random.randint(0, 9)
            if number not in seznam:
                seznam.append(number)
        for i in seznam:
            if seznam[0] != 0:
                hadanka += str(i)
        return hadanka

    def fce_cislo():
        cislo = input("Enter number: ")
        pocet = 0
        while True:
            if len(cislo) != 4:
                cislo = input("Please enter 4 digit number: ")
            elif not cislo.isdigit():
                cislo = input("Please enter 4 digit number: ")
            elif cislo.startswith("0"):
                cislo = input("Please enter number not beginning with 0: ")
            else:
                for i in cislo:
                    pocet += cislo.count(i)
                if pocet != 4:
                    pocet = 0
                    cislo = input("Please enter 4 numbers without duplication: ")
                else:
                    break
        return cislo

    def fce_bulls():
        bull = 0
        cow = 0
        for i, num in enumerate(fcislo):
            for ii, numm in enumerate(fhadanka):
                if (i, num) == (ii, numm):
                    bull += 1
                elif (num == numm) and (i != ii):
                    cow += 1
        return [bull, cow]

    pokus = 1
    vysledek = " "
    mn_bull = "bulls"
    mn_cow = "cows"
    oddelovac = "-"

    fce_pozdrav()
    fcislo = fce_cislo()
    fhadanka = fce_hadanka()
    fbull = fce_bulls()

    while fbull[0] != len(fcislo):
        print(fhadanka)
        pokus += 1
        if fbull[0] and fbull[1] > 1:
            print(f"{fbull[0]} {mn_bull}, {fbull[1]} {mn_cow}")
            print(oddelovac * 55)
            fcislo = fce_cislo()
            fbull = fce_bulls()
        elif fbull[0] > 1 and fbull[1] < 2:
            print(f"{fbull[0]} {mn_bull}, {fbull[1]} cow")
            print(oddelovac * 55)
            fcislo = fce_cislo()
            fbull = fce_bulls()
        elif fbull[0] < 2 and fbull[1] > 1:
            print(f"{fbull[0]} bull {fbull[1]} {mn_cow}")
            print(oddelovac * 55)
            fcislo = fce_cislo()
            fbull = fce_bulls()
        else:
            print(f"{fbull[0]} bull {fbull[1]} cow")
            print(oddelovac * 55)
            fcislo = fce_cislo()
            fbull = fce_bulls()

    if pokus < 4:
        vysledek = "amazing!"
    elif pokus < 7:
        vysledek = "average."
    elif pokus < 10:
        vysledek = "not so good."
    else:
        vysledek = "terrible, turn off the game!"

    print(f"Correct, you've guessed the right number in {pokus} guesses!")
    print(oddelovac * 55)
    print(f"That's {vysledek}")


fce_hra()
