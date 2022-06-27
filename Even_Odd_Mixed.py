n=int(input())
q=n
c=0
even=0
odd=0
while(q):
    r=q%10
    c=c+1
    if r%2==0:
        even=even+1
    else:
        odd=odd+1
    q=q//10
if even==c:
    print("Even")
elif odd==c:
    print("Odd")
else:
    print("Mixed")