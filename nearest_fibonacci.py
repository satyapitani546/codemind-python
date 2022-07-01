f=[0]*100
f[1]=1
for i in range(2,100):
    f[i]=f[i-1]+f[i-2]
    
n=int(input())
for i in range(15):
    if n-i in f and n+i in f:
        print(n-i,n+i)
        break
    elif n-i in f:
        print(n-i)
        break
    elif n+i in f:
        print(n+i)
        break