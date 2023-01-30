# program palindrom
# wersja z funkcją reversed
palindrom = input("podaj słowo do sprawdzenia")
test = ''.join(reversed(palindrom))
if(palindrom == test):
    print("Podane słowo jest Palindromem")
else:
    print("Podane słowo NIE jest Palindromem" )