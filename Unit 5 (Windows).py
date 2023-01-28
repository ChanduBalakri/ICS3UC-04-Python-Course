##
# Pygame base template for opening a window
# MVC version
#
# @author Chandresh Balakrishnan
# @course ICS3UC
# @date 2022/05/26 Last modified
#
# Simpson College Computer Science
# http://programarcadegames.com/
# http://simpson.edu/computer-science/
##

## Pygame setup
import pygame

# setup screen and title
pygame.init()
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Chandresh Create-A-Picture")

## MODEL - Data use in system
# Subprograms
# draw sky subprogram
def drawSky():
  pygame.draw.rect(screen, triColour_BLUE, [0, 0, 800, 300])

# draw ground subprogram
def drawGround():
  pygame.draw.rect(screen, GREY, [0, 550, 800, 50])

# draw road subprogram
def drawRoad():
  pygame.draw.rect(screen, BLACK, [0, 300, 800, 400])
  for x_offset in range(0, 601, 200):
    pygame.draw.line(screen, YELLOW, [25 + x_offset, 425], [100 + x_offset, 425], 10)

# draw UFO subprogram
def drawUFO(x_random, y_random, colour1, colour2, colour3, colour4, colour5):
    # Create UFO Body
    pygame.draw.ellipse(screen, colour1, [400+x_random, 100+y_random, 125, 50]) 
    pygame.draw.ellipse(screen, colour2, [400+x_random, 100+y_random, 125, 50],10) 
    pygame.draw.ellipse(screen, colour1, [440+x_random, 75+y_random, 50, 50])  

    # Create UFO Windows
    pygame.draw.circle(screen, colour3, [435+x_random, 125+y_random], 7.5)
    pygame.draw.circle(screen, colour4, [435+x_random, 125+y_random], 7.5, 2)
    pygame.draw.circle(screen, colour3, [465+x_random, 130+y_random], 7.5)
    pygame.draw.circle(screen, colour4, [465+x_random, 130+y_random], 7.5, 2)
    pygame.draw.circle(screen, colour3, [495+x_random, 125+y_random], 7.5)
    pygame.draw.circle(screen, colour4, [495+x_random, 125+y_random], 7.5, 2)
    pygame.draw.ellipse(screen, colour3, [450+x_random, 85+y_random, 35, 20])
    pygame.draw.ellipse(screen, colour4, [450+x_random, 85+y_random, 35, 20], 2)
  
    # These arcs imply the direction of movement of the UFO, not just random arcs
    pygame.draw.arc(screen, colour5, [450+x_random,80+y_random,100,50], 0, pi/2, 2)
    pygame.draw.arc(screen, colour5, [438+x_random,90+y_random,100,50], 0, pi/2, 2)

# Define some colors
BLACK = (0, 0, 0)
BLUE = (6, 26, 42)
LIGHT_BLUE = (164, 222, 227)
WHITE = (255, 255, 255)
GREY = (95, 95, 95)
RED = (255, 0, 0)
YELLOW = (237, 246, 37)
PINK = (254, 174, 243)
BROWN = (49, 32, 9)
GREEN = (40, 206, 37)
DARK_GREEN = (75, 83, 32)

# changeable colours
ufo1triColour_GREY = [95, 95, 95]
ufo1triColour_GREEN = [40, 206, 37]
ufo1triColour_LIGHT_BLUE = [164, 222, 227]
ufo1triColour_WHITE = [255, 255, 255]
ufo1triColour_PINK = [254, 174, 243]
ufo2triColour_GREY = [95, 95, 95]
ufo2triColour_GREEN = [40, 206, 37]
ufo2triColour_LIGHT_BLUE = [164, 222, 227]
ufo2triColour_WHITE = [255, 255, 255]
ufo2triColour_PINK = [254, 174, 243]
ufo3triColour_GREY = [95, 95, 95]
ufo3triColour_GREEN = [40, 206, 37]
ufo3triColour_LIGHT_BLUE = [164, 222, 227]
ufo3triColour_WHITE = [255, 255, 255]
ufo3triColour_PINK = [254, 174, 243]
ufo4triColour_GREY = [95, 95, 95]
ufo4triColour_GREEN = [40, 206, 37]
ufo4triColour_LIGHT_BLUE = [164, 222, 227]
ufo4triColour_WHITE = [255, 255, 255]
ufo4triColour_PINK = [254, 174, 243]
ufo5triColour_GREY = [95, 95, 95]
ufo5triColour_GREEN = [40, 206, 37]
ufo5triColour_LIGHT_BLUE = [164, 222, 227]
ufo5triColour_WHITE = [255, 255, 255]
ufo5triColour_PINK = [254, 174, 243]
triColour_GREY = [95, 95, 95]
triColour_GREEN = [40, 206, 37]
triColour_LIGHT_BLUE = [164, 222, 227]
triColour_WHITE = [255, 255, 255]
triColour_PINK = [254, 174, 243]
triColour_BLUE = [6, 26, 42]
triColour_YELLOW1 = [237, 246, 37]
triColour_YELLOW2 = [237, 246, 37]
triColour_YELLOW3 = [237, 246, 37]
triColour_DARK_GREEN = [75, 83, 32]

