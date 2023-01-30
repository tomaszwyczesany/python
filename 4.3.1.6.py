def czy_przestepny(rok):
    if (rok % 4 == 0 and rok % 100 != 0)or rok % 400 == 0:
        return True
    else:
        return False
dane_testowe = [1900, 2000, 2016, 1987]
wyniki_testow = [False, True, True, False]
for i in range(len(dane_testowe)):
	r = dane_testowe[i]
	print(r,"->",end="")
	wynik = czy_przestepny(r)
	if wynik == wyniki_testow[i]:
		print("OK")
	else:
		print("Nie powiodło się")
