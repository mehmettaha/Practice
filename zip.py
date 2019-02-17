A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1 = range(10)

A2 = sorted([i for i in A1 if i in A0])


A5 = {i:i*i for i in A1}
print(A5)