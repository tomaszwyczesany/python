# print('siema!')
# print("siema!")
# print('Mc\'Donalds')
# print("Mc'Donalds")
# x="Hello"
# print(x+" world!")
# y=10
# print("y="+y)
# y=10
# print("y=",y)
# print("y="+ str(y) )
# x=5
# y=10
# print("x={} y={}".format(x,y))

# x=input('podaj x:')
# print('x wynosi '+x)
# print(type(x),type(1),type(1.3))

# 10:31

# x=input('podaj x:\n')
# print("x={}".format(x))
# print("x="+x)
# print(f"x={x}")
#
# x=10
# print(x)
# x="coś innego"
# print(x)

# Napisz program który przyjmie od użyszkodnika imię oraz nazwisko, a następnie
# wypisze na konsoli komunikat typu "Witaj TwojeImie TwojeNazwisko!"
#
# imie=input('podaj imię:\n')
# nazwisko=input('podaj nazwisko:\n')
# print(f"Witaj {imie} {nazwisko}!")
# print("Witaj "+imie+" "+nazwisko+"!")
# print("Witaj {} {}!".format(imie,nazwisko))

#
# wynik=round(10/3,2)
# print(wynik)

# a=int(input('podaj a:'))
# b=int(input('podaj b:'))
# wynik=round(a/b,2)
# print(wynik)
#
# a=float(input('podaj a:'))
# b=float(input('podaj b:'))
# wynik=round(a/b,2)
# print(wynik)
# print(pow(1.76,2))
# 2. BMI= masa/(wzrost*wzrost) .
# Napisz program który odbierze od użytkownika jego masę w kilogramach i wzrost
# w metrach, wyliczy i wypisze BMI.
# x=50
# print("x="+str(x))
# print("x={}".format(x))
# print(f"x={x}")

# wzrost=float(input('podaj wzrost:\n'))
# masa=float(input('podaj masę:\n'))
# #bmi=masa/(wzrost*wzrost)
# bmi=round(masa/pow(wzrost,2),2)
# print(f'Twoje bmi wynosi {bmi}')
# print('Twoje bmi wynosi {}'.format(bmi))
# print(f'Twoje bmi wynosi '+str(bmi))


# x=2
# if x==1:
#     print('x jest równe jeden')
#     print('!!!!')
# print('koniec')


# x=2
# if x==1:
#     print('x jest równe jeden')
#     print('!!!!')
# else:
#     print('x NIE jest równe jeden')
# print('koniec')

#
# x=2
# if x==1:
#     print('x jest równe jeden')
# elif x==2:
#     print('x jest równe dwa')
# elif x==3:
#     print('x jest równe trzy')
# elif x==4:
#     print('x jest równe cztery')
# else:
#     print('powyżej 4 lub poniżej 1')
# print('koniec')
# x=11
# if x>0:
#     pass

# 3. Niech użytkownik poda jakąś liczbę. Jeśli poda dodatnią to
# chcemy wyświetlić tę wartość z informacją "wartość dodatnia",
# jeśli zero to wyświetlamy z informacją "równe zero",
# jeśli ujemna to wyświetlamy "wartość ujemna".

# liczba=float(input('podaj liczbę:\n'))
# if liczba>0:
#     print(f'{liczba} jest dodatnia')
# elif liczba==0:
#     print(f'{liczba} jest równa zero')
# else:
#     print(f'{liczba} jest ujemna')

# if 1==1:
#     print('1==1')
#
# if 2==2:
#     print('2==2')
#
#
# if 1==1:
#     pass
# elif 2==2:
#     pass

# przerwa do 11:40

# 4.Rozbuduj swoj program do bmi w taki sposob by poza wyswietleniem obliczonego bmi
#  wyswietlil nam rowniez odpowiedni opis wg skali z Wikipedii.
#
# wzrost=float(input('podaj wzrost:\n'))
# masa=float(input('podaj masę:\n'))
# bmi=round(masa/pow(wzrost,2),2)
# print(f'Twoje bmi wynosi {bmi}')
#
# if bmi<16:
#     print('wyglodzenie')
# elif  bmi<17:
#     print('wychudzenie')
# elif bmi<18.5:
#     print('niedowaga')
# elif bmi<25:
#     print('masa ok')
# elif bmi<30:
#     print('nadwaga')
# elif bmi<35:
#     print('Otylosc 1 stopnia')
# elif bmi<40:
#     print('Otylosc 2 stopnia')
# else:
#     print('Otylosc 3 stopnia')


# for x in range(10):
#     print('hello!')

# for x in range(10):
#     print(f'hello! x={x}')
#
# for x in range(1,11):
#     print(f'hello! x={x}')

# 5. Wyświetl 20 kolejnych potęg liczby 2

# print(  pow(2,x)  )\
#
# for x in range(1,21):
#     print(f'2^{x}={pow(2,x)}')

