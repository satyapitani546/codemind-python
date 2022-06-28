def most_frequent(a):
    c=0
    n=a[0]
    for i in a:
        cur_frequency=a.count(i)
        if(cur_frequency>c):
            c=cur_frequency
            n=i
    return n
n=int(input())
a=list(map(int,input().split()))
print(most_frequent(a))