n=int(input())
f=1
s=0
t=n
while(n):
    r=n%10
    for i in range(1,r+1):
        f=f*i
    s=s+f
    f=1
    n=n//10
n=t
if(n==s):
    print("The number %d is a strong number"%n)
else:
    print("The number %d is not a strong number"%n)