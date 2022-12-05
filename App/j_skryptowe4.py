
liczba1 = int(input("Podaj początek zakresu"))

liczba2 = int(input("Podaj koniec zakresu"))

for liczba in range(liczba1, liczba2+1):
    if liczba %2 ==1 and liczba %17 == 0:
        print(liczba)



rok = int(input("Podaj rok"))

def Czy_przestępny(rok):
    if rok % 4 == 0 and (rok % 100 != 0 or rok % 400 == 0):
        return "Tak"
    else:
        return "Nie"

print(Czy_przestępny(rok))