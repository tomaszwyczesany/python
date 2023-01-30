# Program odczytuje sekwencje liczb i liczy ile z nich
# jest liczbami parzystymi a ile nieparzystymi.
# Program konczy prace po wpisaniu zera.
parzyste = 0
nieparzyste = 0
# wczytaj pierwsza liczbe
liczba = int(input("Wpisz liczbe lub 0, aby zatrzymac: "))
# 0 konczy wykonywanie
while liczba != 0:
    # sprawdz czy liczba jest nieparzysta
    if liczba % 2 == 1:
        # zwieksz licznik liczb nieparzystych
        nieparzyste += 1
    else:
        # zwieksz licznik liczb parzystych
        parzyste += 1
    # wczytaj kolejna liczbe
    liczba = int(input("Wpisz liczbe lub 0, aby zatrzymac: "))

# wyswietl wynik
print("Liczb nieparzystych:", nieparzyste)
print("Liczb parzystych:", parzyste)