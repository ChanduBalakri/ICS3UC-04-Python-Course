##
# SplitTheBill
#
# Chandresh Balakrishnan
# ICS3UC
# 2022/02/23 - Last Modified
##

# Get info about dinner (INPUT)
billAmt = float(input("How much was the bill: "))

peopleAtTable = int(input("How many people were at the table: "))

percentageTip = int(input("What percentage of the bill is being tipped: "))

percentageTax = int(input("What percentage of the bill is being taxed: "))

# Convert percentage values into dollar values (PROCESS)
percentageTax = percentageTax/100
amountTax = round(percentageTax * billAmt, 2)
percentageTip = percentageTip/100
amountTip = round(percentageTip * billAmt, 2)


# Calculate the final amount (OUTPUT)
totalCost = amountTax + amountTip + billAmt
# Calculate the final amount per person
splitCost = round(totalCost/peopleAtTable, 2) 

# Show the user how much they each owe
print("If the bill costs $", billAmt, end="")
print(" with a tip of $", amountTip, end="")
print(" and a tax of $", amountTax, end="")
print(", the subtotal is $", totalCost, end="")
print(" and each person will have to pay $", splitCost, ".")
