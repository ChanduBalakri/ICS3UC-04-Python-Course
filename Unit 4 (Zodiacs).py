##
# Grocery Shopping
#
# @author Chandresh Balakrishnan
# @course ICS3UC
# @date 2022/04/26 - last modified
##

# create empty total list
totalList = []

# reset cost and make it equal to 0 at the start of the code
cost = 0

# reset extraMoney and make it equal to 0 at the start of the code
extraMoney = 0

# get amount and specific fruits from user
def getFruit():
  fruit=[]
  valid1 = True
  while (valid1 == True):
    try:
      # ask user how many fruits they want
      howManyFruits = int(input("How many fruits do you want?: "))
      if(howManyFruits > 0):
        valid1 = False
      else:
        print("Out of range")
    except:
      print("Not a valid input, must be an integer")

  # ask user what fruits they want
  for i in range(howManyFruits):
    typeOfFruit = input("What is your fruit?: ")
    fruit.append(typeOfFruit)
    totalList.append(typeOfFruit)
  return fruit, howManyFruits, typeOfFruit, totalList

# get amount and specific bread from user
def getBread():
  bread=[]
  valid2 = True
  while (valid2 == True):
    try:
      # ask user how many breads they want
      howManyBreads = int(input("How many breads do you want?: "))
      if(howManyBreads > 0):
        valid2 = False
      else:
        print("Out of range")
    except:
      print("Not a valid input, must be an integer")

  # ask user what breads they want
  for i in range(howManyBreads):
    typeOfBread = input("What is your bread?: ")
    bread.append(typeOfBread)
    totalList.append(typeOfBread)
  return bread, howManyBreads, typeOfBread, totalList

# get amount and certain chocolate from user
def getChocolate():
  chocolate=[]
  valid3 = True
  while (valid3 == True):
    try:
      # ask user how many chocolates you want
      howManyChocolates= int(input("How many chocoalates do you want?: "))
      if(howManyChocolates > 0):
        valid3 = False
      else:
        print("Out of range")
    except:
      print("Not a valid input, must be an integer")

  # ask user what chocolates you want
  for i in range(howManyChocolates):
    typeOfChocolate = input("What is your chocolate?: ")
    chocolate.append(typeOfChocolate)
    totalList.append(typeOfChocolate)
  return chocolate, howManyChocolates, typeOfChocolate, totalList

# get amount and certain vegetables from user
def getVegetable():
  vegetable=[]
  valid4 = True
  while (valid4 == True):
    try:
      # ask user how many vegetables they want
      howManyVegetables = int(input("How many vegetables do you want?: "))
      if(howManyVegetables > 0):
        valid4 = False
      else:
        print("Out of range")
    except:
      print("Not a valid input, must be an integer")
      
  # ask user what vegetables they want
  for i in range(howManyVegetables):
    typeOfVegetable = input("What is your vegetable?: ")
    vegetable.append(typeOfVegetable)
    totalList.append(typeOfVegetable)
  return vegetable, howManyVegetables, typeOfVegetable, totalList

# get amount and certain phones from user
def getPhone():
  phone=[]
  valid5 = True
  while (valid5 == True):
    try:
      # ask user how many phones they want
      howManyPhones = int(input("How many phones do you want?: "))
      if(howManyPhones > 0):
        valid5 = False
      else:
        print("Out of range")
    except:
      print("Not a valid input, must be an integer")
      
  # ask user what phones they want
  for i in range(howManyPhones):
    typeOfPhone = input("What is your phone?: ")
    phone.append(typeOfPhone)
    totalList.append(typeOfPhone)
  return phone, howManyPhones, typeOfPhone, totalList

# get amount and certain clothes from user
def getCloth():
  cloth=[]
  valid6 = True
  while (valid6 == True):
    try:
      # ask user how many clothes they want
      howManyClothes = int(input("How many clothes do you want?: "))
      if(howManyClothes > 0):
        valid6 = False
      else:
        print("Out of range")
    except:
      print("Not a valid input, must be an integer")

  # ask user what clothes they want
  for i in range(howManyClothes):
    typeOfCloth = input("What is your cloth?: ")
    cloth.append(typeOfCloth)
    totalList.append(typeOfCloth)
  return cloth, howManyClothes, typeOfCloth, totalList

