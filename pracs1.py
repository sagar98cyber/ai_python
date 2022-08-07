separator1 = ' ' 

str1 = '    Mr. Sagar     '
str2 = 'Shah'

index1 = str1.index('g')
print(f'The String was found at the index of {index1}')

strip1 = str1.strip()
print(f'The stripped version of the string is as follows: {strip1}')

count1 = str1.count('a')
print(f'The count of the specific string is: {count1}')

split1 = str1.split(' ')
print(f'The result after the split is : {split1}')

upper1 = str1.strip().upper()
print(f'The result after the upper is: {upper1}')

lower1 = str1.strip().lower()
print(f'The result after the upper is: {lower1}')

isUpper1 = str1.isupper()
print(f'The given string is upper: {isUpper1}')

isLower1 = lower1.islower()
print(f'The given string is upper: {isLower1}')

#trans1 = str1.translate()
#print(f'The translated string is as follows: {trans1}')

mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

find1 = str1.find('a')
print(f'The output of the find function is: {find1}')

center1 = str1.center(20,'O')
print(f'The output of the center function is: {center1}')

myTuple = ("John", "Peter", "Vicky")
#x = "#".join(myTuple)
x = separator1.join(myTuple)
print(x)
x = separator1
x= separator1.join(str2)
print(x)