#
# x=10
# if x>0:
#     for i in range(1,x+1):
#         print(i)

# for x in range(-10,11):
#     if x<0:
#         print(f'{x} jest ujemne')
#     elif x==0:
#         print(f'{x} jest zerem')
#     else:
#         print(f'{x} jest dodatnie')

# 6. Wydrukuj liczby w zakresie 1-100 wypisujac obok czy dana liczba jest
#  parzysta czy nieparzysta
#
# print(10%2)
#
#
# for liczba in range(1,101):
#     if liczba%2==0:
#         print(f'{liczba} jest parzysta')
#     else:
#         print(f'{liczba} jest NIEparzysta')

# przerwa obiadowa do 13:02
# oproc=0.03
# 7. Napisz symulator lokaty. Symulator ma przyjmować przez zmienne:
# - kwotę lokaty
# - oprocentowanie w skali roku
# - ilość miesięcy na jaką zakladamy lokatę
# Symulator ma dla każdego miesiąca lokaty wypisać który to miesiąc
# oraz ile mamy aktualnie zgromadzone na koncie po doliczeniu odsetek.
# Kapitalizacja comiesięczna

# for x in range(1,ilosc_miesiecy+1):
#
# kapital=100000
# oproc=0.03
# ilosc_miesiecy=24
# for m in range(1,ilosc_miesiecy+1):
#     kapital=round(kapital+(kapital*oproc/12),2)
#     print(f'miesiac={m} kapital={kapital}')


# x=1
# while x<1000:
#     x=x*2
#     print(x)
#
# x=10
# while x<1000:
#     x=x*2
#     print(x)
#
# while 1==1:
#     print('dupa')
#
#
# while True:
#     print('dupa')

# 8. Napisz pętlę while która będzie wyświetlała kolejne potęgi liczby 2
# aż wartość  potęgi nie przekroczy wartości podanej przez użytkownika
# #
# max=int(input('podaj max zakres:\n'))
# wartosc=0
# x=1
# while wartosc<max:
#     wartosc=pow(2,x)
#     print(wartosc)
#     x+=1
#
# x=1
# while x<1000:
#     #x=x*2
#     x*=2
#     print(x)
#
# #x=x+1
# #x+=1
#
# import random
# for x in range(10):
#     print(random.randint(1,100))

# 9.Napisz program który będzie dodawał kolejne losowe wartości z zakresu
# od 1 do 10 do zmiennej suma, tak dlugo az suma nie osiagnie wartosci
# wiekszej od wartosci podanej przez uzytkownika
# suma=0
#
# import random
# suma=0
# max=1000
# while suma<max:
#     suma+=random.randint(1,10)
#     print(suma)

# tekst="siała BABA mak"
# print(tekst)
# print(tekst.upper())
# print(tekst.lower())
# print(tekst.replace("a",'X'))
# print(tekst)
# print(tekst.lower().replace("a",'X'))
# print(tekst.replace("a",'').replace("A",''))
# tekst=tekst.replace("a",'X')
# print(tekst)

# 10. Napisz program który przyjmie od użyszkodnika ciąg tekstowy
# a następnie usunie z niego znaki ,.!? i wyświetli powiększony do
# dużych liter na konsoli


# tekst=input('podaj tekst:\n')
# print(tekst.replace(',','').replace('.','').replace('!','').replace('?','').upper())

# print(input('podaj tekst:\n').replace(',','').replace('.','').replace('!','').replace('?','').upper())

# przerwa do 14:29
#
# for linia in open('dane.csv',encoding='utf-8'):
#     print(linia.strip())

# tekst='siała baba mak'
# print(len(tekst))
#
# for linia in open('dane.csv',encoding='utf-8'):
#     print(linia.strip(),'#',len(linia.strip()) )

# 11. Napisz program który wyświetli na konsoli niepuste linie z
# pliku tekstowego którego nazwę poda użytkownik

# for linia in open('dane.csv',encoding='utf-8'):
#     if len(linia.strip())>0:
#         print(linia.strip())

# calosc=open('dane.csv',encoding='utf-8').read()
# print(calosc)

# tekst="siała BABA mak"
# print(tekst.count('a'))
# print(tekst.lower().count('a'))
# if "baba" in tekst.lower():
#     print('jest')
# else:
#     print('niet!')


# 12. Napisz program który zliczy ilość wystąpień małej lub dużej
# wersji ciagu tekstowego podanego przez użytkownika w pliku którego nazwę
# również poda użytkownik
# zawartosc=open('tadzio.txt',encoding='utf-8').read()
# poszukiwane='tadEusz'
# print(f'znaleziono {zawartosc.lower().count(poszukiwane.lower())}')
#
# nazwa_pliku=input('podaj nazwę pliku:\n')
# poszukiwane=input('podaj czego szukasz:\n')
# zawartosc=open(nazwa_pliku,encoding='utf-8').read()
# print(f'znaleziono {zawartosc.lower().count(poszukiwane.lower())} wystąpień słowa {poszukiwane}')


