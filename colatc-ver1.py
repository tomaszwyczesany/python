c0 = int(input("Podaj wartość c0: "))
a = 0
if c0 > 1:
    while c0 > 1:
        if c0 % 2 == 0:
            c0 = c0 / 2
            print(c0)
            a = a + 1
        elif c0 % 2 != 0:
            c0 = 3 * c0 + 1
            print(c0)
            a = a + 1
        if c0 == 1:
            break
print("Liczba krokow: ", a)