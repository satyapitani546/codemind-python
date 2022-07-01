import math
n=int(input())
s=0
dc=0
temp=n
while(temp):
    temp=temp//10
    dc+=1
temp=n
while(temp):
    d=temp%10
    s=s+pow(d,dc)
    temp=temp//10
    dc-=1
if(s==n):
    print("True")
else:
    print("False")