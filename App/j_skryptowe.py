import sys
breaker = False

while True:

    while True:
        try:
            liczba = int(input("podaj liczbe całkowitą: "))
            break

        except ValueError:
            print("To nie jest liczba całkowita")
            breaker = True
            break
    if breaker:
        break

    def funkcja(liczba):

        if liczba < 0:
            return -1000
        elif liczba == 0:
            return "ZEROOOO!!!!"
        elif 0 < liczba < 10:
            return liczba
        elif 10 <= liczba <= 100:
            return "dużo"
        elif liczba > 100:
            return "bardzo dużo"

    print(funkcja(liczba))


