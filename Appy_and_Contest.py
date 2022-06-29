a=int(input())
for i in range(a):
    n,x,y,m=map(int,input().split())
    c1=((n-x)//x)+1
    c2=((n-y)//y)+1
    c3=((n-(x-y))//(x*y))+1
    if(c1+c2-c3>m):
        print("Win")
    else:
        print("Lose")