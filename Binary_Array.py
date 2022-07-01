n=int(input())
a=list(map(int,input().split()))
s=0
for i in a:
    if i!=0 and i!=1:
        s=1
        break
if s==0:
    print('True')
else:
    print('False')