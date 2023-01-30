import random
# https://blog.jsystems.pl/

def cw1():
    print('hello')
    print("hello hh")
    pi = 3.14
    r = 1
    print('Pole kola: ' + str(pi * r * r))
    print('Pole kola: {}'.format(pi * r * r))
    x = input('Podaj x: ')
    y = input('Podaj y: ')
    print('{} + {} = {}'.format(x, y, x + y))
    print(type(x), type(y), type(3.5))
    print(f"x = {x}")
    imie = input('Podaj imie: ')
    nazwisko = input('Podaj imie: ')
    print(f"Witaj {imie} {nazwisko}")
    a = float(input('podaj a: '))
    b = float(input('podaj b: '))
    wynik = round(a / b, 2)
    print(wynik)


def cw2():
    masa = float(input('Podaj mase ciala w kg: '))
    wzrost = float(input('Podaj wzrost w metrach: '))
    bmi = round(masa / (wzrost * wzrost), 2)
    if bmi < 16:
        print(f'BMI: {bmi} wyglodzenie')
    elif bmi < 17:
        print(f'BMI: {bmi} wychudzenie')
    elif bmi < 18.5:
        print(f'BMI: {bmi} niedowaga')
    elif bmi < 25:
        print(f'BMI: {bmi} norma')
    elif bmi < 30:
        print(f'BMI: {bmi} nadwaga')
    else:
        print(f'BMI: {bmi} otylosc')
    # if -1:
    #     print("ok")
    # else:
    #     print('noko')


def cw3():
    x = -3
    if x == 1:
        print('x jest rowne 1')
    elif x > 1:
        print('wiekszy od 1')
    else:
        print('Jednak x jest mniejszy od 1')
    print('koniec')


def cw4():
    a = float(input('podaj a: '))
    if a > 0:
        print(f'liczba {a} jest dodatnia')
    elif a == 0:
        print(f'liczba {a} jest rowna zero')
    else:
        print(f'liczba {a} jest ujemna')


def cw5():
    result = 1
    list = []
    for x in range(1, 21):
        print(f'2^{x} = {pow(2, x)}')
        list.append(pow(2, x))
    print(list)
    for i in range(1, 101):
        if i % 2 == 0:
            print(f'liczba {i} jest parzysta')
        else:
            print(f'liczba {i} jest nieparzysta')


def cw6():
    kwota = float(input('podaj kwote: '))
    oprocentowanie = float(input('podaj oprocentowanie roczne: '))
    ilMiesiecy = int(input('podaj ilosc miesiecy: '))
    kapital = kwota
    for m in range(1, ilMiesiecy + 1):
        odsetki = (kapital * (oprocentowanie / 12))
        kapital = kapital + odsetki
        print(f'miesiac: {m} kapital: {round(kapital, 2)} odsetki: {round(odsetki, 2)}')


def cw7():
    limit = int(input('Podaj granice: '))
    result = 0
    count = 1
    while result < limit:
        result = pow(2, count)
        count = count + 1
        print(f'2^{count} = {result}')


def cw8(randRange=10):
    sumLimit = int(input('podaj granice: '))
    sum = 0
    while sum < sumLimit:
        x = random.randint(1, randRange)
        sum += x
        dd = ' + ' if sum < sumLimit else ' = '
        print(f'{x}', end=dd)
        # print(f'x = {x} sum = {sum}')
    print(sum)


def cw9():
    text = input('podaj tekst: ')
    chars = '.,?!'
    # text = text.replace('.', '').replace(',', '').replace('!', '').replace('?', '').upper()
    # text = text.replace(('.',',','!','?'),'').upper()
    for c in chars:
        text = text.replace(c, '')

    print(text.upper())


def cw10():
    for line in open('dane.csv', encoding='utf-8'):
        print(line.strip(), '|', len(line.strip()))


def cw11():
    filename = input('Podaj nazwe pliku: ')
    for line in open(filename, encoding='utf-8'):
        if len(line.strip()) > 0:
            print(line.strip())


def cw12():
    char = input('Jakiego zanku szukac: ')
    filename = input('Podaj nazwe pliku: ')
    text = open(filename, encoding='utf-8').read()
    count = 0
    # for c in text.lower():
    #     if char.lower() == c:
    #         count = count + 1
    # print(f'znak {char} wystepuje {count} razy')
    print(f'znak {char} wystepuje: {text.lower().count(char.lower())}')


def cw13():
    char = input('Jakiego zanku szukac: ').lower()
    filename = input('Podaj nazwe pliku: ')
    nr = 0
    count = 0
    for line in open(filename, encoding='utf-8'):
        nr = nr + 1
        # if char.lower() in line.lower():
        ile = line.lower().count(char)
        if ile > 0:
            # print(f'Znaleziono tekst {char} w linii: {nr} razy: {ile}')
            print(nr, line.strip())
            count = count + ile
    print(f'ilosc wystapien: {count}')


# cw1()
# cw2()
# cw3()
# cw4()
# cw5()
# cw6()
# cw7()
# cw8(20)
# cw9()
# cw10()
# cw11()
# cw12()
cw13()
