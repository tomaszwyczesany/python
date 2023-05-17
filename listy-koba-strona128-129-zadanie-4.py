N = 8
lista = [0] * N

def wczytaj_elementy_listy():
      for i in range(N):
            lista[i] = int(input("podaj liczbe do listy"))
def wyswietl_elementy_listy():
      for i in range(N):
            print("Element",lista[i],"listy")

wczytaj_elementy_listy()

wyswietl_elementy_listy()
# szukanie zerowego elementu listy
i = 0
while lista[i] != 0:
      i=i+1
      if lista[i] == 0:
            print("element listy",i,"rowny",lista[i])
            break
      else:
            print("Brak elementu zero")

      

