##
# Garage Sale
#
# @author Chandresh Balakrishnan
# @course ICS3UC
# @date 2020/05/06 - last modified
##

#getItems subprogram
def getItems():
    print("Seller Please Set Up your Garage Sale >>>>> ")
    # get items from seller
    items = input("Enter a list of items for sale seperated by spaces: ").split()
    costs = []
    print("Seller, you will now be asked to enter the cost of each item.")
    for i in range (len(items)):
      valid1 = True
      while(valid1 == True):
        valid1 = True
        try:
          # get cost of items from seller
          costs.append(int(input("Enter the cost of this item: " + items[i] + " $")))
          if (costs[i] < 0):
            costs.pop()
            print("Cannot be a negetive number")
          elif (costs[i] > 0):
            valid1 = False
          else: 
            print("Must be a value that is greater than 0")
        except:
          print("Not a valid input, must be an integer")
    return items, costs

#buyerWallet subprogram
def buyerWallet(Buyitem, bwallet, itemcost):
  bdeals = 0
  purchasedList = []
  purchasedItemList = []
  for i in range(len(Buyitem)):
    counter = 0
    # ask buyer if they want to buy item
    print("Do you want to buy -", Buyitem[i], "for $", itemcost[i], "(y/n): ")
    valid2 = True
    while (valid2 == True):
      try:
        wantBuy = input()
        if(wantBuy == "y" or wantBuy == "n"):
          valid2 = False
        else:
          print("The values must be 'y' or 'n'")
      except:
        print("Not a valid input") 
    # if buyer does not want the item at the listed       price
    if (wantBuy == "n"):
      valid3 = True
      while (valid3 == True):
        try:
          negotiateBuy = input("Do you want to negotiate this price?: (y/n) ")
          if(negotiateBuy == "y" or negotiateBuy == "n"):
            valid3 = False
          else:
            print("The values must be 'y' or 'n'")
        except:
          print("Not a valid input")
      # if buyer wants to negotiate
      if (negotiateBuy == "y"):
        negotiate = itemcost[i] - 1.1
        stopper = "hello"
        while (negotiate < itemcost[i] - 1 and stopper != "None"):
          counter = counter + 1
          # if negotiate is less than half of the               price
          if(negotiate < (itemcost[i]/2)):
            print("The deal is over, the item was not sold.")
            stopper = "None"
          else:
            negotiate = int(input("What is your counter offer?: $"))
            itemcost[i] = itemcost[i] - 1 
            print("The seller's price is now: $",itemcost[i])
        # if negotiate is within 1 dollar of price
        if(negotiate == itemcost[i] or negotiate >= itemcost[i] - 1):
          # if buyer cannot afford the item
          if (itemcost[i] > bwallet):
            print("You cannot afford this item")
          # calculations to wallets and lists
          else:
            bwallet = bwallet - itemcost[i]
            purchasedList.append(itemcost[i])
            purchasedItemList.append(Buyitem[i])
            bdeals = bdeals + counter 
      # if buyer does not want the item at all 
      elif(negotiateBuy == "n"):
        print("The buyer is not interested :(")
    # if buyer wants to buy the item at the listed        price
    if (wantBuy == "y"):
      # if buyer cannot afford the item
      if (itemcost[i] > bwallet):
        print("You cannot afford this item")
      # calculations to wallets and lists
      else:
        bwallet = bwallet - itemcost[i]
        purchasedList.append(itemcost[i])
        purchasedItemList.append(Buyitem[i])
    print("The buyer's current balance is: $",bwallet)
  return bwallet, itemcost, purchasedList, purchasedItemList, bdeals

#sellerWallet subprogram
def sellerWallet(purchaseList):
  sellerwallet = 0
  for i in range(len(purchaseList)):
    sellerwallet = sellerwallet + purchaseList[i]
  print("The seller's current balance is: $",sellerwallet)
  return sellerwallet

#returnItems subprogram
def returnItems(Returnitem, dollars, Bbalance, Sbalance):
  staticList = []
  for i in range (len(Returnitem)):
    staticList.append(Returnitem[i])
  valid4 = True
  while(valid4 == True):
    try:
      # ask if buyer wants to return any items
      wantToReturn = input("Do you want to return any items?: (y/n) ")
      if (wantToReturn == "y" or wantToReturn == "n"):
        valid4 = False
      else:
        print("Must be 'y' or 'n' values")
    except:
      print("Not a valid input")
  # if buyer wants to return 
  if (wantToReturn == "y"):
    for i in range(len(Returnitem)):
      valid5 = True
      while(valid5 == True):
        print("Do you want to return",staticList[i])
        try:
          # if buyer wants to return this item
          whichToReturn = input()
          if(whichToReturn == "y" or whichToReturn == "n"):
            valid5 = False
          else:
            print("Input must be 'y' or 'n'")
        except:
          print("Not a valid input")
      # return the price to seller and buyer if buyer       wants to return
      if (whichToReturn == "y"):
        print("The buyer returned",staticList[i],"at $",dollars[i])
        Bbalance = Bbalance + dollars[i]
        Sbalance = Sbalance - dollars[i]
        Returnitem.remove(staticList[i])
        print("The buyer now owns:")
        for k in range(len(Returnitem)):
          print(Returnitem[k])
        print("The buyer's curent balance is now $",Bbalance)
        print("The seller's current balance is now $",Sbalance)
  # if buyer does not want to return anything 
  else:
    print("Have a good rest of your day!")
  return staticList

#buyerDeals subprogram
def buyerDeals(deal):
  print("Pass the device to the buyer so they can see their deals. >>>>")
  print("The buyer has saved $",deal,"from negotiating")

##MAIN
# get variables itemList and priceList from getItems subprogram
itemList, priceList = getItems()
print("Pass the device to the customer for purchasing.>>>>")
valid6 = True
while(valid6 == True):
  try:
    # ask buyer how much money they have to spend
    wallet = int(input("How much money does the buyer have to spend? : $"))
    if (wallet > 0):
      valid6 = False
    else:
      print("Must be a value greater than 0")
  except:
    print("Not a valid input")
    
# get variables walletsBalance, totalList, buyList, and newItemList from buyerWallet subprogram
walletsBalance, totalList, buyList, newItemList, deals = buyerWallet(itemList, wallet, priceList)

# get variable swallet from sellerWallet subprogram
swallet = sellerWallet(buyList)

# call buyerDeals subprogram
buyerDeals(deals)

# call returnItems subprogram
returnItems(newItemList, buyList, walletsBalance, swallet)
