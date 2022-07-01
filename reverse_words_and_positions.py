a=input()
b=list(a.split( ))
for i in range(0,len(b)):
    c=''
    a=b[i]
    for j in range(len(a)-1,-1,-1):
        c+=a[j]
    b[i]=c
d=[]
for i in range(len(b)-1,-1,-1):
    d.append(b[i])
print(*d)