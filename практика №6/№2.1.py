import random
a = [random.randint(-20, 20) for i in range(10)]
print(a)
print(min(a))
print(a.index(min(a)))
