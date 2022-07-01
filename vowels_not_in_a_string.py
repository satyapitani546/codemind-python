a=input()
l=[0,0,0,0,0]
b='aeiou'
n=0
for i in a:
    if i in 'aeiou':
        if i=='a':
            l[n]+=1
        elif i=='e':
            l[n+1]+=1
        elif i=='i':
            l[n+2]+=1
        elif i=='o':
            l[n+3]+=1
        else:
            l[n+4]+=1
count=0
for i in range(0,5):
    if l[i]==0:
        for j in range(0,5):
            if i==j:
                count+=1
                print(b[i],end=' ')
if count==0:
    print('0')