# 13. Napisz wyszukiwarkę plikową. Wyszukiwarka powinna odebrać od użytkownika
# poszukiwaną frazę, oraz nazwę pliku. Wyszukiwarka powinna wyświetlić
#  linie w których znalazła poszukiwaną frazę wraz z numerem linii. Wyszukiwarka
#  po  odebraniu danych od uzyszkodnika powinna wyswietlic jakiej frazy
#  i  jakim pliku szuka. Wyszukiwarka powinna być nieczula na wielkosc liter.
#
# nazwa_pliku=input('podaj nazwę pliku:\n')#'tadzio.txt'
# szukane=input('podaj szukaną frazę:\n').lower()#'Tadeusz'
# x=0
# print(f'szukam "{szukane}" w pliku {nazwa_pliku}')
# for linia in open(nazwa_pliku,encoding='utf=8'):
#     x+=1
#     if szukane in linia.lower():
#         print(x,linia.strip())
#
#
# krotka=()
# lista=[]
# lista=list()
# lista=[1,2,3,4,5,'nietoperz']
# lista.append(6666)
# lista.insert(0,'poczatek')
# for element in lista:
#     print(element)
# print(lista)
#
# lista=[]
# for x in range(1,11):
#     lista.append(x)
# print(lista)

# 14. Napisz kod który umieści w liście 10 kolejnych potęg liczby 2.
# Następnie przeiteruj po tej liście i każdy z jej elementów wyświetl
# na konsoli w osobnej linii.
# lista=[]
# for e in range(1,11):
#     lista.append(pow(2,e))
# print(lista)
# for l in lista:
#     print(l)
#
# for l in [pow(2,e) for e in range(1,11)]: print(l)

# import this

# import random
# print(random.randint(1,100))
# lista1=[1,2,3,4,5]
# lista2=[6,7,8,9,10]
# print(lista1)
# print(*lista1)
# lista3=[*lista1,*lista2]
# print(lista3)

# lista1=[1,2,3,4,5]
# lista2=[6,7,8,9,10]
# lista1.extend(lista2)
# print(lista1)

#
# lista1=[1,2,3,4,5]
# lista2=[6,7,8,9,10]
# lista3=[]
# lista3.extend(lista1)
# lista3.extend(lista2)
# print(lista3)

# 15. Stwórz dwie listy. Każda z list ma zawierać 10 liczb losowych z zakresu 1-10.
# Połącz te dwie listy do jednej i wyswietl na konsoli (extend albo *lista)
#
# import random
# #
# lista1 = []
# lista2 = []
# for x in range(10):
#     lista1.append(random.randint(1, 10))
#     lista2.append(random.randint(1, 10))
# print(lista1)
# print(lista2)
# wynik=[*lista1,*lista2]
# print(wynik)
#
# print([*[random.randint(1,10) for e in range(10)],
#        *[random.randint(1,10) for e in range(10)]]
#       )
#
#
# lista1=[1,2]
# lista2=[3,4]
# lista3=[lista1,lista2]
# print(lista3)
# print(lista3[0])
# print(lista3[0][1])
# lista4=[  [1,'A'],[2,'B']  ]
# for l in lista4:
#     print(l)
#
# lista=[]
# for x in range(1,11):
#     podlista=[x,x*100]
#     lista.append(podlista)
# print(lista)
# for l in lista:
#     print(l)


#16. Korzystajac z petli stworz liste zawierajaca elementy same bedace listami.
# Kazdy taki element ma zawierac numer potegi oraz wartosc tej potegi dla liczby 2.

#[1,2],[2,4],[3,8],[4,16]

# lista=[]
# for x in range(1,11):
#     podlista=[x,pow(2,x)]
#     lista.append(podlista)
# print(lista)

# lista=[]
# for x in range(1,11):
#     lista.append(  [x,pow(2,x)]  )
# print(lista)

# lista=[]
# for x in range(1,11):
#     lista.append(x)
# print(lista)
#
# lista=[x*1000 for x in range(1,11)]
# print(lista)
# import random
# losowa=[random.randint(1,10) for e in range(1,11)]
# print(losowa)
# print([random.randint(1,10) for e in range(1,11)])

# lista=[x for x in range(1,11) if x%2==0]
# print(lista)

# lista=[x*333 for x in range(1,11) if x%2==0]
# print(lista)


# lista=[  [x,pow(2,x)] for x in range(1,11) ]
# print(lista)
# import random
# lista=[random.randint(1,100) for e in range(1,101)]
# print(lista)
# przetworzone=[e*1000 for e in lista if e%2==0]
# print(przetworzone)

