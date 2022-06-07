n=int(input())
rev=0
org=0
s=n*n
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
rs=rev*rev
while rs>0:
    r=rs%10
    org=org*10+r
    rs=rs//10
if(s==org):
    print("True")
else:
    print("False")