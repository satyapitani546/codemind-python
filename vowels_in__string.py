n=input()
b=[]
for i in n:
    if i in 'aeiouAEIOU' and i not in b:
        b.append(i)
c=''.join(b)
print(*c)
        