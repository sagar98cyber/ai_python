names = ['Sagar','Ross','Rachel','Joey','Monica','Phoebe']
print(names[2])
print(names[-2])
print(names[2:])
#value of fourth item or the upper index is not returned
print(names[2:4])
print(names[2:5])

names[0] = 'Chandler'
print(names)


#find the largest number in the list
limit = int(input('Enter the limit of list of numbers to be added: '))
print(limit)
numbers_list = []
items = 0

for items in range(0,limit):
    print(items)
    numbers_list.append(int(input('Enter the number to be saved in the list: ')))
    items+=1

print(f'The entered list is: {numbers_list}')
largest = numbers_list[0]

for item in numbers_list:
    if item>largest:
        largest = item
    
print(f'Largest number in the list: {largest}')



matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix[0][0])

matrix[0][2] =30

print(matrix)

for row in matrix:
    for item in row:
        print(item)


# PROGRAM TO REMOVE DUPLICATES FROM THE LIST
list_values = []
limit = int(input(f'Enter the number of items you want to enter in the list: '))
uniques = []
count=0

while count < limit:
    list_values.append(int(input(f'Enter the item to be entered: ')))
    count+=1

for value in list_values:
    if value not in uniques:
        uniques.append(value) 

print(f'After removing the values from the list: {uniques}')
