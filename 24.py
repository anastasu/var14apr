
f = open('24-2.txt')
s = f.readline()
k, m = 1, 1
for i in range(len(s)-1):
    if s[i]=='P' and s[i+1]=='P':
        k=1
    else:
        k += 1
        m=max(m, k)
print(m)