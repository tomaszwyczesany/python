# tutaj pisze
o1 = float(input("Podaj liczbe osob uwzglednionych w przepisie: "))
o2 = float(input("Podaj liczbe uczestnikow spotkania: "))
s1 = float(input("Podaj liczbe składników z przepisu: "))

s2 = (s1 * o2) / o1
print("Dla ", o2, " osób potrzeba ", s2, "składnika sałatki")
