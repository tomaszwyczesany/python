def silnia_iter(n):
    wynik = 1
    if n>1:
        for i in range(2,n+1):
            wynik = wynik * i
    return wynik

def silnia_rek(n):
    if n==0:
        return 1
    else:
        return n*silnia_rek(n-1)

liczba = int(input("Podaj liczbe"))

print("Silnia rekurencyjnie :",silnia_rek(liczba))
print("Silnia iter :",silnia_iter(liczba))
