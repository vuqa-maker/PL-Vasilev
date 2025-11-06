n=3
A=[]
for i in range(n):
    B=[]
    for i in range(n):
        B.append(int(input()))
    A.append(B)
for i in range(n):
    for j in range(n):
        print(A[i][j], end=' ')
    print()
s=0
for j in range(n):
    s+=A[0][j]
b='является магическим'
for i in range(n):
    s1=0
    s2=0
    for j in range(n):
        s1+=A[i][j]
        s2+=A[j][i]
    if s1 !=s or s2 !=s:
        b='не является магическим'
        break
print(b)
