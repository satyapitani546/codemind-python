n=int(input())
a=list(map(int,input().split()))
c,d=map(int,input().split())
count=0
for i in a:
    if i<c or i>d:
        print(i,end=' ')
        count+=1
if count==0:
    print('-1')