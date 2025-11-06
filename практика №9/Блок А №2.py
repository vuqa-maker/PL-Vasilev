def d(a,b):
    return d(a-b,b) if a>=b else a
a=int(input())
b=int(input())
print(d(a,b))
