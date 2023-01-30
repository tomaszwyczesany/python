print("LOTHAR COLAZ HYPOTESIS")
c0 = int(input("Give me the number"))
i = 0
while c0 != 1:
    i += 1
    if c0 % 2 == 0:
        c0 = c0 / 2
        print(c0)
    else:
        c0 = 3 * c0 + 1
        print(c0)
print("steps",i)
# 25 := steps 23
# 26 := steps 10
# 27 := steps 111
