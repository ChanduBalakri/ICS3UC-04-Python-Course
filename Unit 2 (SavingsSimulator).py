##
# Savings Simulator
#
# @author Chandresh
# @course ICS3UC
# @date 2022/03/21 - LastModified
##

# Get amount being invested
valid = False
while (valid != True):
    try:
        amount = float(input("How much money would you like to invest?: "))
        if (amount >= 1):
            valid = True
        else:
            print("Out of range, must be greater than 1, try again!")
    except:
        print("This input must be an number, try again!")

# Get number of years being invested for
while (amount > 0):
  valid1 = False
  while (valid1 != True):
    try:
        years = int(input("How many years will you be investing for?: "))
        if (years > 0):
            valid1 = True
        else:
            print("Out of range, must be greater than 1, try again!")
    except:
        print("This input must be a integer, try again!")
  valid2 = False    
  
  # Get interest percentage from user
  while (valid2 != True):
    try:
        interest = float(input("Enter a percentage of interest you will earn from investing?: "))
        if (interest > 0):
          valid2 = True
        else:
          print("Out of range, must be greater than 0, try again!")
    except:
      print("This input must be a whole number, try again!")
  investmentEarningsFirst = amount * (interest/100) + amount
  
  # Tell the reader their profits
  for i in range(years):
    currentBalance = investmentEarningsFirst
    investmentEarningsFirst = round(currentBalance * (interest/100) + currentBalance, 2)
    print("Year", i+1, "=", currentBalance)
    
  valid3 = False
  # Get withdrawal amount for user
  while (valid3 != True):
    try:
        withdraw = float(input("How much money would you like to withdraw?: "))
        if (withdraw <= currentBalance):
            valid3 = True
        else:
            print("Out of range, must be less than or equal to the total investment money gained, try again!")
    except:
        print("This input must be a number, try again!")
      
  # Calculate how much is left in the investment portfolio after the withdrawal
  amount = round(currentBalance - withdraw, 2)
  print("You now have $", amount, "left inside your investment portfolio")
