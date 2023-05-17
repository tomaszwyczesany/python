tajny_numer = 777
print(
"""
+================================+
| Witaj w mojej grze, mugolu!    |
| Wprowadź liczbę całkowitą      |
| i zgadnij, jaki numer          |
| wybrałem dla ciebie.           |
| Jaki jest więc sekretny numer? |
+================================+
""")
liczba = int(input("Podaj liczbe "))

while liczba != 777:
    print("Nie, to nie jest ta liczba, którą wybrałem dla ciebie. Spróbuj ponownie!")
    liczba = int(input("Podaj liczbe "))
print("Dobra robota! To numer, który wybrałem dla ciebie! Jesteś teraz wolny.")
    
    

