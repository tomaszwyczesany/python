def cw1():
    lista = [1, 2, 5, 8, "ddddd", 'ggggg']
    lista.insert(0, 'poczatek')
    for el in lista:
        print(el)


def w1_cw1():
    potegi = []
    for number in range(1, 11):
        potegi.append(pow(2, number))
    # skladanie list
    for l in [pow(2, e) for e in range(1, 11)]: print(f'tt: {l}')
    for el in potegi:
        print(el)
    potegi2 = potegi  # referencja do tej samej listy
    potegi2.insert(2, 'fff')
    print(potegi)
    print(*potegi)  # rozpakowanie listy
    lista3 = [*[1, 3, 4], *['yy', 45]]
    print(lista3)


import random


def w2_cw1():
    list1 = []
    list2 = []
    for elm in range(1, 11):
        list1.append(random.randint(1, 10))
        list2.append(random.randint(1, 10))
    print(list1)
    print(list2)
    list3 = [*list1, *list2]
    print(list3)
    # to samo skladane razem
    print([*[random.randint(1, 10) for e in range(10)],
           *[random.randint(1, 10) for e in range(10)]]
          )


def w3_cw1():
    lista = []
    for el in range(1, 11):
        # pod_lista = [el, pow(2, el)]
        # lista.append(pod_lista)
        lista.append([el, pow(2, el)])
    print(lista)


def cw2():
    lista = [x * x for x in range(1, 11)]
    lista2 = [random.randint(1, 10) for e in range(1, 11)]
    lista3 = [x for x in range(1, 11) if x % 2 == 0]
    lista4 = [[x, pow(2, x)] for x in range(1, 11) if x % 2 == 0]
    print(lista)
    print(lista2)
    print(lista3)
    print(lista4)


def w1_cw2():
    lista = [pow(2, x) for x in range(1, 11)]
    print(lista)


import requests


def test1():
    odpowiedz = requests.get("http://jsystems.pl/static/blog/python/dane.json", auth=('user', 'pass'))
    print(odpowiedz.status_code)
    dane = odpowiedz.json()
    print(dane)


def w2_cw2():
    lista = [[e, pow(2, e)] for e in range(1, 11)]
    print(lista)


def w3_cw2():
    for linia in open('dane.csv', encoding='utf-8'):
        if len(linia.split()) > 0:
            lista = linia.strip().split(';')
            print(lista[1].upper(), lista[2].upper(), lista[3], lista[4])
    lista = [linia.strip().split(';') for linia in open('dane.csv', encoding='utf-8') if len(linia.strip()) > 0]
    print(lista)


def w4_cw2():
    # lista = [linia.strip().split(';') for linia in open('dane.csv', encoding='utf-8') if len(linia.strip()) > 0]
    # for x in lista:
    #     print(x)

    for x in [linia.strip().split(';')
              for linia in open('dane.csv', encoding='utf-8') if len(linia.strip()) > 0]:
        print(x)


def w5_cw2():
    for x in [linia.strip().split(';')
              for linia in open('dane.csv', encoding='utf-8') if len(linia.strip()) > 0]:
        bmi = round(float(x[4]) / pow(float(x[3]), 2), 2)
        print(f'Id: {x[0]} {x[1]} {x[2]} wzrost: {x[3]}m masa: {x[4]}kg BMI: {bmi}')
        l1 = [1, 3, 4, 5]
        # l2 = [*l1]  # kopiowanie listy
        l2 = l1.copy()  # tez kopiowanie listy
        l2.insert(2, 'ttt')
        print(l1, l2)


def w5_cw2():
    lista = [random.randint(1, 100) for x in range(10)]
    lista.sort()
    for x in lista: print(x)


from operator import itemgetter


def w6_cw2():
    lista = [x for x in [linia.strip().split(';')
                         for linia in open('dane.csv', encoding='utf-8') if len(linia.strip()) > 0]
             ]
    lista.sort(key=itemgetter(2))
    for e in lista: print(e)


def w7_cw2():
    lista = [[*x, round(float(x[4]) / pow(float(x[3]), 2), 2)]
             for x in [linia.strip().split(';')
                       for linia in open('dane.csv', encoding='utf-8')
                       if len(linia.strip()) > 0]
             ]
    lista.sort(key=itemgetter(5), reverse=True)
    for e in lista:
        print(e)


import os


def cw3():
    for w in os.walk('I:\\tools\\screemerRadio'):
        print(w)


def w1_cw3():
    katalog = 'I:\\tools\\szukane'
    fraza = input('Podaj fraze do szukania: ').lower()
    lista = [e for e in os.walk(katalog)]
    for elem in lista:
        for dirname in elem[1]:
            if fraza in dirname.lower():
                print(f'katalogi: {fraza} \tsciezka: {elem[0]} \tnazwa:{dirname}')
        for dirname in elem[2]:
            if fraza in dirname.lower():
                print(f'pliki: {fraza} \tsciezka: {elem[0]} \tnazwa:{dirname}')

    ######## KROTKI


def cw4():
    k1 = tuple([random.randint(1, 10) for x in range(10)])
    k2 = tuple([random.randint(11, 20) for x in range(10)])
    k3 = (*k1, *k2)
    for e in k3:
        print(e)


def w1_cw4():
    lista = [
        tuple(linia.strip().split(';'))
        for linia in open('dane.csv', encoding='utf-8') if len(linia.strip()) > 0
    ]
    print(lista)


import matplotlib.pyplot as plt


def w2_cw4():
    lista1 = [random.randint(1, 100) for e in range(20)]
    lista2 = [random.randint(1, 100) for e in range(20)]
    os_x = [e for e in range(1, 21)]
    print(lista1)
    print(lista2)
    plt.plot(lista1)
    plt.plot(lista2)
    # plt.savefig('wykres.png')
    plt.show()


def cw5():
    z1 = {2, 3, 5, 6, 9, 50}
    z2 = {2, 3, 5, 6, 9, 34, 8, 2, 9}

    print(z1.intersection(z2))
    print(z1.union(z2))
    print(z1.difference(z2))
    print(z2.difference(z1))


def w1_cw5():
    # s1 = set()
    # s2 = set()
    # for e in range(20):
    #     s1.add(random.randint(1, 40))
    #     s2.add(random.randint(1, 40))
    s1 = {random.randint(1, 40) for e in range(20)}
    s2 = {random.randint(1, 40) for e in range(20)}
    print(s1)
    print(s2)
    print('z1+z2: ', s1.union(s2))
    print('z1-z2: ', s1.difference(s2))
    print('z1 i z2: ', s1.intersection(s2))


def w2_cw5():
    # lista = [
    #     tuple(linia.strip().split(';'))
    #     for linia in open('dane.csv', encoding='utf-8') if len(linia.strip()) > 0
    # ]
    # s1 = set(lista)
    s1 = {
        tuple(linia.replace(',','.').strip().split(';'))
        for linia in open('dane.csv', encoding='utf-8') if len(linia.strip()) > 0
    }
    lista = list(s1)
    for s in lista:
        print(s)


# cw1()
# w1_cw1()
# w2_cw1()
# w3_cw1()
# cw2()
# w1_cw2()
# test1()
# w2_cw2()
# w3_cw2()
# w4_cw2()
# w5_cw2()
# w5_cw2()
# w6_cw2()
# w6_cw2()
# w7_cw2()
# cw3()
# w1_cw3()
# cw4()
# w1_cw4()
# w2_cw4()
# cw5()
# w1_cw5()
w2_cw5()
