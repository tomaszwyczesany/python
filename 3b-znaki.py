wyraz = input("Podaj Wyraz ")
print(wyraz)
print("Ilosc znako twojego słowa to : ",len(wyraz))
for litera in wyraz:
      print(litera)

for i in range(len(wyraz)):
      print(wyraz[i])
#Łączenie wyrazow przykład
w1 = "oto"
w2 = "ma"
w3 = "na"
print(w1+w2+w3)
#Wyodrębnianie indeksów
print(wyraz[0:1])
print(wyraz[-1])
print(wyraz[3:6])
