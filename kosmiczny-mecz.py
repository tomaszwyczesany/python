plik = open('mecz.txt')
we = plik.read().strip()
print(len(we))
plik.close()
#----zadanie 1.1
ile = 0
for i in range(1,len(we)):
    if we[i] != we[i - 1]:
        ile += 1
print(ile)
#-----zadanie 1.2
la = 0
lb = 0
for i in range(len(we)):
    if we[i]=='A':
        la+=1
    else:
        lb+=1
    if (la >= 1000 or lb >= 1000) and abs(lb - la) >= 3:
        break
print('Druzyna A',la)
print('Druzyna B',lb)
#-----zadanie 1.3
