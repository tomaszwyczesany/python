#zadania strona 128
N = 8
lista = [0] * N
def wprowadz_dane():
    for i in range(N):
        lista[i] = int(input("Podaj Liczbe : "))

def wyprowadz_dane():
    for i in range(N):
        print("Lista:",i,"=",lista[i])

wprowadz_dane()
wyprowadz_dane()
# szukanie zera w tablicy 8 elementowej
for i in range(N):
    if lista[i] == 0:
        print("Element listy",lista[i],"jest równy 0")
