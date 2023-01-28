##
# War Card Game
#
# @author Chandresh Balakrishnan
# @course ICS3UC
# @date 2022/05/10 - last modified
##
# import random in order to "shuffle" cards
import random

# subprogram designed to get most inputs from user
def numOfItems():
  
  # entire deck
  typeOfCard = ["2C", "2H", "2S", "2D", "3C", "3H", "3S", "3D", "4C", "4H", "4S", "4D", "5C", "5H", "5S", "5D", "6C", "6H", "6S", "6D", "7C", "7H", "7S", "7D", "8C", "8H", "8S", "8D", "9C", "9H", "9S", "9D", "TC", "TH", "TS", "TD", "JC", "JH", "JS", "JD", "QC", "QH", "QS", "QD", "KC", "KH", "KS", "KD", "AC", "AH", "AS", "AD"]
  valid1 = True
  while(valid1 == True):
    try:
      # ask user how many players there are
      numOfPlayers = int(input("How many players would like to play?: "))
      if (numOfPlayers > 0):
        valid1 = False
      else:
        print("must be an integer greater than 0")
    except:
      print("Not a valid input")
  nameList = []
  playerList = []
  valid2 = True
  while(valid2 == True):
    try:
      # ask user how many cards each play should start with
      numOfCards = int(input("How many cards should each player start with?: "))
      if (numOfCards > 0):
        valid2 = False
      else:
        print("must be an integer greater than 0")
    except:
      print("Not a valid input")
  # get the names of the players
  for i in range(numOfPlayers):
    playerList.append([])
    print("What is the name of player", i+1 ,"?:")
    nameList.append(input())
    # randomly generate corresponding cards
    for k in range(numOfCards):
      playerList[i].append(random.choice(typeOfCard))    
  return numOfPlayers, numOfCards, nameList, playerList

