##
# Curling - Your exam practical :-)
# Author: Mr. Reid and ...
# Course: ICS3UC
#
# Based on template from programarcadegames.com
##

# Import a library of functions called 'pygame'
import pygame
import random
import math

# Default Colours
BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
YELLOW=(255,255,0)
GREY=(100,100,100)

########################################################
# The following defines classes used
# Class - Rock
class Rock:
    # Attributes
    x = 0.0
    y = 0.0
    width = 30
    speedX = 0.0
    speedY = 0.0
    colour = RED
    thrown = False
    inMotion = False

    def __init__(self, c, x, y):
        self.x = x
        self.y = y
        self.colour = c


    # Draw our Rock
    def draw(self):
        pygame.draw.ellipse(screen, GREY, [self.x-self.width/2, self.y-self.width/2, self.width, self.width], 0)
        pygame.draw.ellipse(screen, self.colour, [self.x-self.width/4, self.y-self.width/4, self.width/2, self.width/2], 0)

    # Distance from any point
    def distance(self, point):
        return math.sqrt( pow(rock.x - point[0],2) + pow(rock.y - point[1], 2) )
      
    # make the rock move
    def move(self):
      # Move only if the rock is thrown
      if (rock.inMotion == True):
        rock.speedY -= 0.1

        if (rock.speedY < 0):
            rock.speedY = 0
            rock.speedX = 0
            rock.inMotion = False
        else:
            rock.x += rock.speedX
            rock.y += rock.speedY

##############################################
# Subprogram to draw the Curling Rink - don't worry about this code
def drawBoard():

    # House
    pygame.draw.ellipse(screen, RED, [75, 400, 350, 350], 0)
    pygame.draw.ellipse(screen, WHITE, [140, 465, 220, 220], 0)
    pygame.draw.ellipse(screen, BLUE, [190, 515, 120, 120], 0)
    pygame.draw.ellipse(screen, WHITE, [230, 555, 40, 40], 0)

    # Lines
    pygame.draw.line(screen, BLACK, [0, 50], [screen.get_width(), 50], 1)
    pygame.draw.line(screen, BLACK, [0, 750], [screen.get_width(), 750], 1)
    pygame.draw.line(screen, BLACK, [screen.get_width()/2, 50], [screen.get_width()/2, 750], 1)
    pygame.draw.line(screen, BLACK, [0, 575], [screen.get_width(), 575], 1)

    # Scoreboard
    pygame.draw.rect(screen, BLACK, [100, 750, 100, 50], 1)
    pygame.draw.rect(screen, BLACK, [200, 750, 100, 50], 1)
    pygame.draw.rect(screen, BLACK, [300, 750, 100, 50], 1)
    pygame.draw.rect(screen, BLACK, [400, 750, 100, 50], 1)

    # Instructions
    Instfont = pygame.font.SysFont('Calibri', 14, True, False)
    text = Instfont.render("Arrows: Adjust weight/spin   Space:throw",True,BLACK)
    screen.blit(text, [0, 0])

    # Controls
    stopper = 0
    Instfont = pygame.font.SysFont('Calibri', 20, True, False)
    text = Instfont.render("Weight: "+str(round(weight,1)),True,BLACK)
    screen.blit(text, [300, 0])
    text = Instfont.render("Spin: "+str(spin),True,BLACK)
    screen.blit(text, [420, 0])
    text = Instfont.render("Results:",True,BLACK)
    screen.blit(text, [20, 765])

    for i in range(4):
        text = Instfont.render(resultList[i],True,BLACK)
        screen.blit(text, [100*(i) + 130, 765])

    # Game Over
    if (turns >= 4):
        font = pygame.font.SysFont('Calibri', 40, True, False)
        text = font.render("Game Over",True,RED)
        screen.blit(text, [150, 300])
        text = font.render("Best:"+bestResult,True,RED)
        screen.blit(text, [150, 350])


################################################################
# Other subprogram you may want to create go here
def scores():
  for i in range(1):
      print(rock.distance(houseCenter))
      if (rock.distance(houseCenter) <= 10):
        resultList.append("Button")
      if (rock.distance(houseCenter) <= 70 and rock.distance(houseCenter) > 10):
        resultList.append("4ft")
      if (rock.distance(houseCenter) <= 100 and rock.distance(houseCenter) > 70):
        resultList.append("8ft")
      if (rock.distance(houseCenter) <= 200 and rock.distance(houseCenter) > 100):
        resultList.append("12ft")
      if (rock.distance(houseCenter) > 200):
        resultList.append("Miss")
  print(resultList)
################################################################
# Main ####

## MODEL

################################################################
# Question 1: Fix the spacing and add comments the following
# code demonstrating your understanding of the purpose of
# the instructions. (Over commenting will be allowed here)
      
