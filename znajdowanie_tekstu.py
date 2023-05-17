def znajdz_tekst(tekst, wzorzec, pozycja_startowa):
      dl1 = len(tekst)
      dl2 = len(wzorzec)
      print(dl1)
      print(dl2)
      for i in range (pozycja_startowa, dl1-dl2):
            print(i,pozycja_startowa, dl1-dl2)
            for j in range(dl2):
                  if tekst[i+j] != wzorzec[j]:
                        print(tekst[i+j],wzorzec[j])
                        print("break")
                        break
            if j == dl2:
                  print("j",j)
                  print("i",i)
                  return i
      return -1
                  
przeszukiwany_tekst = "matematayka"
wzor = "mat"
poz = 0
szukanie = znajdz_tekst(przeszukiwany_tekst,wzor,poz)


print(szukanie)
