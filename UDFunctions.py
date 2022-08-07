def evenOdd( x ):
	if (x % 2 == 0):
		print("even")
	else:
		print("odd")

# Driver code
evenOdd(2)
evenOdd(3)


def myFun(x, y = 50):
	print("x: ", x)
	print("y: ", y)

myFun(10)


def myFun1(*argv):
	for arg in argv:
		print (arg)

def myFun2(**kwargs):
	for key, value in kwargs.items():
		print ("% s == % s" %(key, value))

# Driver code
print("Result of * args: ")
myFun1('Hello', 'Welcome', 'to', 'NFSU')

print("\nResult of **kwargs")
myFun2(first ='N', mid ='FS', last ='U')
