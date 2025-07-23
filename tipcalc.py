import math
#Get initial item price from user


num1 = float(input("Enter bill amount: "))

#Puts the equal sign 30 times for spacing and formatting

print("=" * 30)

#Receives given item price from user and puts it as a bill

print("\nBill: $", format(num1 , ".2f"))

#Formula for the Tip

stnum = (num1 * 0.15)

#Tip calculation

print("\nTip (15%): $", format(stnum , ".2f"))

#Total cost calculation

print("\nTotal: $", format(stnum + num1 , ".2f"))

print("=" * 30)

