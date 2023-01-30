#Kosmiczny mecz zadanie 1
# matura informatyka Grudzień 2022
plik = open('mecz.txt')
we = plik.read().strip()
#print(len(we))
plik.close()
#ZADANIE 1.1
ile=0
for i in range(1,len(we)):
    if we[i]!=we[i-1]:
        ile+=1
print(ile)
#ZADANIE 1.2
la=0
lb=0
for i in range(len(we)):
    if we[i]=='A':
        la+=1
    else:
        lb+=1
    if (la >= 1000 or lb >= 1000) and abs(lb-la)>=3:
        break
print('Druzyna A',la,lb,'B')
#zadania 1.3
passa_a=0
passa_b=0
tA=[]
tB=[]
for i in we:
    if i =='A':
        if passa_b>=10:
            tB.append(passa_b)
        passa_b = 0
        passa_a += 1
    else:
        if passa_a>=10:
            tA.append(passa_a)
        passa_a = 0
        passa_b += 1
print('Passy A ',len(tA),'B :',len(tB),'suma:',len(tA)+len(tB))
print('max A :', max(tA),'max B :', max(tB))
#komentarz