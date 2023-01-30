def czy_pierwsza(n):
    pierw = int(n ** 0.5) + 1
    print("pierw : ",n)
    for dzielnik in range(3, pierw, 2):
        if n % dzielnik == 0:
            print("dziel f : ",n)
            return False
    print("dziel p : ",n)
    return True

for i in range(1, 20):
	if czy_pierwsza(i + 1):
			print(i + 1)
print()
