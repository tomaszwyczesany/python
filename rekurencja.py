def fun(a):
    if a > 30:
        print(a)
        return 3
    else:
        print(a,"rek")
        return a + fun(a + 3)
        
print(fun(25))
