n=int(input())
a=list(map(int,input().split()))
l=0
for i in a:
    c=0
    m=i
    while m:
        m=m//10
        c+=1
    if c>l:
        l=c
count=0
for i in a:
    c=0
    m=i
    while m:
        m=m//10
        c+=1
    if c==l:
        count+=1
print(count)