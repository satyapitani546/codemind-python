n=input()
c=0
s=0
for i in n:
    if i=='z':
        c+=1
    else:
        s+=1
if c*2==s:
    print("Yes")
else:
    print("No")