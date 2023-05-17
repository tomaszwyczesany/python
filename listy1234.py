moja_lista = [1, 2, 3, 4, 5]
wycinek_pierwszy = moja_lista[2: ]
wycinek_drugi = moja_lista[ :2]
wycinek_trzeci = moja_lista[-2: ]

print(wycinek_pierwszy) # daje na wyjściu: [3, 4, 5]
print(wycinek_drugi) # daje na wyjściu: [1, 2]
print(wycinek_trzeci) # daje na wyjściu: [4, 5]