# font type
font = pygame.font.SysFont('Calibri', 20, True, False)

# pi for arcs
pi = 21/7

# x and y values for changeable and moving objects
stopSign1_x = 520
stopSign2_x = 580
stopSign3_x = 630
stopSign4_x = 630
stopSign5_x = 580
stopSign6_x = 520
stopSign7_x = 470
stopSign8_x = 470
stopPole1_x = 550
stopPole2_x = 550
text4_x = 493
text5_x = 505
text4_x_change = 1
text5_x_change = 1
stopSign1_x_change = 1
stopSign2_x_change = 1
stopSign3_x_change = 1
stopSign4_x_change = 1
stopSign5_x_change = 1
stopSign6_x_change = 1
stopSign7_x_change = 1
stopSign8_x_change = 1
stopPole1_x_change = 1
stopPole2_x_change = 1
bullet_x = 350
bullet_y = 300
arc1_x = 330
arc1_y = 280
arc2_x = 340
arc2_y = 290
arc3_x = 325
arc3_y = 275
arc4_x = 340
arc4_y = 290
bullet_x_change = 2
bullet_y_change = 2
arc1_x_change = 2
arc1_y_change = 2
arc2_x_change  = 2
arc2_y_change  = 2
arc3_x_change  = 2
arc3_y_change  = 2
arc4_x_change  = 2
arc4_y_change  = 2

# multiple counters to perform specific actions at given times
reload_counter = 0
counter1 = 0
counter2 = 0
counter3 = 0
counter4 = 0
counter5 = 0

# x values for tank to move it
tankBody1x = 50
tankBody2x = 100
tankBody3x = 60
tankBullet1x = 140
tankBullet2x = 170
tankBullet3x = 200
tankWheelx = 100
tankRoofx = 150
tankArm1x = 200
tankArm2x = 300
tankShooterx = 300

# empty UFO list
UFOlist = []

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
  
