moja_lista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
nowa = []

for i in moja_lista:
  if i not in nowa:
    nowa.append(i)
    print(nowa)
    
print(moja_lista)
print("Lista tylko z unikalnymi elementami:")
print(nowa)
