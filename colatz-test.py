ile_liczb = int(input("Podaj ile liczb spr :"))
for k in range(ile_liczb,1,1):
      while k != 1:
            if k % 2 == 0:
                  k = k / 2
            else:
                  k = k * 3 + 1

      print("Ilość liczb = ", k)

            
