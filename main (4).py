##
# Choose Your Own Adventure
#
# @author Chandresh
# @course ICS3UC
# @date 2022-03-09 - LastModified
##
# Title
print("Alien Takeover... can you stop it?!")
print("-------------------------------------------")
# Introduce the story
print("Aliens are planning a world takeover on the Earth in the next 24 hours. Maverick sneaked into their UFO and heard their plan behind the scenes.")

# Ask user for first input
question1 = input("Should Maverick help the aliens for this takeover? (Yes/No): ")

# First branch of input, when question1 = yes, nesting other if statements inside this big if statement
if(question1 == "Yes"):
  print("Maverick has decided to help the aliens, he needs to disable the satellite transmitter from within the NATO headquarters to complete this mission.")
# Proposes next question to the user
  question2 = input("Should he attack the headquarters with a laser gun? (Yes/No): ")
# First variation of answer to question2 "No"
  if(question2 == "No"):
    print("Maverick decides to go in the headquarters with a wooden spoon. As soon as Maverick steps foot into the headquarters he gets shot down for trespassing.")
# Second variation of answer to question2 "Yes"
  if(question2 == "Yes"):
    print("Maverick prepares his laser gun for alien takeover. He enters the headquarters and kills everyone in sight.")
# Proposes next question to the user
    question5 = input("Should Maverick backstab the aliens last second? (Yes/No): ")
# First variation of answer to question5 "Yes"
    if(question5 == "Yes"):
      print("Maverick turns around and shoots all the aliens and saves humanity last second.")
# Second variation of answer to question5 "No"
    if(question5 == "No"):
      print("Maverick disables the satellites and completes his mission for alien takeover. He converts into an alien himself and conquers the world")

# Second branch of input, when question1 = no, nesting other if statements inside this big if statement  
elif(question1 == "No"):
  print("Now Maverick has secret information about the aliens' plans. They are planning on disabling the satellite transmitter within the NATO headquarter.")
# Proposes next question to the user
  question3 = input("Should he inform NATO to protect their headquarters? (Yes/No): ")  
# First variation of answer to question3 "Yes"
  if(question3 == "Yes"):
    print("Maverick snitches on the aliens to the NATO headquarters. NATO proceeds to heavily defend themselves. The aliens attack the headquarters but the NATO were ready and the aliens were defeated. Maverick earned a Novel Peace Prize for his honest work!")
# Second variation of answer to question3 "No"
  if(question3 == "No"):
    print("Maverick steers to keeping this information to himself, he plans on stopping the aliens all by himself?!")
# Proposes next question to the user
    question4 = input("Should Maverick defend the headquarters with a baseball bat? (Yes/No): ")  
# First variation of answer to question4 "Yes"
    if(question4 == "Yes"):
      print("Maverick goes to defend the headquarters with a wooden baseball bat. He gets mowed down by the alien laser guns and the aliens takeover the world.")
# Second variation of answer to question4 "No"
    if(question4 =="No"):
      print("Maverick goes to defend the headquarters with a ak47. He annihilates all the aliens.")
# Proposes next question to the user
      question6 = input("Should Maverick exit the headquarters? (Yes/No): ")
# First variation of answer to question6 "Yes"
      if (question6 == "Yes"):
        print("Maverick exits the headquarters and gets shot by NATO. He was mistaken for and alien, therefore, NATO funded his funeral. His death was not forgotten for his efforts against the alien invasion.")
# Second variation of answer to question6 "No"
      if (question6 == "No"):
        print("Maverick decides to live inside the NATO headquarters as he eats Mini Wheats for the rest of his life!")