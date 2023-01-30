def cw1():
    # plik = open('output.csv', mode='w')
    # for x in range(1,11):
    #     plik.write(f'ala ma kota nr {x}\n')
    # plik.close()
    with open('output.csv', mode='w') as plik:
        for x in range(1, 11):
            plik.write(f'ala ma kota nr {x}\n')


def w1_cw1():
    s1 = {
        tuple(linia.replace(',', '.').strip().split(';'))
        for linia in open('dane.csv', encoding='utf-8') if len(linia.strip()) > 0
    }
    lista = list(s1)
    with open('output.csv', mode='w', encoding='utf-8') as plik:
        for x in lista:
            e = list(x)
            e.append(str(round(float(e[4]) / pow(float(e[3]), 2), 2)))
            print(';'.join(e))
            plik.write(';'.join(e) + '\n')


def cw2():
    dic1 = dict()
    for linia in open('ustawienia.csv', encoding='utf-8'):
        if len(linia.strip()) > 0:
            e = linia.strip().split(';')
            dic1[e[0]] = e[1]
    for key in dic1:
        print(f'{key}: {dic1[key]}')


def w1_cw2():
    dic1 = dict()
    for linia in open('dane.csv', encoding='utf-8'):
        linia = linia.replace(',', '.')
        if len(linia.strip()) > 0:
            e = linia.strip().split(';')
            dic1[' '.join([e[1], e[2]])] = tuple([e[0], e[3], e[4]])
    for key in dic1:
        print(f'{key}: {dic1[key]}')


def cw3():
    for x in range(-11, 11):
        try:
            print(1 / x)
        # except ZeroDivisionError:
        #     print('Dzielenie przez ZERO')
        except IOError:
            print('Error IO')
        except Exception as e:
            print(f'Inny error: {e}')


def w1_cw3():
    lista = [linia.strip().split(';') for linia in open('dane.csv', encoding='utf-8') if len(linia.strip()) > 0]
    with open('bledy.csv', encoding='utf-8', mode='a') as plik:
        for e in lista:
            # print(e)
            try:
                bmi = round(float(e[4]) / pow(float(e[3]), 2), 2)
                print(bmi)
                # print(';'.join(e))
            except Exception as ex:
                plik.write(';'.join(e) + ': ' + str(ex) + '\n')


# def c4():
#     def bmi(mass, height=2.0):
#         try:
#             return round(mass / pow(height, 2), 2)
#         except Exception as ex:
#             print(f'Blad BMI: {str(ex)}')
#             return -1
#
#     print(bmi(70, 1.89))


def w2_cw3():
    myList = fromFileCSVToList(filename='dane.csv')
    showList(myList)


def fromFileCSVToList(filename, encoding='utf-8'):
    return [linia.strip().split(';')
            for linia in open(filename, encoding=encoding) if len(linia.strip()) > 0]


def showList(list):
    for e in list:
        print(e)


# import biblioteki.funkcje as lib1
# from biblioteki.funkcje import bmi


# def c4():
#     print(bmi(56, 2))

import requests


def get_dane(url="http://jsystems.pl/Universe/samaTabelka.do"):
    response = requests.get(url)
    print(response.status_code)
    if response.status_code == 200:
        return [e for e in response.json()]
    else:
        return []


def c5():
    dane = get_dane()
    for e in dane:
        if 'python' in e['tytul_szkolenia'].lower() and e['terminyGwarantowany'] == 1:
            print(f" tytuł: {e['tytul_szkolenia']} miasto: {e['miasto']} termin: {e['termin']} {e['terminyGwarantowany']}")


# cw1()
# w1_cw1()
# cw2()
# w1_cw2()
# cw3()
# w1_cw3()
# c4()
# w2_cw3()
# c4()
c5()
