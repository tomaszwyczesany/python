N=5
a=[0] * N 
def wprowadz_dane_do_listy():
    for i in range(N):
        a[i] = int(input("Podaj liczbe"))
def wyswietl():
    for i in range(N):
        print("a[",i,"] = ", a[i])
wprowadz_dane_do_listy()
if a[0] > a[1]:
    print("większym ele. jest pierwszy ele. listy a[0]")
else:
    print("większym ele. jest drugi ele. listy a[1]")
wyswietl()