# allow the user to rebuy items
def getReBuy(extraNum):
  valid7 = True
  
  # give extraFruitsSpecific an empty value
  extraFruitsSpecific = 0
  # give extraVegetablesSpecific an empty value
  extraVegetablesSpecific = 0
  # give extraBreadsSpecific an empty value
  extraBreadsSpecific = 0
  # give extraChocolatesSpecific an empty value
  extraChocolatesSpecific = 0
  # give extraClothesSpecific an empty value
  extraClothesSpecific = 0
  # give extraPhonesSpecific an empty value
  extraPhonesSpecific = 0
  while (valid7 == True):
    try:
      # ask user if they want an extra item
      extraItems = input("What extra item do you want?: ")
      if (extraItems == "fruit" or extraItems == "vegetable" or extraItems == "cloth" or extraItems == "bread" or extraItems == "chocolate" or extraItems == "phone" or extraItems == "none"):
        valid7 = False
      else:
        print("Must be a 'fruit', 'vegetable', 'chocolate', 'bread', 'phone', 'cloth', or 'none'")
    except:
      print("Not a valid input")

  # check if they want more fruits
  if (extraItems == "fruit"):
    valid8 = True
    while (valid8 == True):
      try:
        extraNum = int(input("How many more fruits do you want?: "))
        if (extraNum > 0):
          valid8 = False
        else:
          print("Must be an integer greater than 0")
      except:
        print("Not a valid input")
    for i in range (extraNum):
      extraFruitsSpecific = input("What is the name of your fruit?: ")
    extraNum = extraNum * 2
    totalList.append(extraFruitsSpecific)

  # check if they want more vegetables
  if (extraItems == "vegetable"):
    valid8 = True
    while (valid8 == True):
      try:
        extraNum = int(input("How many more vegetables do you want?: "))
        if (extraNum > 0):
          valid8 = False
        else:
          print("Must be an integer greater than 0")
      except:
        print("Not a valid input")
    for i in range (extraNum):
      extraVegetablesSpecific = input("What is the name of your vegetable?: ")
    extraNum = extraNum * 1
    totalList.append(extraVegetablesSpecific)

  # check if they want more breads
  if (extraItems == "bread"):
    valid8 = True
    while (valid8 == True):
      try:
        extraNum = int(input("How many more breads do you want?: "))
        if (extraNum > 0):
          valid8 = False
        else:
          print("Must be an integer greater than 0")
      except:
        print("Not a valid input")
    for i in range (extraNum):
      extraBreadsSpecific = input("What is the name of your bread?: ")
    extraNum = extraNum * 4
    totalList.append(extraBreadsSpecific)

  # check if they want more clothes
  if (extraItems == "cloth"):
    valid8 = True
    while (valid8 == True):
      try:
        extraNum = int(input("How many more clothes do you want?: "))
        if (extraNum > 0):
          valid8 = False
        else:
          print("Must be an integer greater than 0")
      except:
        print("Not a valid input")
    for i in range (extraNum):
      extraClothesSpecific = input("What is the name of your cloth?: ")
    extraNum = extraNum * 20
    totalList.append(extraClothesSpecific)

  # check if they want more chocolates
  if (extraItems == "chocolate"):
    valid8 = True
    while (valid8 == True):
      try:
        extraNum = int(input("How many more chocolates do you want?: "))
        if (extraNum > 0):
          valid8 = False
        else:
          print("Must be an integer greater than 0")
      except:
        print("Not a valid input")
    for i in range (extraNum):
      extraChocolatesSpecific = input("What is the name of your chocolate?: ")
    extraNum = extraNum * 3
    totalList.append(extraChocolatesSpecific)

  # check if they want more phones
  if (extraItems == "phone"):
    valid8 = True
    while (valid8 == True):
      try:
        extraNum = int(input("How many more phones do you want?: "))
        if (extraNum > 0):
          valid8 = False
        else:
          print("Must be an integer greater than 0")
      except:
        print("Not a valid input")
    for i in range (extraNum):
      extraPhonesSpecific = input("What is the name of your phone?: ")
    extraNum = extraNum * 1000
    totalList.append(extraPhonesSpecific)
  return extraItems, extraNum, extraFruitsSpecific, extraVegetablesSpecific, extraBreadsSpecific, extraChocolatesSpecific, extraPhonesSpecific, extraClothesSpecific 
  
# tell the user all of their items
def checkOut():
  print("You ordered", len(totalList), "items!, these items were:")
  for i in range(len(totalList)):
    print(totalList[i])
    
# calculate the final cost with tax
def finalPrice(fruity, vegetably, bready, chocolatey, phoney, clothey, rebuycost):
  cost = (fruity[1] * 2) + (vegetably[1] * 1) + (bready[1] * 4) + (chocolatey[1] * 3) + (phoney[1] * 1000) + (clothey[1] * 20)
  cost = cost + rebuycost
  print("Your subtotal is $", cost)
  cost = round(cost*1.13, 2)
  print("Your total is $", cost)
  return cost
  
## MAIN PROGRAM

# call getFruit subprogram
fruits = getFruit()

# call getVegetable subprogram
vegetables = getVegetable()

# call getBread subprogram
breads = getBread()

# call getChocolate subprogram
chocolates = getChocolate()

# call getPhone subprogram
phones = getPhone()

# call getCloth subprogram
clothes = getCloth()

# call getReBuy subprogram
rebuyList = getReBuy(extraMoney)

# call checkOut subprogram
checkOut()

# call finalPrice subprogram
finalCost = finalPrice(fruits, vegetables, breads, chocolates, phones, clothes, rebuyList[1])
