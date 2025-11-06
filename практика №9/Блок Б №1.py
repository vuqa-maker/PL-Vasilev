def m():
    n=int(input())
    if n==0:
        return 0
    else:
        max_n=m()
        return max(n,max_n)
print(m())
