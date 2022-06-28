n=int(input())
for i in range(n):
    m=int(input())
    ar=list(map(int,input().split()))
    for a in range(1,m+1):
        if a not in ar:
            print(a)