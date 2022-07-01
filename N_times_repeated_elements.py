n=int(input())
a=list(map(int,input().split()))
b=int(input())
c=[]
for i in a:
    if a.count(i)==b:
        if i not in c:
            c.append(i)
if len(c)==0:
   print('-1')
else:
    print(*c)