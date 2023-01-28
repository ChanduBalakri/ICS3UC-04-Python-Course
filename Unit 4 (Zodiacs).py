##
# Zodiac Compatibility
#
# @author Chandresh, Daniel U., Adrian
# @course ICS3UC
# @date 2022/04/20 - last modified
##

#Get names of people
def getNames(number):
    print("What is the", number, "person's name?: ")
    person = input()
    return person

#Get birthdays of users
def getBirthday(people):
    valid1 = True

    #Enter birth month
    while (valid1 == True):
        try:
            print(people+", please enter your birth month")
            month = int(input())
            if(month<=12 and month>=1):
                valid1 = False
            else:
                print("Not in range of 1-12")
        except:
            print("Not a valid input, must be an integer")

    #Find birth day number for each month
    #Jan, Mar, May, Jul, Aug, Oct, Dec
    if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):

        #Enter birthday day
        valid2 = True
        while (valid2 == True):
            try:
                print(people+", enter the day of your birthday: ")
                day = int(input())
                if (day <= 31):
                    valid2 = False
                else:
                    print("Out of range for the selected month")
            except:
              print("Must be an integer")

    #Apr, Jun, Sep, Nov
    elif (month == 4 or month == 6 or month == 9 or month == 11):

        #Enter birthday day
        valid3 = True
        while (valid3 == True):
            try:
                print(people, ", enter the day of your birthday: ")
                day = int(input())
                if (day <= 30):
                    valid3 = False
                else:
                    print("Out of range for the selected month")
            except:
                print("Must be an integer")  

    #Feb
    elif (month == 2):

        #Enter birthday day
        valid4 = True
        while (valid4 == True):
            try:
                print(people, ", enter the day of your birthday: ")
                day = int(input())
                if (day <= 28):
                    valid4 = False
                else:
                    print("Out of range for the selected month")
            except:
                print("Must be an integer")  
                
    return day, month

#Get zodiac sign
def getZodiacSign(month, day):
    sign = "result"
    #Jan
    if (month == 1):
        if(day>=19):
            sign = "capricorn"
            element = "earth"
        else:
            sign = "sagittarius"
            element = "fire"
    #Feb
    elif (month == 2):
        if(day<=15):
            sign = "capricorn"
            element = "Earth"
        else:
            sign = "aquarius"
            element = "air"
    #March
    elif (month == 3):
        if(day<=11):
            sign = "aquarius"
            element = "air"
        else:
            sign = "pisces"
            element = "water"
    #Apr
    elif (month == 4):
        if(day<=18):
            sign = "pisces"
            element = "water"
        else:
            sign = "aries"
            element = "fire"
    #May
    elif (month == 5):
        if(day<=13):
            sign = "aries"
            element = "fire"
        else:
            sign = "taurus"
            element = "earth"
    #June
    elif (month == 6):
        if(day<=19):
            sign = "taurus"
            element = "earth"
        else:
            sign = "gemini"
            element = "air"
    #July
    elif (month == 7):
        if(day<=20):
            sign = "gemini"
            element = "air"
        else:
            sign = "cancer"
            element = "water"
    #Aug
    elif (month == 8):
        if(day<=9):
            sign = "cancer"
            element = "water"
        else:
            sign = "leo"
            element = "fire"
    #Sept
    elif (month == 9):
        if(day<=15):
            sign = "leo"
            element = "fire"
        else:
            sign = "virgo"
            element = "earth"
    #Oct
    elif (month == 10):
        if(day<=30):
            sign = "virgo"
            element = "earth"
        else:
            sign = "libra"
            element = "air"
    #Nov
    elif (month == 11):
        if(day<=22):
            sign = "libra"
            element = "air"
        elif(day<=29):
            sign = "scorpio"
            element = "water"
        else:
            sign = "ophiuchus"
            element = "water"
    #Dec
    elif (month == 12):
        if(day<=17):
            sign = "ophiuchus"
            element = "water"
        else:
            sign = "sagittarius"
            element = "fire"
    return sign, element

#Power couple
def getPowerCouple():
    if (zSign == "taurus" and zSign2 == "cancer"):
        power = "power couple"
    elif (zSign == "cancer" and zSign2 == "taurus"):
        power = "power couple"
        
    elif (zSign == "gemini" and zSign2 == "aries"):
        power = "power couple"
    elif (zSign == "aries" and zSign2 == "gemini"):
        power = "power couple"
        
    elif (zSign == "leo" and zSign2 == "leo"):
        power = "power couple"
        
    elif (zSign == "virgo" and zSign2 == "virgo"):
        power = "power couple"
        
    elif (zSign == "libra" and zSign2 == "capricorn"):
        power = "power couple"
    elif (zSign == "capricorn" and zSign2 == "libra"):
        power = "power couple"
        
    elif (zSign == "scorpio" and zSign2 == "sagittaruis"):
        power = "power couple"
    elif (zSign == "sagittarius" and zSign2 == "scorpio"):
        power = "power couple"
        
    elif (zSign == "aquarius" and zSign2 == "pisces"):
        power = "power couple"
    elif (zSign == "pisces" and zSign2 == "aquarius "):
        power = "power couple"
    else:
        power = "None"
    return power

