#mutiplication table for +ve int
n=int(input())
if(n<=0):
    ptint("Invalid")
else:
    i=1
    while(i<=10):
        print("{} * {} = {}". format(n,i, n*i))
        i=i+1
