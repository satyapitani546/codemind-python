def sum(n):
    re=0
    while(n):
        r=n%10;
        re=re+r;
        n=n//10;
    return re;
n=int(input())
while n>9:
    n=sum(n)
print(n)