import psycopg2 as pg


# bazy danych -- postgres

def cw1():
    connection = pg.connect(host="localhost", port=5432, database='apka', user='aplikacja', password='postgres')
    cursor = connection.cursor()
    query = 'select * from produkty'
    cursor.execute(query)
    for w in cursor:
        print(f'{w[1]},{w[2]},{w[3]}')


def getFromDb2CSV(filename='wynik.csv'):
    with pg.connect(host="localhost", port=5432, database='apka', user='aplikacja', password='postgres') as connection:
        cursor = connection.cursor()
        query = 'select * from produkty'
        cursor.execute(query)
        with open(filename, encoding='utf-8', mode='w') as file:
            for w in cursor:
                # li=[str(e) for e in w]
                # file.write(f'{w[0]};{w[1]};{w[2]};{w[3]}\n')
                # file.write(';'.join(li)+'\n')
                file.write(';'.join(str(e) for e in w) + '\n')


def w1_cw1():
    getFromDb2CSV('wynik.csv')


def fromFileCSVToList(filename, encoding='utf-8'):
    return [linia.strip().replace(',', '.').split(';')
            for linia in open(filename, encoding=encoding) if len(linia.strip()) > 0]


def w2_cw1():
    with pg.connect(host="localhost", port=5432, database='apka', user='aplikacja', password='postgres') as connection:
        cursor = connection.cursor()
        query = 'select max(id_produktu) from produkty'
        cursor.execute(query)
        for w in cursor:
            print(w[0])


def w3_cw2():
    lista = fromFileCSVToList('dane.csv')
    # print(lista)
    with pg.connect(host="localhost", port=5432, database='apka', user='aplikacja', password='postgres') as connection:
        cursor = connection.cursor()
        for e in lista:
            try:
                dane = [f"'{str(elem)}'" for elem in e]
                query = f"INSERT INTO zawodnicy VALUES({','.join(dane)})"
                # print(query)
                query2 = f"INSERT INTO zawodnicy VALUES({e[0]},'{e[1]}','{e[2]}',{e[3]},{e[4]})"
                cursor.execute(query2)
            except Exception as ex:
                print(str(ex))

        connection.commit()


class Samochod:
    # marka = None
    # model = None
    # rejestracja = None
    def __init__(self, marka=None, model=None, rejestracja='111111'):
        self.marka = marka
        self.model = model
        self.rejestracja = rejestracja

    def ustaw(self, marka=None, model=None, rejestracja='111111'):
        self.marka = marka
        self.model = model
        self.rejestracja = rejestracja

    def wyswietl(self) -> None:
        print(f'marka: {self.marka} model: {self.model} rejestracja: {self.rejestracja}')

    def __str__(self) -> str:
        return f'from toString() -> marka: {self.marka} model: {self.model} rejestracja: {self.rejestracja}'


def cw2():
    s1 = Samochod("marka1", "model1", "rejestracja1")
    s2 = Samochod(model='elo')
    s3 = Samochod()
    s3.ustaw(model='hhh', marka='rrrrr', rejestracja='ttttt')
    s1.wyswietl()
    s2.wyswietl()
    print(s1)
    print(s3)
    help(Samochod)
    help(list)


class Zawodnik:
    def __init__(self, id=-1, imie='noname', nazwisko='noname', wzrost=1, masa=100):
        self.id = id
        self.imie = imie
        self.nazwisko = nazwisko
        self.wzrost = wzrost
        self.masa = masa

    def toCSVLine(self, znak=';') -> str:
        return f'{self.id}{znak}{self.imie}{znak}{self.nazwisko}{znak}{self.wzrost}{znak}{self.masa}'

    def get_bmi(self):
        return round(self.masa / pow(self.wzrost, 2), 2)

    def __str__(self) -> str:
        return f'id: {self.id} imie: {self.imie} nazwisko: {self.nazwisko} wzrost: {self.wzrost} masa: {self.masa}'


def getAllFromTable():
    dane = []
    with pg.connect(host="localhost", port=5432, database='apka', user='aplikacja', password='postgres') as connection:
        cursor = connection.cursor()
        query = 'SELECT * FROM zawodnicy'
        cursor.execute(query)
        for c in cursor:
            dane.append(Zawodnik(c[0], c[1], c[2], c[3], c[4]))
        # for d in dane:
        #     print(d.get_bmi())
    return dane


def fromFileCSVToZawodnikList(filename='dane.csv', encoding='utf-8'):
    lista = [linia.strip().replace(',', '.').split(';')
             for linia in open(filename, encoding=encoding) if len(linia.strip()) > 0]
    return [Zawodnik(z[0], z[1], z[2], z[3], z[4]) for z in lista]


def w1_cw2():
    dane = getAllFromTable()
    for d in dane:
        print(f'BMI: {d.get_bmi()} dla zawodnika {d}')
        print(f'BMI: {d.get_bmi()} dla zawodnika {d.__dict__}')
    # print(dane[0].__dict__)


def w2_cw2():
    lista = fromFileCSVToZawodnikList()
    for z in lista:
        print(z)


# cw1()
# w1_cw1()
# w2_cw1()
# w3_cw2()
# cw2()
# getAllFromTable()
# w1_cw2()
w2_cw2()