## Main Program Loop
while not done:
    ## CONTROL
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    ## VIEW
    # Clear screen
    screen.fill(WHITE)

    # Draw
    ##Sky
    drawSky()
    
    ##Road
    drawRoad()

    ##Ground
    drawGround()

    ##Moon
    Moon = pygame.image.load("graphics/moon.png").convert()
    Moon.set_colorkey(BLACK)
    Moon = pygame.transform.scale(Moon, (175, 125))
    screen.blit(Moon, [0, 10])
  
    ##StopSign
    pygame.draw.line(screen, BROWN, [stopPole1_x, 540],[stopPole2_x, 600], 20)
    pygame.draw.polygon(screen, RED, [[stopSign1_x, 380], [stopSign2_x, 380], [stopSign3_x, 430], [stopSign4_x, 490], [stopSign5_x, 540], [stopSign6_x, 540], [stopSign7_x, 490], [stopSign8_x, 430]])
    pygame.draw.polygon(screen, WHITE, [[stopSign1_x, 380], [stopSign2_x, 380], [stopSign3_x, 430], [stopSign4_x, 490], [stopSign5_x, 540], [stopSign6_x, 540], [stopSign7_x, 490], [stopSign8_x, 430]], 5)
  
    # assign stop sign changes
    stopSign1_x += stopSign1_x_change 
    stopSign2_x += stopSign2_x_change 
    stopSign3_x += stopSign3_x_change 
    stopSign4_x += stopSign4_x_change 
    stopSign5_x += stopSign5_x_change 
    stopSign6_x += stopSign6_x_change 
    stopSign7_x += stopSign7_x_change 
    stopSign8_x += stopSign8_x_change
    stopPole1_x += stopPole1_x_change
    stopPole2_x += stopPole2_x_change
    text4_x += text4_x_change
    text5_x += text5_x_change
  
    # move stop sign opposite direction when it hits the edge
    if(stopSign3_x == 800):
      stopSign1_x_change *= -1
      stopSign2_x_change *= -1
      stopSign3_x_change *= -1
      stopSign4_x_change *= -1
      stopSign5_x_change *= -1
      stopSign6_x_change *= -1
      stopSign7_x_change *= -1
      stopSign8_x_change *= -1
      stopPole1_x_change *= -1
      stopPole2_x_change *= -1
      text5_x_change *= -1
      text4_x_change *= -1

    # move stop sign opposite direction when it an x value of 450
    if(stopSign8_x == 450):
      stopSign1_x_change *= -1
      stopSign2_x_change *= -1
      stopSign3_x_change *= -1
      stopSign4_x_change *= -1
      stopSign5_x_change *= -1
      stopSign6_x_change *= -1
      stopSign7_x_change *= -1
      stopSign8_x_change *= -1
      stopPole1_x_change *= -1
      stopPole2_x_change *= -1
      text5_x_change *= -1
      text4_x_change *= -1
      
    ##Stars
    for x_offset in range(0, 800, 150):
      for y_offset in range(0, 201, 100):
        
      # add smaller image of stars
        Stars = pygame.image.load("graphics/stars.png").convert()
        Stars.set_colorkey(BLACK)
        Stars = pygame.transform.scale(Stars, (10, 10))
        screen.blit(Stars, [0+x_offset, 10+y_offset])

        # create other stars with polygon
        pygame.draw.polygon(screen, WHITE, [[15 + x_offset, 15 + y_offset], [20 + x_offset, 20 + y_offset], [25 + x_offset, 20 + y_offset], [20 + x_offset, 25 + y_offset], [25 + x_offset, 30 + y_offset], [15 + x_offset, 27 + y_offset], [5 + x_offset, 30 + y_offset], [10 + x_offset, 25 + y_offset], [5 + x_offset, 20 + y_offset], [10 + x_offset, 20 + y_offset]])

    ## UFO
    # dispurse the UFOs
    while (counter1 < 1):
      x1_random = 100
      y1_random = 100
      counter1 = 1
    while (counter2 < 1):
      x2_random = 0
      y2_random = -60
      counter2 = 1
    while (counter3 < 1):
      x3_random = -150
      y3_random = 0
      counter3 = 1
    while (counter4 < 1):
      x4_random = -260
      y4_random = -20
      counter4 = 1
    while (counter5 < 1):
      x5_random = -200
      y5_random = 100
      counter5 = 1

    # create all five UFOs
    ufo1 = drawUFO(x1_random, y1_random, ufo1triColour_GREY, ufo1triColour_GREEN, ufo1triColour_LIGHT_BLUE, ufo1triColour_WHITE, ufo1triColour_PINK)
    ufo2 = drawUFO(x2_random, y2_random, ufo2triColour_GREY, ufo2triColour_GREEN, ufo2triColour_LIGHT_BLUE, ufo2triColour_WHITE, ufo2triColour_PINK)
    ufo3 = drawUFO(x3_random, y3_random, ufo3triColour_GREY, ufo3triColour_GREEN, ufo3triColour_LIGHT_BLUE, ufo3triColour_WHITE, ufo3triColour_PINK)
    ufo4 = drawUFO(x4_random, y4_random, ufo4triColour_GREY, ufo4triColour_GREEN, ufo4triColour_LIGHT_BLUE, ufo4triColour_WHITE, ufo4triColour_PINK)
    ufo5 = drawUFO(x5_random, y5_random, ufo5triColour_GREY, ufo5triColour_GREEN, ufo5triColour_LIGHT_BLUE, ufo5triColour_WHITE, ufo5triColour_PINK)

    # append all the UFO's to the UFO list
    UFOlist.append(ufo1)
    UFOlist.append(ufo2)
    UFOlist.append(ufo3)
    UFOlist.append(ufo4)
    UFOlist.append(ufo5)
    
    ##"STOP" word
    text4 = font.render("UFO Ahead!",True,WHITE)
    screen.blit(text4, [text4_x,450])
    if (triColour_GREY[0] == 6):
      text4 = font.render("UFO Ahead!",True,RED)
      screen.blit(text4, [text4_x,450])
      text5 = font.render("BEWARE!",True,WHITE)
      screen.blit(text5, [text5_x,450])

    ##Tank
    # create tank body
    pygame.draw.ellipse(screen, DARK_GREEN, [tankBody1x,450,250,80])
    pygame.draw.ellipse(screen, DARK_GREEN, [tankBody2x, 400, 150, 100])
    pygame.draw.ellipse(screen, BLACK, [tankBody3x,460,230,60], 5)

    # Create multiple tank wheels
    for x_offset in range(0, 200, 50):
      pygame.draw.circle(screen, GREY, [tankWheelx+x_offset, 490], 15)
      
    # create tank roof, arm, and shooter
    pygame.draw.rect(screen, DARK_GREEN, [tankRoofx, 390, 50, 20])
    pygame.draw.line(screen, DARK_GREEN, [tankArm1x, 450], [tankArm2x, 350], 20)
    pygame.draw.circle(screen, triColour_DARK_GREEN, [tankShooterx, 350], 20)

    # Creating Ammo for Tank
    pygame.draw.circle(screen, triColour_YELLOW1, [tankBullet1x, 430], 20)
    pygame.draw.circle(screen, triColour_YELLOW2, [tankBullet2x, 430], 20)
    pygame.draw.circle(screen, triColour_YELLOW3, [tankBullet3x, 430], 20)
  
    # assign different messages to number of misses as well as make shots "disappear" as being shot accordingly 
