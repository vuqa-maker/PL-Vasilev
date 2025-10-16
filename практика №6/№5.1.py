import random
a = [-3,-5,1,2,3,5,-7,-8]
print(a)
for i in range(len(a)-1):
    if a[i]<0 and a[i+1]<0:
        print(a[i],a[i+1])
