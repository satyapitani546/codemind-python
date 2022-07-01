n=int(input())
a=list(map(int,input().split()))
s=0
for i in a:
    s=s+i*(2**(n-1))
    n-=1
print(s)