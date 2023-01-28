##
# ICS3U Practical - U
# @author Chandresh Balakrishnan
# @course ICS3U-04
# @date 2022/05/11

# get the number of tickets from the user
def getNumOfTickets():
  
  # input validation for adults
  valid1 = True
  while (valid1 == True):
    try:
      numAdults = int(input("Number of Adult Tickets: "))
      if (numAdults >= 0):
        valid1 = False
      else:
        print("Must be an integer greater than 0 or equal to 0")
    except:
      print("Not a valid input")
      
  # input validation for students
  valid2 = True
  while (valid2 == True):
    try:
      numStudents = int(input("Number of Student Tickets: "))
      if (numStudents >= 0):
        valid2 = False
      else:
        print("Must be an integer greater than 0 or equal to 0")
    except:
      print("Not a valid input")
      
  # input validation for fast pass
  valid3 = True
  while (valid3 == True):
    try:
      numFast = int(input("Number of Fast Pass Tickets: "))
      if (numFast >= 0):
        valid3 = False
      else:
        print("Must be an integer greater than 0 or equal to 0")
    except:
      print("Not a valid input")
  
  # make sure numFast is correctly bought
  if (numFast < numAdults + numStudents):
    numFast == 0
    # make sure the user buys correct number of fast passes
    print("You must but fast passes for the whole group, or none at all :(")
    
    # ask user if they want to correctly buy fast passes
    valid4 = True
    while (valid4 == True):
      try:
        wantFast = input("Do you want to buy fast passes for the whole group?: ")
        if (wantFast == "y" or wantFast == "n"):
          valid4 = False
        else:
          print("Must be a 'y' or 'n' value")
      except:
        print("Not a valid input")
    
    # if user wants to buy fast pass for whole group
    if (wantFast == "y"):
      numFast = numAdults + numStudents
    else:
      numFast = 0
  return numAdults, numStudents, numFast

# section these tickets into the specific deal
def calculateDeals(adult, student):
  familyPack = 0
  while (adult >= 2 and student >= 2):
    # familyPack deal
      familyPack = familyPack + 1
      adult = adult - 2
      student = student - 2
  return familyPack, adult, student

# calculate the totals and tell the user their bill
def msgTotals(families, numberOfAdults, numberOfStudents, fastPass):
  
  # create empty ticketList list
  ticketList = []
  # create empt typeList list
  typeList = []
  
  # append all variables to ticketList list
  ticketList.append(families)
  ticketList.append(numberOfAdults)
  ticketList.append(numberOfStudents)
  ticketList.append(fastPass)
  
  # append all "words" to typeList list
  typeList.append("family")
  typeList.append("adult")
  typeList.append("student")
  typeList.append("fast pass")
  
  ##clean up lists to not show 0 values
  # families
  if (families == 0):
    ticketList.remove(families)
    typeList.remove("family")
  # adults
  if (numberOfAdults == 0):
    ticketList.remove(numberOfAdults)
    typeList.remove("adult")
  # students
  if (numberOfStudents == 0):
    ticketList.remove(numberOfStudents)
    typeList.remove("student")
  # fast passes
  if (fastPass == 0):
    ticketList.remove(fastPass)
    typeList.remove("fast pass")
  print("You ordered: ")
  # tell the user what items they ordered
  for i in range(len(typeList)):
    print(ticketList[i],"",typeList[i],"tickets")
    
  # change number of tickets into corresponding prices
  families = families * 100
  numberOfAdults = numberOfAdults * 35
  numberOfStudents = numberOfStudents * 28
  fastPass = fastPass * 20
  totalAmount = families + numberOfAdults + numberOfStudents + fastPass
  
  # tell the user the total amount
  print("Your total amount is: $",totalAmount)
  
##Main Program
# Complete the rest from here - modify as much code as you like
  
# introduction statement
print("WELCOME TO FUNLAND")

# ask user if they want to start an order
valid5 = True
while (valid5 == True):
  try:
    wantOrder = input("Do you want to create an order?: ")
    if (wantOrder == "y" or wantOrder == "n"):
      valid5 = False
    else:
      print("Must be a 'y' or 'n' value")
  except:
    print("Not a valid input")


# continuously ring out orders until the user does not want any more
while(wantOrder == "y"):
  adults, students, fast = getNumOfTickets()
  numOfFamilyPacks, numOfAdults, numOfStudents =  calculateDeals(adults, students)
  msgTotals(numOfFamilyPacks, numOfAdults, numOfStudents,  fast)
  
  # re-ask user if they want to order
  valid6 = True
  while (valid6 == True):
    try:
      wantOrder = input("Do you want to start a new order?: ")
      if (wantOrder == "y" or wantOrder == "n"):
        valid6 = False
      else:
        print("Must be a 'y' or 'n' value")
    except:
      print("Not a valid input")
  
  
# conclusion statement
print("Have a wonderful day!")