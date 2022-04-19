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
        #print(i[1],end='\n')
        print(i,end='\n')

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
        print(f"Zero to thousand {income[i],loan[i]}")
        zeroThousand.append((income[i],loan[i]))
    elif income[i] > 1000 and income[i]<=2000:
        print(f" two thousand {income[i],loan[i]}")
        thousand2Thousand.append((income[i],loan[i]))
    elif income[i] > 2000 and income[i]<=3000:
        print(f"three thousand {income[i],loan[i]}")
        twoThousand3Thousand.append((income[i],loan[i]))
    elif income[i] > 3000 and income[i]<=4000:
        print(f"four thousand {income[i],loan[i]}")
        threeThousand4Thou.append((income[i],loan[i]))
    elif income[i] > 4000 and income[i]<=5000:
        print(f"five thousand {income[i],loan[i]}")
        fourThousand5Thousand.append((income[i],loan[i]))        
    elif income[i] > 5000 and income[i]<=6000:
        print(f"six thousand {income[i],loan[i]}")
        fiveThousand6Thousand.append((income[i],loan[i]))                
    elif income[i] > 6000 and income[i]<=7000:
        print(f"seven thousand {income[i],loan[i]}")
        six7Thousand.append((income[i],loan[i]))         
    elif income[i] > 7000 and income[i]<=8000:
        print(f"eight thousand {income[i],loan[i]}")
        seven8Thousand.append((income[i],loan[i]))         
    elif income[i] > 8000 and income[i]<=9000:
        print(f"nine thousand {income[i],loan[i]}")
        eight9Thousand.append((income[i],loan[i]))  
    elif income[i] > 9000 and income[i]<=10000:
        print(f"ten thousand {income[i],loan[i]}")
        nine10Thousan.append((income[i],loan[i]))        
    else:
        print(f"above thousand {income[i],loan[i]}")
        ten15Thous.append((income[i],loan[i]))                         

'''
print(f'Zero to Thousand \n {zeroThousand}\n\n\n')

print(f'Thousand \n {thousand2Thousand}\n\n\n')

print(f'2 Thousand \n {twoThousand3Thousand}\n\n\n')

print(f'3 Thousand \n {threeThousand4Thou}\n\n\n')

print(f'4 Thousand \n {fourThousand5Thousand}\n\n\n')

print(f'5 Thousand \n {fiveThousand6Thousand}\n\n\n')

print(f'6 Thousand \n {six7Thousand}\n\n\n')

print(f'7 Thousand \n {seven8Thousand}\n\n\n')

print(f'8 Thousand \n {eight9Thousand}\n\n\n')

print(f'9 Thousand \n {nine10Thousan}\n\n\n')

print(f'10 Thousand \n {ten15Thous}\n\n\n')

'''

loanRequirement = int(input("Please enter the amount of loan required:"))
candidateIncome = int(input("Please enter the monthly salary:"))
thresholdValue = 50
print('\n\n\n\n')
if candidateIncome < 1000:
    print(f'Zero {loanRequirement}')
    listLoanAmount(zeroThousand,loanRequirement)
elif candidateIncome > 1000 and candidateIncome<2000:
    print(f'One {loanRequirement}')
    listLoanAmount(thousand2Thousand,loanRequirement)
elif candidateIncome > 2000 and candidateIncome<3000:
    print(f'Two {loanRequirement}')
    listLoanAmount(twoThousand3Thousand,loanRequirement)
elif candidateIncome > 3000 and candidateIncome<4000:
    print(f'Three {loanRequirement}')
    listLoanAmount(threeThousand4Thou,loanRequirement)
elif candidateIncome > 4000 and candidateIncome<5000:
    print(f'Four {loanRequirement}')
    listLoanAmount(fourThousand5Thousand,loanRequirement)     
elif candidateIncome > 5000 and candidateIncome<6000:
    print(f'Five {loanRequirement}')
    listLoanAmount(fiveThousand6Thousand,loanRequirement)
elif candidateIncome > 6000 and candidateIncome<7000:
    print(f'Six {loanRequirement}')
    listLoanAmount(six7Thousand,loanRequirement)
elif candidateIncome > 7000 and candidateIncome<8000:
    print(f'Seven {loanRequirement}')
    listLoanAmount(seven8Thousand,loanRequirement)
elif candidateIncome > 8000 and candidateIncome<9000:
    print(f'Eight {loanRequirement}')
    listLoanAmount(eight9Thousand,loanRequirement)
elif candidateIncome > 9000 and candidateIncome<10000:
    print(f'Nine {loanRequirement}')
    listLoanAmount(nine10Thousan,loanRequirement)
else:
    print(f'Ten {loanRequirement}')
    listLoanAmount(ten15Thous,loanRequirement)