#17. Korzystając z list składanych wygeneruj listę zawierajaca 10 kolejnych poteg 2Andr
#
# liczby=[]
# for x in range(1,11):
#     liczby.append(pow(2,x))
# print(liczby)
#
# lista=[pow(2,x) for x in range(1,11)]
# print(lista)
#
# print([pow(2,x) for x in range(1,11)])
#
# #przerwa do 10:29


#18. Korzystając z list składanych wygeneruj listę 10 elementow której każdy
# element również będzie listą. Pierwszy element tej podlisty to numer potegi,
# a drugi to wartosc tej potegi dla liczby 2
#
# lista=[ [e,e*100] for e in range(1,101)]
# print(lista)


# lista=[ [e,pow(2,e)] for e in range(1,11)]
# print(lista)
# for l in lista:
#     print(l)


#for l in [ [e,pow(2,e)] for e in range(1,11)]:print(l)

#19. Napisz program który z pliku dane.csv wyświetli powiekszone imiona
# i nazwiska oraz wzrost i masę

# for linia in open('dane.csv',encoding='utf-8'):
#     lista=linia.strip().split(';')
#     print(lista[1].upper(),lista[2].upper(),lista[3],lista[4])

# for linia in open('dane.csv',encoding='utf-8'):
#     print(linia.strip())
#
# linia="1;Renault;Kadjar"
# print(linia)
# print(linia.split(';'))
# lista=linia.split(';')
# print(lista[1])
# print(lista[1].upper())

#20.Korzystajac z list skladanych zaladuj do listy zawartosc pliku dane.csv
# w taki sposób   by linie oczyścic z bialych znaków i rozbić na listy.
# Każdy z elementów listy sam   powinien byc listą.
# Następnie przeiteruj po wyniku i wyświetl wszystkie elementy listy
# linia po linii.

#e.strip().split(';')


# lista=[e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]
# for l in lista:
#     print(l)

# for l in [e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]:
#     print(l)

#print(*'dupa')
#
# for l in [e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]:
#     print(l)
#
# for literka in 'dupa':
#     print(literka)

#21. * Dla każdego wpisu w pliku dane.csv wyświetl na konsoli dane o
#   id, imieniu,nazwisku, wzroscie,masie oraz obliczonym bmi zawodnika

# wzrost=1.76
# masa=75
# bmi=round(masa/pow(wzrost,2),2)
# print(bmi)

# for l in [e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]:
#     print(float(l[3]),type(float(l[3])))

# for l in [e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]:
#     wzrost=float(l[3])
#     masa=float(l[4])
#     bmi=round(masa/pow(wzrost,2),2)
#     l.append(bmi)
#     print(l)
#
# for l in [e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]:
#     l.append(round(float(l[4])/pow(float(l[3]),2),2))
#     print(l)
#

#przerwa do 11:39

# lista=[1,2,3,4,5]
# print(lista[2])
# print(lista[0:4])
# lista=[1,2,3,4,5]
# druga=lista
# lista.clear()
# print(lista)
# print(druga)
#
# lista=[1,2,3,4,5]
# druga=lista.copy()
# lista.clear()
# print(lista)
# print(druga)
# lista=[1,2,3,4]
# druga=[*lista]

#lista=[]

#tekst=tekst.replace('a','X')
#
# lista=['koza','banan','nietoperz']
# print(lista.index('banan'))
#
# lista=['koza','banan','nietoperz']
# lista.sort()
# print(lista)

#
# lista=['koza','banan','nietoperz']
# lista.sort(reverse=True)
# print(lista)


# lista=['koza','banan','nietoperz']
# lista.sort()
# lista.reverse()
# print(lista)
#
# lista=['koza','banan','nietoperz','1','2','10','20']
# lista.sort()
# print(lista)
#
# lista=[65,4,3,111,2222,767,8]
# lista.sort()
# print(lista)

#22.Wygeneruj listę 10 elementów o losowej wartości liczbowej,
# posortuj listę i wyświetl jej zawartość linia po linii
#
# import random
# lista=[random.randint(1,11) for x in range(10)]
# print(lista)
# lista.sort()
# print(lista)
# for e in lista:
#     print(e)
#
# from operator import itemgetter
# lista=[
#     [1,'B'],
#     [3,'A'],
#     [2,'C']
# ]
#
# print(lista)
# #lista.sort(key=itemgetter(1))
# lista.sort(key=itemgetter(1), reverse=True)
# print(lista)

#23. Wczytaj do listy kolejne wiersze z pliku dane.csv.
# Dane posortuj po nazwiskach i wyswietl linia po linii na konsoli.

from operator import itemgetter
# lista=[e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]
# #lista.sort(key=itemgetter(2))
# lista.sort(key=lambda x:x[2].upper())
# for l in lista:
#     print(l)

#24. Wyświetl na konsoli linia po linii dane z pliku dane.csv
# ale posortowane  malejąco wg. bmi

