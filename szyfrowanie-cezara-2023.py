def znak_na_kod(znak):
    return ord(znak.upper()) - ord('A')
def kod_na_znak(kod_znaku):
    return chr(kod_znaku + ord('A'))
def zaszyfruj(napis):
    wynik = ""
    for znak in napis:
        kod_znaku = znak_na_kod(znak)
        kod_znaku_zaszyfrowany = (kod_znaku +3) % 26
        wynik += kod_na_znak(kod_znaku_zaszyfrowany)
    return wynik
def deszyfruj(napis):
    wynik = ""
    for znak in napis:
        kod_znaku = znak_na_kod(znak)
        kod_znaku_odszyfrowany = (kod_znaku - 3 + 26) % 26
        wynik += kod_na_znak(kod_znaku_odszyfrowany)
    return wynik
tekst = input("Podaj tekst do zaszyfrowania")
szyfrogram = zaszyfruj(tekst)
print( "Teskt zaszyfrowany : ", szyfrogram)
print( "Teskt odszyfrowany : ", deszyfruj(szyfrogram))