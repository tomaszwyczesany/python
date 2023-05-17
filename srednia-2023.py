
# program liczący średnią twmperatur
srednia = 0
suma = 0
srednia1 = 0
suma1 = 0
print("Program liczy średnią n liczb")
#---------------------------------
ilosc = int(input("Podaj srednie dzienne kazdego miesiaca"))
for i in range(ilosc):
      liczba1 =float(input("Podaj liczbe do średniej "))
      suma = suma + liczba1
srednia=float(suma/ilosc)
print("Srednia liczb to :", srednia)
#---------------------------------
ilosc1 = int(input("Podaj srednie nocne kazdego miesiaca"))
for i in range(ilosc1):
      liczba11 =float(input("Podaj liczbe do średniej "))
      suma1 = suma1 + liczba11
srednia1=float(suma1/ilosc1)
print("Srednia liczb to :", srednia1)
