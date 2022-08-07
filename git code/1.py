import numpy as np


a = np.array([[10,20]])
b = np.array([[15,25]])
print(a)
print(b, end="=B\n")

x = a+b
print(f'Addition:\n {x}')

x = a.T+b.T
print(f'Add: \n {x}')
#(a+b).T

x = a - b
print(f'Substraction: \n {x}')

#scalar
s = 5
n = np.array([[5,7]])
x = s * n
print(f'Scalar: \n {x}')

#matrix multiplication
n = np.array([[11,15]])
m = np.array([[4,2]])
x = n * m
print(f'multiplication: \n {x}')
#np.dot(n,m)

#matrix scalar multiplication

#matrix sum
a= np.array([[11,13],[7,3],[22,17]])
b = np.array([[4,10],[23,7],[9,15]])
print (a + b)


#identity matrix
IM2 = np.eye(2)
print(IM2, end=" =IM 2\n")
IM3 = np.eye(3)
print(IM3, end=" =IM 3\n")

#inverse matrix
a = ([[1,2,0],[0,1,2],[2,0,1]])
print (a, end=" =a\n\n")
print(np.linalg.inv(a), end=" =|a|")