# lista=[e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]
# for l in lista:
#     wzrost=float(l[3])
#     masa=float(l[4])
#     bmi=round(masa/pow(wzrost,2),2)
#     l.append(bmi)
#
# from operator import itemgetter
# lista=[e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]
# for l in lista:
#     bmi=round(float(l[4])/pow(float(l[3]),2),2)
#     l.append(bmi)
# lista.sort(key=itemgetter(5),reverse=True)
# for l in lista:
#     print(l)

#PRZERWA OBIADOWA DO 13:05

#25.POKAZAĆ OS.WALK i operator in dla stingow i list.
# Napisz wyszukiwarkę plików która przyjmie od użytkownika szukaną frazę i
# katalog startowy. Wyszukiwarka ma wyswietlić wszystkie pliki i katalogi
# zawierajace w nazwie szukaną frazę - wraz ze ścieżkami.
# Wyszukiwarka ma być nieczuła na wielkość liter
#
# import os
# for w in os.walk('E:\\'):
#     print(w[0],w[1],w[2])


#
# import os
# for w in os.walk('E:\Big Data'):
#     #print(w[0],w[1],w[2])
#     print(f'########## ścieżka={w[0]}')
#     for plik in w[2]:
#         print(plik)
#
# if "baba" in "siała baba mak":
#     print('jest')
# else:
#     print('nie ma')


# szukane="baba"
# tekst="siała baba mak"
# if szukane.lower() in tekst.lower():
#     print('jest')
# else:
#     print('nie ma')

# lista=['siala','baba','mak']
# for l in lista:
#     if 'bab'.lower() in l.lower():
#         print(f'znaleziono bab w {l}')
# if 'bab' in lista:
#     print('jest')
# else:
#     print('niet')

#25.
# Napisz wyszukiwarkę plików która przyjmie od użytkownika szukaną frazę i
# katalog startowy. Wyszukiwarka ma wyswietlić wszystkie pliki i katalogi
# zawierajace w nazwie szukaną frazę - wraz ze ścieżkami.
# Wyszukiwarka ma być nieczuła na wielkość liter
#

#
# szukane="baba"
# tekst="siała baba mak"
# if szukane.lower() in tekst.lower():
#     print('jest')
# else:
#     print('nie ma')
#
# import os
# szukane=input('czego szukasz:\n')#'oracle'
# gdzie=input('ścieżka startowa:\n')
# for w in os.walk(gdzie):
# #    print(w)
#     for katalog in w[1]:
#         if szukane.upper() in katalog.upper():
#             print(w[0],'\\',katalog)
#     for plik in w[2]:
#         if szukane.upper() in plik.upper():
#             print(w[0],'\\',plik)


# lista=[1,2,3,1,2,3]
# lista.sort()
# krotka=(1,2,3,1,2,3)
# lista=list(krotka)
# lista.sort()
# krotka=tuple(lista)
# print(krotka)
# print(lista)
# #krotka.sort()

# krotka1=(1,2,3)
# krotka2=(4,5,6)
# suma=(*krotka1,*krotka2,'coś jeszcze')
# print(suma)
# print(suma[0])
# print(suma[0:6])
#

#26. Stwórz dwie krotki. Jedna ma zawierać 10 losowych liczb zakresu 1-10,
# druga 10 losowych liczb zakresu 11-20. Stwórz trzecią krotkę która ma
# zawierać dane z obu krotek. Trzecią krotkę wypisz na konsoli
# import random
# k1=tuple([random.randint(1,10) for e in range(10)])
# k2=tuple([random.randint(11,20) for e in range(10)])
# print(k1)
# print(k2)
# suma=(*k1,*k2)
# print(suma)

#przerwa do 14:27


#27. Napisz kod ktora wyświetli w postaci listy krotek zawartość pliku dane.csv

# lista=[   tuple(e.strip().split(';')) for e in open('dane.csv',encoding='utf-8')]
# print(lista)
# for l in lista:
# #     print(l)
# import matplotlib.pyplot as plt
# #import random
# from random import randint
# #lista=[random.randint(1,100) for e in range(20)]
# lista=[randint(1,100) for e in range(20)]
# print(lista)
# plt.plot(lista)
# plt.savefig('wykres.png')
# plt.show()


#
# import matplotlib.pyplot as plt
# from random import randint
# lista1=[randint(1,100) for e in range(20)]
# lista2=[randint(1,100) for e in range(20)]
# print(lista1)
# print(lista2)
# plt.plot(lista1)
# plt.plot(lista2)
# plt.show()

