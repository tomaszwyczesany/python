with open("liczby.txt") as f:
    lines = f.read().splitlines()

powers = set()
for i in range(0,11):
    powers.add(3**i)
   # print(powers)
counter = 0

for ln in lines:
    if not ln:
        continue
    num = int(ln)
    if num in powers:
        counter += 1
print(counter)