moja_lista = [4,6,5,99,1]
print(len(moja_lista)) # funksja len zwraca rozmiar listy
#             0 1 2 3  4
#Zadanie 1 : wyświtl pierwszy i ostatni element listy 
print("Elemment pierwszy mojej listy to : ",moja_lista[0])
print("Elemment ostatni mojej listy to : ",moja_lista[4])
#Zadanie 2 : sprawdzic który element listy
#jest wiekszy pierwszy czy drugi
if moja_lista[0] >= moja_lista[1]:
      print("Element pierwszy jest większy lub równy")
else:
      print("Element drugi jest większy")
#if moja_lista[0] == moja_lista[1]:
#      print("elementy listy rowne")
# Zadanie 3 definicja fukcji suma_danych()
def suma_danych(a):
      suma = 0
      for i in range(len(moja_lista)):
            suma +=a[i]
      print("Suma : ", suma)

suma_danych(moja_lista)
      
      
