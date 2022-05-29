n=int(input())
sum=0
pro=1
while n>0:
    rem=n%10
    sum+=rem
    pro*=rem
    n=n//10
min=pro-sum
print(min)