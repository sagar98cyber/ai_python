import pandas as pd
import matplotlib.pyplot as plt 

income = []
loan = []
intIncome = []
intLoa = []
count = 1

def splitFunction(parsedString):                #function to split the string and apppend to the list
    myList = parsedString.split(',')
    if myList[6] == "" or myList[6] == '' or myList[6] == ' ':
        income.append(0)
    else:
        income.append(int(myList[6]))
    if myList[8] == "" or myList[8] == '' or myList[8] == ' ':
        loan.append(0)
    else:
        loan.append(int(myList[8]))
    

with open('test.csv',buffering=200000) as f:
    if count <= 100:
        for line in f:
            splitFunction(line)
            count +=count

print(type(loan[0]))