##
# PINReset
#
# @author Chandresh Balakrishnan
# @course ICS3UC
# @date 2022/04/12 - LastModified
##

# Declare Subprograms
# get username from User
def getUser():
  name = input("What is your username?: ")
  return name
#get PIN from user
def getPin():
  pinEntered = int(input("What is your pin?: "))
  return pinEntered
# print welcome msg if password is correct
def msgWelcome():
  print("Welcome!")
# reset the password
def getNewPin():
  newPin = int(input("What is your new pin? "))
  return newPin
#sign out 'username'
def signOut(person):
  print("Goodbye", person)
 
# userName and set correct PIN    
userName = getUser()
correctPin = 1111
pinEntered = getPin()
#if password is correct welcome the userName
while (pinEntered != correctPin):
  pinEntered = getPin()
if (correctPin == pinEntered):
  msgWelcome()
#Reset the PIN
valid1 = True
while(valid1 == True):
  try:
    reset = getNewPin()
    if (reset != correctPin and reset > 999 and reset < 10000):
      print("Your new pin is", reset)
      valid1 = False
    else:
      print("Pin must be between 1000 and 9999. Also cannot be the same as previous pin.")
  except:
    print("Out of range")
#Sign Out
signOut(userName)