#Dangerous matches
def getDangerousMatches():
    if (zSign == "aries" and zSign2 == "cancer"): 
        danger = "danger couple"
    elif (zSign == "cancer" and zSign2 == "aries"):
        danger = "danger couple"
        
    elif (zSign == "taurus" and zSign2 == "leo"):
        danger = "danger couple"
    elif (zSign == "leo" and zSign2 == "taurus"):
        danger = "danger couple"
        
    elif (zSign == "cancer" and zSign2 == "aquarius"):
        danger = "danger couple"
    elif (zSign == "aquarius" and zSign2 == "cancer"):
        danger = "danger couple"
        
    elif (zSign == "leo" and zSign2 == "capricorn"):
        danger = "danger couple"
    elif (zSign == "capricorn" and zSign2 == "leo"):
        danger = "danger couple"
        
    elif (zSign == "virgo" and zSign2 == "sagittarius"):
        danger = "danger couple"
    elif (zSign == "sagittarius" and zSign2 == "virgo"):
        danger = "danger couple"
        
    elif (zSign == "libra" and zSign2 == "virgo"):
        danger = "danger couple"
    elif (zSign == "virgo" and zSign2 == "libra"):
        danger = "danger couple"
        
    elif (zSign == "scorpio" and zSign2 == "libra"):
        danger = "danger couple"
    elif (zSign == "libra" and zSign2 == "scorpio"):
        danger = "danger couple"
        
    elif (zSign == "pisces" and zSign2 == "pisces"):
        danger = "danger couple"
    else:
        danger = "None"
    return danger   

#Zodiac sign
def msgZodiacSign(person, sign):
    print(person+"'s zodiac sign is", sign)

#Print zodiac element
def msgZodiacElement(person, element):
  print(person+"'s zodiac element is", element)

#Power couple contradiction
def msgCompatibleContradictionsPower():
    if (dangerousMatch == "None" and powerCouple == "power couple" and zElement != zElement2):
        print("You guys are a Power Couple, however, your elements do not match. After further research, Power Couple and Danger Match cases should overrule the regular zodiac compatibility element rule. Therefore, you guys are compatible!")
        
    elif (dangerousMatch == "None" and powerCouple == "None" and zElement == zElement2):
        print("Both of your elements match! You guys are neither a Power Couple or a Danger Match. Therefore, you guys are compatible!")
        
    elif (dangerousMatch == "None" and powerCouple == "power couple" and zElement == zElement2):
        print("You guys are compatible! You both have the same elements and you are even a Power Couple!!!")

#Danger couple contradiction
def msgCompatibleContradictionsDangerous():
    if (powerCouple == "None" and dangerousMatch == "danger couple" and zElement != zElement2):
        print("You guys are completely NOT compatible. You do not have the same elements AND you are a Danger Match. Unfortunately, you guys are NOT compatible :(")
        
    elif (powerCouple == "None" and dangerousMatch == "danger couple" and zElement == zElement2):
        print("You are considered a Danger Match. However, your elements are the same. Unfortunately, we have concluded that Danger Matches and Power Couples overrule the basic zodiac element compatibility. Therefore, you guys are not compatible :(")
        
    elif (powerCouple == "None" and dangerousMatch == "None" and zElement != zElement2):
        print("Both of your element do NOT match. You guys are neither a Power Couple nor a Danger Match. Unfortunately, you guys are not compatible :(")
      
## MAIN Program

# Get birthdays and names
person1 = getNames("first")
person2 = getNames("second")
bday, bmonth = getBirthday(person1)
bday2, bmonth2 = getBirthday(person2)

# Find their signs, elements, and compatibility
zSign, zElement = getZodiacSign(bmonth, bday)
zSign2, zElement2 = getZodiacSign(bmonth2, bday2)
powerCouple = getPowerCouple()
dangerousMatch = getDangerousMatches()

# Tell user their zodiac signs and elements
msgZodiacSign(person1, zSign)
msgZodiacSign(person2, zSign2)
msgZodiacElement(person1, zElement)
msgZodiacElement(person2, zElement2)

# Are they compatible?
msgCompatibleContradictionsPower()
msgCompatibleContradictionsDangerous()
