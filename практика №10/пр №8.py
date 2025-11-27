with open('ВСС_УБ-51_vvod.txt', 'r') as file:
    l = file.readlines()
A = []
for line in l:
    row = list(map(int, line.strip().split()))
    A.append(row)
n = len(A)  
for i in range(n):
    temp = A[i][0]
    A[i][0] = A[i][n-1]
    A[i][n-1] = temp
with open('ВСС_УБ-51_vivod.txt', 'w') as file:
    for i in range(n):
        for j in range(n):
            file.write(str(A[i][j]) + ' ')
        file.write('\n')
print("Исходная матрица:")
with open('ВСС_УБ-51_vvod.txt', 'r') as file:
    print(file.read())
print("Матрица после перестановки столбцов:")
for i in range(n):
    for j in range(n):
        print(A[i][j], end=' ')
    print()