#
# import matplotlib.pyplot as plt
# from random import randint
# lista1=[randint(1,100) for e in range(20)]
# os_x=[e for e in range(1,21)]
# print(lista1)
# plt.bar(lista1,os_x)
# plt.show()
#
# zbior={1,1,2,2,3,3,3,3,3,3,3,3,4}
# #slownik={'klucz1':111,'klucz2':222}
# print(type(zbior))
# print(zbior)
#
# z1={1,2,3,4}
# z2={3,4,5,6}
#
# print("część wspólna=",z1.intersection(z2))
# print("suma zbiorów =",z1.union(z2))
# print("z1-z2 =",z1.difference(z2))
# print("z2-z1 =",z2.difference(z1))

# l1=[1,2,3,3,3,3,3,3,3]
# l2=[3,3,3,3,4,4,4,4,4]
# z1=set(l1)
# z2=set(l2)
# print(z1)
# print(z2)
#
# l1=[1,2,3,3,3,3,3,3,3]
# print( list(set(l1))  )

#
# zestaw=set()
# for x in range(10):
#     zestaw.add(x)
# print(zestaw)
#
# lista={1,2,3,4}
# print(len(lista))
# print(sum(lista))
# print(sum(lista)/len(lista))
# print(max(lista))
# print(min(lista))
# krotka=(2,3,4,5,1,2,3)
# krotka=sorted(krotka)
# print(krotka)
# import random
# zestaw1={random.randint(1,40) for e in range (1,21)}
# print(zestaw1)
# zestaw2={random.randint(1,40) for e in range (1,21)}
# print(zestaw2)

# #zestaw1.add(zestaw2)
# print(zestaw1)


#28. Wygeneruj dwa zestawy, dodaj do nich po 20
# (w przypadku duplikatów lista może być mniejsza niż 20 elementów)
# losowych liczb z zakresu 1-40. Wyswietl ich sumę, różnicę i część wspólną
# import random
# z1={random.randint(1,40) for e in range(20)}
# z2={random.randint(1,40) for e in range(20)}
# print(z1)
# print(z2)
# print('suma=',z1.union(z2))
# print('część wspólna=',z1.intersection(z2))
# print('z1-z2=',z1.difference(z2))
# print('z2-z1=',z2.difference(z1))

# z1={ (1,'A'),(2,'A'),(1,'A'),(2,'B') }
# print(z1)

#29. Zduplikuj jeden z wierszy w pliku dane.csv.
# Napisz kod który zwróci do postaci listy krotek
# zawartość tego pliku z danymi bez powtórek.
#
# lista_krotek=[ tuple(e.strip().split(';')) for e in open('dane.csv',encoding='utf-8')]
# print(lista_krotek)
# wynik=list(set(lista_krotek))
# for z in wynik:
#     print(z)


# plik=open('output.csv',encoding='utf-8',mode="w")
# for x in range(1,11):
#     plik.write(f'koza spadła z woza po raz {x}\n')
# plik.close()
#
# lista=[1,'Andrzej','Klusiewicz']
# lista[0]=str(lista[0])
# linia=";".join(lista)
# print(linia)

#
# plik=open('output.csv',encoding='utf-8',mode="w")
# for x in range(1,11):
#     plik.write(f'koza spadła z woza po raz {x}\n')
#     print(1/0)
# plik.close()


# with open('output.csv',encoding='utf-8',mode="w") as plik:
#     for x in range(1,11):
#         plik.write(f'koza spadła z woza po raz {x}\n')
#     print('koniec managera kontekstu')
# print('koniec programu')


# linia='costam;1,76'
# print(linia)
# linia=linia.replace(',','.')
# print(linia)

#lista=[e.replace(',','.') for e in open('dane.csv') if ...]

#len(linia.strip())


#30. Przetwórz plik dane.csv w taki sposób by w efekcie umieścić w pliku output.csv
# dane z pliku dane.csv wzbogacone o obliczone BMI, bez duplikatów i rozwiązując
# problem  podania przecinka w miejsce kropki we wzroście i masie oraz problem
# z pustymi wierszami.
# import requests
# import re
# strona=requests.get('http://jsystems.pl')
# #print(strona.text)
# print(re.findall('.*\.png',strona.text))

# lista=list(set([tuple(e.strip().replace(',','.').split(';')) for e in open('dane.csv',encoding='utf-8') if len(e.strip())>0]))
# with open('output.csv',encoding='utf-8',mode='w') as plik:
#     for l in lista:
#         l=list(l)
#         bmi=round(float(l[4])/pow(float(l[3]),2),2)
#         l.append(str(bmi))
#         plik.write( ';'.join(l)+"\n" )

# lista=[
#     (1,'Andrzej'),
#     (2,'Stefan')
# ]
# wynik=[list(e) for e in lista]
# for w in wynik:
#     w.append('Klusiewicz')
# print(wynik)
#

