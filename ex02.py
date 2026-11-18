n=int(input())
out=0
i=0
while n>0:
    out+=(n%10)*4**i
    i+=1
    n//=10
print(out)