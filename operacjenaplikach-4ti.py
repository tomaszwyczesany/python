def cw1():
    # plik = open('output.csv', mode='w')
    # for x in range(1,11):
    #     plik.write(f'ala ma kota nr {x}\n')
    # plik.close()
    with open('output.csv', mode='w') as plik:
        for x in range(1, 11):
            plik.write(f'ala ma kota nr {x}\n')

def cw2():
    with open('mecz.txt', mode='r') as plik:
        we = plik.read().strip()
        print(len(we))
        plik.close()

cw1()
cw2()
