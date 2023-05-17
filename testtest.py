kwota = float(input("podaj potrzebna kwote"))
suma_wplat = 0

while suma_wplat < kwota:
    wplata = float(input("Wprowdz wpłatę: "))
    suma_wplat = suma_wplat + wplata
    print("Bieżąca wpłata",suma_wplat)

    
print("Suma wpłat : ", suma_wplat, "zł")
input("\n\n Aby zakończyć naciśnij enter")
