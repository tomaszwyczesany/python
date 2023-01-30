#program palindrom wesja z pętlą for
palindrom = input("podaj słowo do sprawdzenia")
test = ""
for i in palindrom:
    # print(test)
    test = i + test
# print(test)
if (palindrom == test):
    print("podane słowo jest palindromem")
else:
    print("podane slowo nie jest palindromem")