# lista=list(set([tuple(e.strip().replace(',','.').split(';')) for e in open('dane.csv',encoding='utf-8') if len(e.strip())>0]))
# with open('output.csv',encoding='utf-8',mode='w') as plik:
#     for l in lista:
#         l=list(l)
#         bmi=round(float(l[4])/pow(float(l[3]),2),2)
#         l.append(str(bmi))
#         plik.write( ';'.join(l)+"\n" )

#przerwa do 10:39
#
# sl=dict()
# sl['klucz1']='Wartość'
# sl['inny_klucz']=1234
# sl['lista']=[1,2,3,'nietoperz']
# sl['krotka']=(6,7,8,9)
# #
# # print(sl['krotka'])
# # print(sl['dupa'])
#
# for klucz in sl:
#     print(klucz,sl[klucz])

#31. Stwórz plik ustawienia.txt i umieść w nim poniższe dane
# encoding;utf-8
# timezone;-2
# color;black
# Następnie wczytaj dane do słownika w ten sposób by pierwsza kolumna
# stanowila klucze a druga przypisane do nich
# wartości. Przeiteruj po słowniku i wypisz klucze oraz przypisane do nich wartości

# lista=[e.strip().split(';') for e in open('ustawienia.csv')]
# sl=dict()
# for l in lista:
#     sl[l[0]]=l[1]
# for k in sl:
#     print(k,sl[k])

# sl={'klucz1':1111, 'klucz2':'koza'}
# for k in sl:
#     print(k,sl[k])


#32. Wczytaj do słownika dane z pliku dane.csv tak by kluczem było
# imię sklejone z nazwiskiem rozdzielone spacja, a pozostałe dane znalazły się w wartości
#   jako krotka lub lista. Przeiteruj po slowniku i wyswietl jego zawartość.
# lista_list=[[1,'A'],[2,'B']]
# kolumna=[e[1] for e in lista_list]
# print(kolumna)
#
# lista_list=[e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]
# sl=dict()
# for ll in lista_list:
#     klucz=ll[1]+' '+ll[2]
#     wartosc=(ll[0],ll[3],ll[4])
#     sl[klucz]=wartosc
# for k in sl:
#     print(k,sl[k])


# lista_list=[e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]
# sl=dict()
# for ll in lista_list: sl[ll[1]+' '+ll[2]]=(ll[0],ll[3],ll[4])
# for k in sl: print(k,sl[k])


#przerwa do 11:47

#33. Wyświetl wynik dzielenia 1 przez kolejne liczby z zakresu -10 do 10.
#ZeroDivisionError
#
# for x in range(-10,11):
#     print(1/x)

# print('start')
# try:
#     print(1/0)
#     print('coś dalej')
# except:
#     print('wyjątek!')
# print('koniec')
#
# print('start')
# try:
#     print(1/0)
#     print('coś dalej')
# # except ZeroDivisionError:
# #     print('nastąpiło dzielenie przez zero')
# except IndexError:
#     print('wyjątek indeksu')
# except IOError:
#     print('błąd odczytu/zapisu')
# except Exception as e:
#     print(f'inny wyjątek: {e}')
# print('koniec')

#34. Wyświetl wynik dzielenia 1 przez kolejne liczby z zakresu -10 do 10
# w taki sposob by w przypadku wyjatku nie przerywac dzialania petli a po
# prostu wyswietlic na konsoli informację o błędzie i przejsc do dalszego przetwarzania

# for x in range(-10,11):
#     try:
#         print(x,1/x)
#     except ZeroDivisionError:
#         print(x,f'blad dzielenia przez zero przy wartosci {x}')

# try: #zle rozwiazanie!!!!
#     for x in range(-10,11):
#         print(x,1/x)
# except ZeroDivisionError:
#         print(f'blad dzielenia przez zero ')

#35. Przetwórz wszystkie wiersze z dane.csv wyswietlajac na konsoli dane z
# wiersza wzbogacone o bmi. Nie podmieniaj przecinków etc w tekscie.
# W przypadku pojawienia się wyjątku na obliczaniu bmi dla
# któregoś wiersza chcemy go zapisać (cały wiersz) w osobnym pliku bledy.csv
# wzbogacony o informację o rodzaju błędu
#4;Andrzej;1,89;90;IOERROR
#
# lista=[e.strip().split(';') for e in open('dane.csv',encoding='utf-8')]
# for l in lista:
#     try:
#         wzrost=float(l[3])
#         masa=float(l[4])
#         bmi=round(masa/pow(wzrost,2),2)
#         l.append(bmi)
#         print(l)
#     except Exception as e:
#         #print(f'{e} na ',l)
#         with open('bledy.csv',encoding='utf-8',mode='a') as plik:
#             linia=';'.join(l)
#             plik.write(linia+';'+str(e)+'\n')


#przerwa obiadowa do 13:17
#
# def witacz():
#     print('siemka!')
#
# witacz()



# def witacz(ile):
#     for x in range(1,ile+1):
#         print(f'siema po raz {x}')
#
# witacz(10)

