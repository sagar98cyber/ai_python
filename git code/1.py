import numpy as np

one = np.array([[10,20]])
two = np.array([[15,25]])
print(one)
print(two, end="=B\n")

x = one+two
print(f'Addition:\n {x}')

x = one.T+two.T
print(f'Add: \n {x}')
#(a+b).T

x = one - two
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
one= np.array([[11,13],[7,3],[22,17]])
two = np.array([[4,10],[23,7],[9,15]])
print (one + two)

#identity matrix
IM2 = np.eye(2)
print(IM2, end=" =IM 2\n")
IM3 = np.eye(3)
print(IM3, end=" =IM 3\n")

#inverse matrix
one = ([[1,2,0],[0,1,2],[2,0,1]])
print (one, end=" =a\n\n")
print(np.linalg.inv(one), end=" =|a|")
