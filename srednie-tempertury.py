suma = 0.0
srednia = 0.0
for i in range(12):
    temp = float(input("Podaj temperature"))
    suma = suma + temp

srednia = suma / 12
print("Średnia temp z 12 mies : ", srednia)