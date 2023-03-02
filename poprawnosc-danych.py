# try:
#     x = int(input())
#     print("To liczba",x)
# except ValueError:
#     print("To nie liczba, nie liczba całkowita")
while True:
  val = input("Enter a number")
  if val.isdigit():
    val = int(val)
    break
  else:
    print("Can't read a number, try again.")