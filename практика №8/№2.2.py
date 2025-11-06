n=3
m=4
A=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
for i in range(n):
    x=A[i][0]
    A[i][0]=A[i][m-1]
    A[i][m-1]=x
for i in range(n):
    for j in range(m):
        print(A[i][j], end=' ')
    print()
        
