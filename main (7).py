##
# Sounds Fishy
#
# @author Chandresh Balakrishnan
# @course ICS3UC
# @date 2022/04/08 - LastModified

# Create depth readings list
keepDiving = "Yes"
depthReadings = list()
depthReadingstart = input("Depth Reading: ")

# Ask user for Depth Reading input
while (depthReadingstart != "finish"):
  for i in range(2):
    depthReadings.append(input("Depth reading: "))
    
# Calculate whether Fish Rising, Fish Diving, Constant Depth, No Fish
  if (depthReadingstart > depthReadings[0] and depthReadings[0] > depthReadings[1] and depthReadingstart > depthReadings[1]):
      print("Fish Diving")
       
  elif (depthReadingstart < depthReadings[0] and depthReadings[0] < depthReadings[1] and depthReadingstart < depthReadings[1]):
      print("Fish Rising")
    
  elif (depthReadingstart == depthReadings[0] and depthReadings[0] == depthReadings[1] and depthReadingstart == depthReadings[1]):
      print("Constant Depth")
    
  else:
    print("No Fish")

# Clear list to accept new inputs
  depthReadingstart = input("Depth reading: ")
  depthReadings.clear()
print("All Done")
