n=int(input())
a=list(map(int,input().split()))
for i in range(0,n):
    if a[i]!=0:
        print(a[i],end=' ')
for i in range(0,n):
    if a[i]==0:
        print(a[i],end=' ')