def f(n):
    if n>0:
        f(n//3)
        f(n-3)
        print(n)

print (f(9))