x = 6* 343 ** 5 + 5*49**7 -50
k=0
while x>0:
    if x % 7 == 6: k=k+1
    x = x//7
print (k)