import pandas as pd
import matplotlib.pyplot as plt 

income = []
loan = []
zeroThousand = []
thousand2Thousand = []
twoThousand3Thousand = []
threeThousand4Thou = []
fourThousand5Thousand = []
fiveThousand6Thousand = []
six7Thousand = []
seven8Thousand = []
eight9Thousand = []
nine10Thousan= []
ten15Thous = []

def listLoanAmount(list,amount):
    count = 0
    for i in list:
        j = i[1] + thresholdValue
        if amount <= j :
            count = count +1
    print(f'The count is: {count}')
    result = count/len(list)
    print(f'The result is: {result}')
    return result

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
    for line in f:
            splitFunction(line)

for i in range(0,len(income)):
    if income[i] <= 1000:
        zeroThousand.append((income[i],loan[i]))
    elif income[i] > 1000 and income[i]<=2000:
        thousand2Thousand.append((income[i],loan[i]))
    elif income[i] > 2000 and income[i]<=3000:
        twoThousand3Thousand.append((income[i],loan[i]))
    elif income[i] > 3000 and income[i]<=4000:
        threeThousand4Thou.append((income[i],loan[i]))
    elif income[i] > 4000 and income[i]<=5000:
        fourThousand5Thousand.append((income[i],loan[i]))        
    elif income[i] > 5000 and income[i]<=6000:
        fiveThousand6Thousand.append((income[i],loan[i]))                
    elif income[i] > 6000 and income[i]<=7000:
        six7Thousand.append((income[i],loan[i]))         
    elif income[i] > 7000 and income[i]<=8000:
        seven8Thousand.append((income[i],loan[i]))         
    elif income[i] > 8000 and income[i]<=9000:
        eight9Thousand.append((income[i],loan[i]))  
    elif income[i] > 9000 and income[i]<=10000:
        nine10Thousan.append((income[i],loan[i]))        
    else:
        ten15Thous.append((income[i],loan[i]))                         

loanRequirement = int(input("Please enter the amount of loan required:"))
candidateIncome = int(input("Please enter the monthly salary:"))
thresholdValue = 50
probability = 0
print('\n\n\n\n')
if candidateIncome < 1000:
    #print(f'Zero {zeroThousand}')
    probability =  listLoanAmount(zeroThousand,loanRequirement)
elif candidateIncome > 1000 and candidateIncome<2000:
    #print(f'One {thousand2Thousand}')
    probability = listLoanAmount(thousand2Thousand,loanRequirement)
elif candidateIncome > 2000 and candidateIncome<3000:
    #print(f'Two {twoThousand3Thousand}')
    probability = listLoanAmount(twoThousand3Thousand,loanRequirement)
elif candidateIncome > 3000 and candidateIncome<4000:
    #print(f'Three {threeThousand4Thou}')
    probability = listLoanAmount(threeThousand4Thou,loanRequirement)
elif candidateIncome > 4000 and candidateIncome<5000:
    #print(f'Four {fourThousand5Thousand}')
    probability = listLoanAmount(fourThousand5Thousand,loanRequirement)     
elif candidateIncome > 5000 and candidateIncome<6000:
    #print(f'Five {fiveThousand6Thousand}')
    probability = listLoanAmount(fiveThousand6Thousand,loanRequirement)
elif candidateIncome > 6000 and candidateIncome<7000:
    #print(f'Six {six7Thousand}')
    probability = listLoanAmount(six7Thousand,loanRequirement)
elif candidateIncome > 7000 and candidateIncome<8000:
    #print(f'Seven {seven8Thousand}')
    probability = listLoanAmount(seven8Thousand,loanRequirement)
elif candidateIncome > 8000 and candidateIncome<9000:
    #print(f'Eight {eight9Thousand}')
    probability = listLoanAmount(eight9Thousand,loanRequirement)
elif candidateIncome > 9000 and candidateIncome<10000:
    #print(f'Nine {nine10Thousan}')
    probability = listLoanAmount(nine10Thousan,loanRequirement)
else:
    #print(f'Ten {ten15Thous}')
    probability = listLoanAmount(ten15Thous,loanRequirement)

print(f'The probability is: {type(probability)}')
print(f'The probability is: {probability:.6f}')