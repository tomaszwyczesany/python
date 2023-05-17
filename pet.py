kwota = float(input("Podaj pot. kwote"))
suma_wplat = 0

while suma_wplat < kwota:
      wplata = float(input("wprowadz wplate"))
      suma_wplat = suma_wplat + wplata

print("Suma wplat : ", suma_wplat, "zł")
