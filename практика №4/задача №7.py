n=int(input())
s=0
f=1
for i in range(1,n+1):
    x=i*f
    s=s+x
    f=x
print(s)
