n=int(input())
a=list(map(int,input().split()))
b=int(input())
for i in range(0,n):
    if a[i]==b:
        print(i)
        break
else:
    print('-1')