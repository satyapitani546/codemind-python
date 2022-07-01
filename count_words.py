a=input()
b=list(a.split( ))
c=0
for i in range(0,len(b)):
    d=b[i]
    if d[0] in 'aeiouAEIOU' and d[len(d)-1] in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
        c+=1
print(c)