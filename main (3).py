##
# Password Generator
#
# @author Chandresh
# @course ICS3UC
# @date 2022-02-27 - LastModified
##

# Get inputs from the User (INPUT)
firstName = input("What is your first name?: ")
birthDate = input("What year were you born?: ")
birthPlace = input("Which country were you born?: ")
favouriteFood = input("What is your favourite food?: ")
lastName = input("What is your last name?: ")
favouriteSubject = input("What is your favourite school subject?: ")
phonePassword = input("What is your phone password?: ")

# Create your password (PROCESS)
password = firstName[1:5].upper() + birthDate[2].upper() + firstName[5:7].lower() + birthPlace[3:5].upper() + favouriteFood[2:5].lower() + lastName[4:6].upper() + favouriteSubject[1:-2].lower() + phonePassword[2:-2]

# Show the user the new password (OUTPUT)
print("Your secure password is:")
print(password)