#
# def dodaj(a,b):
#     print(a+b)

#
# def dodaj(a,b):
#     suma=a+b
#     return suma
#
#
# wynik=dodaj(10,20)
# print(wynik)

#DRY

#36.Stwórz funkcję która przyjmie wzrost i masę a zwróci zaokraglone do 2 miejsc po przecinku BMI.

# W przypadku pojawienia się wyjątku, wyświetl na konsoli jaki wystąpił problem a z funkcji zwróć -1.

# def bmi(masa,wzrost):
#     try:
#         return round(masa/pow(wzrost,2),2)
#     except ZeroDivisionError:
#         print('wzrost jest równy zero!')
#         return -1
# #wynik=bmi(57,0)
# wynik=bmi(57,1.75)
# print(wynik)


#37.  Napisz funkcję która zwróci pod postacią listy list zawartość pliku
#  którego nazwę przekażemy przez pierwszy argument funkcji. Plik ma być otwarty z kodowaniem
#  podanym jako drugi argument funkcji.
from uu import encode

#open(nazwa_pliku,encoding=kodowanie)

#Jeśli kodowanie nie zostanie pdane ma przyjac utf-8
# def csv2list(nazwa_pliku,kodowanie):
#     lista=[e.strip().split(';') for e in open(nazwa_pliku,encoding=kodowanie)]
#     return lista
#
# def csv2list(nazwa_pliku,kodowanie='utf-8'):
#     print(f'kodowanie pliku={kodowanie}')
#     return [e.strip().split(';') for e in open(nazwa_pliku,encoding=kodowanie) if len(e.strip())>0]
#
# #wynik=csv2list('dane.csv','windows-1250')
# wynik=csv2list('dane.csv')
# print(wynik)
# for e in wynik:
#     print(e)

# def funkcja(obowiazkowy,opcjonalny='domyślne...'):
#     print(f'obowiazkowy={obowiazkowy}')
#     print(f'opcjonalny={opcjonalny}')

#funkcja(1,2)
#funkcja(1)
#funkcja()

#38. Napisz funkcję która bedzie w stanie przyjąć taką listę jaka jest zwracana
 # przez funkcję z poprzedniego ćwiczenia. Funkcja ta ma przeiterować po otrzymanej
 # liście i wyświetlić każdy element na konsoli. Odbierz dane z funkcji z ćwiczenia
 # poprzedniego i przekaz do nowo powstalej funkcji.



# def csv2list(nazwa_pliku,kodowanie='utf-8'):
#     #print(f'kodowanie pliku={kodowanie}')
#     return [e.strip().split(';') for e in open(nazwa_pliku,encoding=kodowanie) if len(e.strip())>0]
#
#
# def drukuj(lista):
#     for e in lista:
#         print(e)

#dane=csv2list('dane.csv')
#drukuj(dane)
#drukuj(csv2list('dane.csv'))

#
# def oddaj():
#     return 'koza'
#
# def przyjmij(dane):
#     print(dane)
#
# x=oddaj()
# przyjmij(x)
# przyjmij(oddaj())


#przerwa do 14:36

# import funkcje
# print(funkcje.dodaj(4,5))
#import matplotlib.pyplot as plt
# import funkcje as fu
# print(fu.dodaj(4,5))

# from funkcje import dodaj
# print(dodaj(1,12))

# from funkcje import *
# print(dodaj(1,12))

# from funkcje import dodaj,odejmij
# print(dodaj(1,12))

# import biblioteki.funkcje
# print(biblioteki.funkcje.dodaj(6,7))

#import matplotlib.pyplot as plt
# import biblioteki.funkcje as bf
# print(bf.dodaj(6,7))

# from biblioteki.funkcje import  dodaj
# print(dodaj(66,77))

#import biblioteki.funkcje as bf

#39. Stwórz pakiet zawierający moduł który bedzie zawierał funkcję przyjmującą wzrost
# i masę a zwracającą bmi. Zaimportuj i wywołaj tę funkcję w taki sposób by przy jej
# wywołaniu nie trzeba było  podawać nazwy pakietu ani modułu.
#
# from pakiet.modul import  bmi
# print(bmi(67,1.76))

#
# import requests
# response=requests.get('http://jsystems.pl/Universe/samaTabelka.do')
# print(response.status_code)
# if response.status_code==200:
#     dane=[e for e in response.json() if "Python" in e['tytul_szkolenia']]
#     #print(dane)
#     for e in dane:
#         print(e['tytul_szkolenia'])

#40. z usługi sieciowej http://jsystems.pl/Universe/samaTabelka.do
# pobierz informację o szkoleniach.
# na konsoli wyswietl tytuly, miasta i daty wszystkich szkolen które w tytule mają malymi
# badz duzymi   literami "Python" i status terminu gwarantowanego (pole terminyGwarantowany=1)
