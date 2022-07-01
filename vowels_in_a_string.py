a=input()
b=input()
c=0
for i in a:
    if i==b:
        c+=1
        ind=a.index(i)
        break
if c==1:
    print('True')
    print(ind)
else:
    print('False')