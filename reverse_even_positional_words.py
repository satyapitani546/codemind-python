a=input()
b=list(a.split( ))
for i in range(0,len(b)):
    d=b[i]
    if i%2==0:
        c=''
        for j in range(len(d)-1,-1,-1):
            c+=d[j]
        print(c,end=' ')
    else:
        print(d,end=' ')