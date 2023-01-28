##
# Xavier Golf Scores
#
# @author Chandresh Balakrishnan
# @course ICS3UC
# @date 2022/04/06 - LastModified
##

# Ask player for number of holes in the course
valid = False
while (valid != True):
  try:
    holes = int(input("Number of holes?: "))
    if(holes > 0):
      valid = True
    else:
      print("Must be greater than 0")
  except:
    print("Not a valid input")
playerList = list()

# Ask player for the amount of players playing and make players(int) into a list
x=0
valid1 = False
while (valid1 != True):
  try:
    players = int(input("How many players are playing?: "))
    while(x != players):
      playerList.append(x+1)
      x = x+1
    if(players > 0):
      valid1 = True
    else:
      print("Must be greater than 0")
  except:
    print("Not a valid input")
names = list()
scores = list()
for i in range(players):
  print("What is the name of player", playerList[i], "?:")
  names.append(input())
  
# Get player's score
for p in range(holes):
  for i in range (players):
    print("What was", names[i],"'s score on hole", p + 1)
    valid3 = False
    while(valid3 != True):
      try:
        score = input()
        if(score == "bogey" or score == "par" or score == "birdie" or score == "eagle"):
          valid3 = True
        else:
          print("Must be bogey, par, birdie, or an eagle")
      except:
        print("Out of range")
    if (score == "bogey"):
      score = 1
    if(score == "par"):
      score = 0
    if(score == "birdie"):
      score = -1
    if(score == "eagle"):
      score = -2
    scores.append(score)

# Get each player's current score
  for k in range(players):
    currentScore = 0
    for h in range(p+1):
      if(h==0):
        currentScore = scores[h+k]
      else:
        currentScore = currentScore + scores[(players*h)+k]
    print(names[k], "'s CURRENT score is", currentScore)

# Get each player's final score
for i in range(players):
  individualScore = scores[i]
  counter2 = players
  for k in range(holes-1):
    individualScore = individualScore + scores[i+counter2]
    counter2 = counter2 + players
  print("-------------------------------------------")
  print(names[i], "'s FINAL score is", individualScore)
  
