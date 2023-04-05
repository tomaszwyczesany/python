N=5
a = [0] * N
def wprowdz_dane():
    for i in range(N):
        a[i] = int(input("Podaj liczbe :"))
def wyprowdz_dane():
    for i in range(N):
        print("a[",i,"] =",a[i])
wprowdz_dane()
wyprowdz_dane()
print("element pierwszy,[a0] tablicy",a[0])
print("element ostatni,[a4] tablicy",a[4])
if a[0] > a[1]:
    print("element pierwszy jest wiekszy od drugiego")
else:
    print("element drugi jest wiekszy od pierwszego")
if a[0] == a[1]:
    print("elemty sa równe")


input("\n nacisnij dowolny klawsz  lub Enter")