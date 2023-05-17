n = int(input("Podaj ile chcesz miesiecy oszczedzan na iphona ?"))
suma = 0
for i in range(1,n+1):
    a = int(input("Podaj kwote "))
    suma = suma + a

print("Suma ",n,"wpłat  to :", suma) 
