n=int(input())
s=n*n
sum=0
while s!=0:
    rem=s%10
    sum+=rem
    s=s//10
if sum==n:
    print("Neon Number")
else:
    print("Not Neon Number")