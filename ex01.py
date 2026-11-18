n=int(input())
out=''
while n>=8:
    out=str(n%8)+out
    n=n//8
out=str(n)+out
print(out)