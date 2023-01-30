wyraz = input("Podaj wyraz: ")

for i in range(len(wyraz)):
    if wyraz[i] == "a":
        wyraz = wyraz[:i] + "b" + wyraz[i+1:]
print("Wyraz po przetworzeniu : ", wyraz)