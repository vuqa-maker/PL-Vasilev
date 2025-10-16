import math
def s(a,b):
    s=a*b
    return s
A=[]
for i in range(3):
    print('введите стороны',i,'-го прямоугольника:')
    a=int(input('a:'))
    b=int(input('b:'))
    A.append(s(a,b))
for i in range(3):    
    print('площадь',i,'-го прямоугольника: {:.2f}'.format(A[i]))

    