# if all UFO's are dead
    if (ufo1triColour_GREY == BLUE and      ufo1triColour_GREEN == BLUE and ufo1triColour_LIGHT_BLUE == BLUE and ufo1triColour_WHITE == BLUE and 
ufo1triColour_PINK == BLUE and ufo2triColour_GREY == BLUE and      ufo2triColour_GREEN == BLUE and ufo2triColour_LIGHT_BLUE == BLUE and ufo2triColour_WHITE == BLUE and 
ufo2triColour_PINK == BLUE and ufo3triColour_GREY == BLUE and      ufo3triColour_GREEN == BLUE and ufo3triColour_LIGHT_BLUE == BLUE and ufo3triColour_WHITE == BLUE and 
ufo3triColour_PINK == BLUE and ufo4triColour_GREY == BLUE and      ufo4triColour_GREEN == BLUE and ufo4triColour_LIGHT_BLUE == BLUE and ufo4triColour_WHITE == BLUE and 
ufo4triColour_PINK == BLUE and ufo5triColour_GREY == BLUE and      ufo5triColour_GREEN == BLUE and ufo5triColour_LIGHT_BLUE == BLUE and ufo5triColour_WHITE == BLUE and 
ufo5triColour_PINK == BLUE):
      text0 = font.render("Completed The Mission!",True,WHITE)
      screen.blit(text0, [tankRoofx-100,350])    
    # if tank missed once
    elif (reload_counter == 1):
      triColour_YELLOW1[0] = 75
      triColour_YELLOW1[1] = 83
      triColour_YELLOW1[2] = 32
      text1 = font.render("KEEP SHOOTING!",True,WHITE)
      screen.blit(text1, [tankRoofx-50,350])
      
    # if tank missed twice
    elif (reload_counter == 2):
      triColour_YELLOW2[0] = 75
      triColour_YELLOW2[1] = 83
      triColour_YELLOW2[2] = 32
      text2 = font.render("ALMOST THERE!",True,WHITE)
      screen.blit(text2, [tankRoofx-50,350])
      
    # if tank missed three times
    elif (reload_counter == 3):
      triColour_YELLOW3[0] = 75
      triColour_YELLOW3[1] = 83
      triColour_YELLOW3[2] = 32
      text3 = font.render("!!!!!!",True,WHITE)
      screen.blit(text3, [tankRoofx,350])
      
    # reset the counter to 0 and reset the shots to appear on the screen again
    elif (reload_counter == 4):
      reload_counter = 0
      triColour_YELLOW1 = [237, 246, 37]
      triColour_YELLOW2 = [237, 246, 37]
      triColour_YELLOW3 = [237, 246, 37]
      triColour_DARK_GREEN = [75, 83, 32]

    # movement for the tank using arrow keys
    if event.type == pygame.QUIT: 
      done = True
    elif (event.type == pygame.KEYDOWN):
        if (event.key == pygame.K_RIGHT):
          tankBody1x = tankBody1x + 5
          tankBody2x = tankBody2x + 5
          tankBody3x = tankBody3x + 5
          tankBullet1x = tankBullet1x + 5
          tankBullet2x = tankBullet2x + 5
          tankBullet3x = tankBullet3x + 5
          tankWheelx = tankWheelx + 5
          tankRoofx = tankRoofx + 5
          tankArm1x = tankArm1x + 5
          tankArm2x = tankArm2x + 5
          tankShooterx = tankShooterx + 5
        elif (event.key == pygame.K_LEFT):
          tankBody1x = tankBody1x - 5
          tankBody2x = tankBody2x - 5
          tankBody3x = tankBody3x - 5
          tankBullet1x = tankBullet1x - 5
          tankBullet2x = tankBullet2x - 5
          tankBullet3x = tankBullet3x - 5
          tankWheelx = tankWheelx - 5
          tankRoofx = tankRoofx - 5
          tankArm1x = tankArm1x - 5
          tankArm2x = tankArm2x - 5
          tankShooterx = tankShooterx - 5
          
    # Create tank shot
    pygame.draw.circle(screen, YELLOW, [bullet_x, bullet_y], 15)
    pygame.draw.arc(screen, LIGHT_BLUE, [arc1_x,arc1_y,30,30],  pi/2,     pi, 2)
    pygame.draw.arc(screen, LIGHT_BLUE,   [arc2_x,arc2_y,30,30],3*pi/2,   2*pi, 2)
    pygame.draw.arc(screen, LIGHT_BLUE, [arc3_x,arc3_y,35,35],  pi/2,     pi, 2)
    pygame.draw.arc(screen, LIGHT_BLUE,   [arc4_x,arc4_y,35,35],3*pi/2,   2*pi, 2)
  
    # make tank shot move diagonally up to the right
    bullet_x += bullet_x_change
    bullet_y -= bullet_y_change
    arc1_x += arc1_x_change
    arc1_y -= arc1_y_change
    arc2_x += arc2_x_change
    arc2_y -= arc2_y_change
    arc3_x += arc3_x_change
    arc3_y -= arc3_y_change
    arc4_x += arc4_x_change
    arc4_y -= arc4_y_change
  
    # if bullet hits the UFO 1
    if (bullet_x > 400+x1_random and bullet_x < 525 + x1_random and bullet_y > 100+y1_random and bullet_y < 150+y1_random):
      ufo1triColour_GREY = BLUE
      ufo1triColour_GREEN = BLUE
      ufo1triColour_LIGHT_BLUE = BLUE
      ufo1triColour_WHITE = BLUE 
      ufo1triColour_PINK = BLUE

    # if bullet hits the UFO 2
    elif (bullet_x > 400+x2_random and bullet_x < 525 + x2_random and bullet_y > 100+y2_random and bullet_y < 150+y2_random):
      ufo2triColour_GREY = BLUE
      ufo2triColour_GREEN = BLUE
      ufo2triColour_LIGHT_BLUE = BLUE
      ufo2triColour_WHITE = BLUE 
      ufo2triColour_PINK = BLUE

    # if bullet hits the UFO 3
    elif (bullet_x > 400+x3_random and bullet_x < 525 + x3_random and bullet_y > 100+y3_random and bullet_y < 150+y3_random):
      ufo3triColour_GREY = BLUE
      ufo3triColour_GREEN = BLUE
      ufo3triColour_LIGHT_BLUE = BLUE
      ufo3triColour_WHITE = BLUE 
      ufo3triColour_PINK = BLUE

    # if bullet hits the UFO 4
    elif (bullet_x > 400+x4_random and bullet_x < 525 + x4_random and bullet_y > 100+y4_random and bullet_y < 150+y4_random):
      ufo4triColour_GREY = BLUE
      ufo4triColour_GREEN = BLUE
      ufo4triColour_LIGHT_BLUE = BLUE
      ufo4triColour_WHITE = BLUE 
      ufo4triColour_PINK = BLUE

    # if bullet hits the UFO 5
    elif (bullet_x > 400+x5_random and bullet_x < 525 + x5_random and bullet_y > 100+y5_random and bullet_y < 150+y5_random):
      ufo5triColour_GREY = BLUE
      ufo5triColour_GREEN = BLUE
      ufo5triColour_LIGHT_BLUE = BLUE
      ufo5triColour_WHITE = BLUE 
      ufo5triColour_PINK = BLUE

     # if the bullet goes off the screen then reset the bullet and add to the miss counter
    if (bullet_y < 0):
      bullet_x = 350
      bullet_y = 300
      arc1_x = 330
      arc1_y = 280
      arc2_x = 340
      arc2_y = 290
      arc3_x = 325
      arc3_y = 275
      arc4_x = 340
      arc4_y = 290
      triColour_GREY = [95, 95, 95]
      triColour_GREEN = [40, 206, 37]
      triColour_LIGHT_BLUE = [164, 222, 227]
      triColour_WHITE = [255, 255, 255]
      triColour_PINK = [254, 174, 243]
      reload_counter += 1
      bullet_x = tankShooterx+10
      arc1_x = bullet_x - 20
      arc2_x = bullet_x - 10
      arc3_x = bullet_x - 25
      arc4_x = bullet_x - 10
    
    ##Update Screen
    pygame.display.flip()
    clock.tick(60)

# Close the window and quit
pygame.quit()