# subprogram designed to actually "play" the main part of the game
def playCards(player, name, card, num):
  over = False
  # a while loop to repeat the code until someone is out of cards
  while (over == False):
    cardValueList = []
    burnList = []
    # for loop to assign each card a specific value
    for i in range(player):
      print(name[i], "'s card is", card[i][0])

      # if statements all assign cards their corresponding value
      if (card[i][0][0] == "2" and card[i][0][1] == "C"):
        burnList.append(card[i][0])
        cardvalue = 2
        cardValueList.append(cardvalue)
      if (card[i][0][0] == "2" and card[i][0][1] == "D"):
        burnList.append(card[i][0])        
        cardvalue = 4
        cardValueList.append(cardvalue)
      if (card[i][0][0] == "2" and card[i][0][1] == "S"):
        burnList.append(card[i][0])        
        cardvalue = 6
        cardValueList.append(cardvalue)
      if (card[i][0][0] == "2" and card[i][0][1] == "H"):
        burnList.append(card[i][0])        
        cardvalue = 8
        cardValueList.append(cardvalue)
      if (card[i][0][0] == "3" and card[i][0][1] == "C"):
        burnList.append(card[i][0])        
        cardvalue = 3
        cardValueList.append(cardvalue)
      if (card[i][0][0] == "3" and card[i][0][1] == "D"):
        burnList.append(card[i][0])        
        cardvalue = 5
        cardValueList.append(cardvalue)
      if (card[i][0][0] == "3" and card[i][0][1] == "S"):
        burnList.append(card[i][0])        
        cardvalue = 7
        cardValueList.append(cardvalue)
      if (card[i][0][0] == "3" and card[i][0][1] == "H"):
        burnList.append(card[i][0])        
        cardvalue = 9
        cardValueList.append(cardvalue)
      if (card[i][0][0] == "4" and card[i][0][1] == "C"):
        burnList.append(card[i][0])        
        cardvalue = 4
        cardValueList.append(cardvalue)
      if (card[i][0][0] == "4" and card[i][0][1] == "D"):
        burnList.append(card[i][0])        
        cardvalue = 6
        cardValueList.append(cardvalue)
      if (card[i][0][0] == "4" and card[i][0][1] == "S"):
        burnList.append(card[i][0])        
        cardvalue = 8
        cardValueList.append(cardvalue)
      if (card[i][0][0] == "4" and card[i][0][1] == "H"):
        burnList.append(card[i][0])        
        cardvalue = 10
        cardValueList.append(cardvalue)
      if (card[i][0][0] == "5" and card[i][0][1] == "C"):
        burnList.append(card[i][0])        
        cardvalue = 5
        cardValueList.append(cardvalue)
      if (card[i][0][0] == "5" and card[i][0][1] == "D"):
        burnList.append(card[i][0])        
        cardvalue = 7
        cardValueList.append(cardvalue)
      if (card[i][0][0] == "5" and card[i][0][1] == "S"):
        burnList.append(card[i][0])        
        cardvalue = 9
        cardValueList.append(cardvalue)
      if (card[i][0][0] == "5" and card[i][0][1] == "H"):
        burnList.append(card[i][0])        
        cardvalue = 11
        cardValueList.append(cardvalue)
      if (card[i][0][0] == "6" and card[i][0][1] == "C"):
        burnList.append(card[i][0])        
        cardvalue = 6
        cardValueList.append(cardvalue)
      if (card[i][0][0] == "6" and card[i][0][1] == "D"):
        burnList.append(card[i][0])        
        cardvalue = 8
        cardValueList.append(cardvalue)
      if (card[i][0][0] == "6" and card[i][0][1] == "S"):
        burnList.append(card[i][0])   
        cardvalue = 10
        cardValueList.append(cardvalue)
      if (card[i][0][0] == "6" and card[i][0][1] == "H"):
        burnList.append(card[i][0])        
        cardvalue = 12
        cardValueList.append(cardvalue)
      if (card[i][0][0] == "7" and card[i][0][1] == "C"):
        burnList.append(card[i][0])        
        cardvalue = 7
        cardValueList.append(cardvalue)
      if (card[i][0][0] == "7" and card[i][0][1] == "D"):
        burnList.append(card[i][0])        
        cardvalue = 9
        cardValueList.append(cardvalue)
      if (card[i][0][0] == "7" and card[i][0][1] == "S"):
        burnList.append(card[i][0])        
        cardvalue = 11
        cardValueList.append(cardvalue)
      if (card[i][0][0] == "7" and card[i][0][1] == "H"):
        burnList.append(card[i][0])        
        cardvalue = 13
        cardValueList.append(cardvalue)
      if (card[i][0][0] == "8" and card[i][0][1] == "C"):
        burnList.append(card[i][0])        
        cardvalue = 8
        cardValueList.append(cardvalue)
      if (card[i][0][0] == "8" and card[i][0][1] == "D"):
        burnList.append(card[i][0])        
        cardvalue = 10
        cardValueList.append(cardvalue)
      if (card[i][0][0] == "8" and card[i][0][1] == "S"):
        burnList.append(card[i][0])        
        cardvalue = 12
        cardValueList.append(cardvalue)
      if (card[i][0][0] == "8" and card[i][0][1] == "H"):
        burnList.append(card[i][0])        
        cardvalue = 14
        cardValueList.append(cardvalue)
      if (card[i][0][0] == "9" and card[i][0][1] == "C"):
        burnList.append(card[i][0])       
        cardvalue = 9
        cardValueList.append(cardvalue)
      if (card[i][0][0] == "9" and card[i][0][1] == "D"):
        burnList.append(card[i][0])        
        cardvalue = 11
        cardValueList.append(cardvalue)
      if (card[i][0][0] == "9" and card[i][0][1] == "S"):
        burnList.append(card[i][0])        
        cardvalue = 13
        cardValueList.append(cardvalue)
      if (card[i][0][0] == "9" and card[i][0][1] == "H"):
        burnList.append(card[i][0])        
        cardvalue = 15
        cardValueList.append(cardvalue)
      if (card[i][0][0] == "T" and card[i][0][1] == "C"):
        burnList.append(card[i][0])        
        cardvalue = 10
        cardValueList.append(cardvalue)
      if (card[i][0][0] == "T" and card[i][0][1] == "D"):
        burnList.append(card[i][0])        
        cardvalue = 12
        cardValueList.append(cardvalue)
      if (card[i][0][0] == "T" and card[i][0][1] == "S"):
        burnList.append(card[i][0])        
        cardvalue = 14
        cardValueList.append(cardvalue)
      if (card[i][0][0] == "T" and card[i][0][1] == "H"):
        burnList.append(card[i][0])        
        cardvalue = 16
        cardValueList.append(cardvalue)
      if (card[i][0][0] == "J" and card[i][0][1] == "C"):
        burnList.append(card[i][0])        
        cardvalue = 11
        cardValueList.append(cardvalue)
      if (card[i][0][0] == "J" and card[i][0][1] == "D"):
        burnList.append(card[i][0])        
        cardvalue = 13
        cardValueList.append(cardvalue)
      if (card[i][0][0] == "J" and card[i][0][1] == "S"):
        burnList.append(card[i][0])        
        cardvalue = 15
        cardValueList.append(cardvalue)
      if (card[i][0][0] == "J" and card[i][0][1] == "H"):
        burnList.append(card[i][0])        
        cardvalue = 17
        cardValueList.append(cardvalue)
      if (card[i][0][0] == "Q" and card[i][0][1] == "C"):
        burnList.append(card[i][0])        
        cardvalue = 12
        cardValueList.append(cardvalue)
      if (card[i][0][0] == "Q" and card[i][0][1] == "D"):
        burnList.append(card[i][0])        
        cardvalue = 14
        cardValueList.append(cardvalue)
      if (card[i][0][0] == "Q" and card[i][0][1] == "S"):
        burnList.append(card[i][0])        
        cardvalue = 16
        cardValueList.append(cardvalue)
      if (card[i][0][0] == "Q" and card[i][0][1] == "H"):
        burnList.append(card[i][0])        
        cardvalue = 18
        cardValueList.append(cardvalue)
      if (card[i][0][0] == "K" and card[i][0][1] == "C"):
        burnList.append(card[i][0])        
        cardvalue = 13
        cardValueList.append(cardvalue)
      if (card[i][0][0] == "K" and card[i][0][1] == "D"):
        burnList.append(card[i][0])        
        cardvalue = 15
        cardValueList.append(cardvalue)
      if (card[i][0][0] == "K" and card[i][0][1] == "S"):
        burnList.append(card[i][0])        
        cardvalue = 17
        cardValueList.append(cardvalue)
      if (card[i][0][0] == "K" and card[i][0][1] == "H"):
        burnList.append(card[i][0])        
        cardvalue = 19
        cardValueList.append(cardvalue)
      if (card[i][0][0] == "A" and card[i][0][1] == "C"):
        burnList.append(card[i][0])        
        cardvalue = 14
        cardValueList.append(cardvalue)
      if (card[i][0][0] == "A" and card[i][0][1] == "D"):
        burnList.append(card[i][0])        
        cardvalue = 16
        cardValueList.append(cardvalue)
      if (card[i][0][0] == "A" and card[i][0][1] == "S"):
        burnList.append(card[i][0])        
        cardvalue = 18
        cardValueList.append(cardvalue)
      if (card[i][0][0] == "A" and card[i][0][1] == "H"):
        burnList.append(card[i][0])        
        cardvalue = 20
        cardValueList.append(cardvalue)
      # remove statement to remove the cards from the main card pile
      card[i].remove(card[i][0])
    # for loop to determine who won the round
    for k in range(players):
      if (max(cardValueList) == cardValueList[k]):
        print(name[k], "won the round")
        for j in range(len(burnList)):
          card[k].append(burnList[j])
    valid3 = True
    while(valid3 == True):
      try:
        # ask user if they want to keep playing
        end = input("Next Round?: ")
        if (end == "y" or end == "n"):
          valid3 = False
        else:
          print("must be a 'y' or 'n' value")
      except:
        print("Not a valid input")
    if (end == "n"):
      over = True
    else:
      print("Next Round Incoming!!!!")
    # for loop to check if anyone has run out of cards
    for i in range(players):
      cardValueList = []
      burnList = []
      if (card[i] == []):
        over = True
  print("game over")
## MAIN
# call numOfItems subprogram
players, numcards, names, cards = numOfItems()
# call playCards subprogram
playCards(players, names, cards, numcards)