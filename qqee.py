print("program do oszczędzania ")
suma_wplat = 0
kwota = float(input("podaj potrzebną kwotę"))

if kwota <= 0:
      print("kwota nie moze byc ujemna")
else:
      while suma_wplat < kwota:
            wplata = float(input("Wprowdz wpłatę"))
            if wplata <= 0:
                  print("wplata nie moze byc ujemna")
            else:
                  suma_wplat = suma_wplat + wplata
      

print("Suma wpłat: ", suma_wplat, " zł")