# initialize pygame library to be used throughout the code
pygame.init()

# create the size of the window being used for this program
size=(500,800)

# Determine the center of the house coordinates to use for scoring later in the code
houseCenter=(250,575)

# create screen with the size of 500 width and 800 height
screen=pygame.display.set_mode(size)

# create a variable called clock to set clock.tick(frames per second) later in the code. This allows the code to change and it allows animation. It can be considered as a "time" aspect to the code
clock=pygame.time.Clock()

# create the title "Xavier Curling" for this program
pygame.display.set_caption("Xavier Curling")

# set done to False so the main loop can run forever until done is True
done=False

# set number of turns player has used to 0
turns=0

# set weight to a default of 7
weight=7

# set spin to a default of 0
spin=0

#?
myTurn=False

# stopper to allow for resultList.pop to function and run only once while in the main loop
stopper = 0

# create the inner part of the object that the user controls; the "rock"
rock=Rock(YELLOW,random.randint(20,screen.get_width()-20),30)

# create an empty result list
resultList=["","","",""]

# create an empty best result list
bestResult=""

### End Question 1 ##

# MAIN LOOP
while not done:
    ## CONTROL
    ############################################################
    # Question 2: You might notice that you can still change
    # the rocks weight and spin after it's thrown.  There is a
    # mistake in the code below.  Read over the code below and
    # fix it so that we can only only change the values while
    # its at the top. (hint no new code needs to be added)
    #

    for event in pygame.event.get(): # User did something
        # Handle the exit
        if (event.type == pygame.QUIT):
            done = True
        elif (event.type == pygame.KEYDOWN):
            # User allowed keys
            if (rock.thrown == False):       
              if (event.key == pygame.K_RIGHT):
                  spin = spin + 1
              if (event.key == pygame.K_LEFT):
                  spin = spin - 1
              if (event.key == pygame.K_UP):
                  weight = weight + 0.2
              if (event.key == pygame.K_DOWN):
                  weight = weight - 0.2
              if (event.key == pygame.K_SPACE):
                      rock.thrown = True
                      rock.speedX = spin / 10.0
                      rock.speedY = weight
                      rock.inMotion = True
    ### End of Question 2 ##
 ############################################################
    # Question 3: The following two blocks of code handle
    # the movement of the rock.  Move and edit this code
    # so that it's a behaviour of the rock class and replace
    # it with the appropriate call here.
    #
    rock.move()
    
   ### End Question 3 ##

    # Ready for next shot if everything has stopped
    if (rock.inMotion == False) and (rock.thrown == True):
        ########################################################
        # Question 4:  Here we need record how well the shot did
        # in proper curling terms.  Create a subprogram above
        # the main to determine the result based on the distance
        # from the middle of the house.  There is a behaviour of
        # the rock class to determine the distance from any point.
        # Center of house (250, 575)
        # Approx Distances:  Button-10, 4ft-70, 8ft-100, 12ft-200
        # Anything else is a "Miss"  (don't use a subprogram for part marks)

        # Score the rock in the resultList
        scores()

        ### End Question 4 ##


        # Pause for effect
        turns = turns + 1;
        pygame.time.wait(1000)

        if (turns < 4):
            # Create rock at random y position
            rock = Rock(YELLOW, random.randint(20, screen.get_width()-20), 30)
        else:
            # Show the best shot at the end
            rock.thrown = False

            ####################################################
            # Question 5: We would like to show the best shot
            # that was made at the end of the game.  Here go
            # back through the results and set the String for
            # the "best" result.  Doing so may make you rethink
            # how you are storing your results.  Make whatever
            # changes you think should be required to satisfy
            # this requirement.
            #
            #Button = 4
            #4ft = 3
            #8ft = 2
            #12ft = 1
            #if (resultList[0] > resultList[1] and resultList[0] > resultList[2] and resultList[0] > resultList[3]):
             # bestResult = "Shot 1"
            #if (resultList[1] > resultList[0] and resultList[1] > resultList[2] and resultList[1] > resultList[3]):
            # bestResult = "Shot 2"
           # if (resultList[2] > resultList[1] and resultList[2] > resultList[3] and resultList[2] > resultList[0]):
             # bestResult = "Shot 3"
           # if (resultList[3] > resultList[1] and resultList[3] > resultList[2] and resultList[3] > resultList[0]):
             # bestResult = "Shot 4"

            ### End of Question 5 #####

    ## VIEW
    # Redraw playing board
    screen.fill(WHITE)
    if (turns >= 4 and stopper != 1):
      resultList.pop(0)
      resultList.pop(1)
      resultList.pop(2)
      resultList.pop(3)
      stopper = 1
    drawBoard()

    # Draw objects
    rock.draw()

    # Display
    pygame.display.flip()
    clock.tick(30)

# Be IDLE friendly
pygame.quit()
