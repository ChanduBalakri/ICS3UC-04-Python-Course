##
# Pygame base template for opening a window
# MVC version
#
# @author Chandresh Balakrishnan
# @course ICS3UC
# @date 2022/05/21 Last modified
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
font = pygame.font.SysFont('Calibri', 20, True, False)
pi = 21/7
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
bullet_x_change = 0.5
bullet_y_change = 0.5
arc1_x_change = 0.5
arc1_y_change = 0.5
arc2_x_change  = 0.5
arc2_y_change  = 0.5
arc3_x_change  = 0.5
arc3_y_change  = 0.5
arc4_x_change  = 0.5
arc4_y_change  = 0.5
reload_counter = 0

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
    pygame.draw.rect(screen, triColour_BLUE, [0, 0, 800, 300])
    
    ##Road
    pygame.draw.rect(screen, BLACK, [0, 300, 800, 400])

    ##Ground
    pygame.draw.rect(screen, GREY, [0, 550, 800, 50])

    ##Moon
    pygame.draw.circle(screen, YELLOW, [100, 75], 40)
    pygame.draw.ellipse(screen, triColour_BLUE, [80, 20, 100, 100])

    ##Road Lines
    for x_offset in range(0, 601, 200):
      pygame.draw.line(screen, YELLOW, [25 + x_offset, 425], [100 + x_offset, 425], 10)
      
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
        pygame.draw.polygon(screen, WHITE, [[15 + x_offset, 15 + y_offset], [20 + x_offset, 20 + y_offset], [25 + x_offset, 20 + y_offset], [20 + x_offset, 25 + y_offset], [25 + x_offset, 30 + y_offset], [15 + x_offset, 27 + y_offset], [5 + x_offset, 30 + y_offset], [10 + x_offset, 25 + y_offset], [5 + x_offset, 20 + y_offset], [10 + x_offset, 20 + y_offset]])

    ##UFO
    # Create UFO Beams
    for y_offset in range(0, 50, 10):
      pygame.draw.line(screen, triColour_GREEN, [525, 100], [300, 500+y_offset])
    for y_offset in range(0, 50, 10):
      pygame.draw.line(screen, triColour_GREEN, [570, 100], [400, 500+y_offset])
    for y_offset in range(0, 50, 10): 
      pygame.draw.line(screen, triColour_GREEN, [550, 100], [350, 500+y_offset])
      
    # Create UFO Body
    pygame.draw.ellipse(screen, triColour_GREY, [400, 100, 250, 100]) 
    pygame.draw.ellipse(screen, triColour_GREEN, [400, 100, 250, 100],10) 
    pygame.draw.ellipse(screen, triColour_GREY, [475, 75, 100, 100])  

    # Create UFO Windows
    pygame.draw.circle(screen, triColour_LIGHT_BLUE, [460, 150], 15)
    pygame.draw.circle(screen, triColour_WHITE, [460, 150], 15, 2)
    pygame.draw.circle(screen, triColour_LIGHT_BLUE, [525, 160], 15)
    pygame.draw.circle(screen, triColour_WHITE, [525, 160], 15, 2)
    pygame.draw.circle(screen, triColour_LIGHT_BLUE, [590, 150], 15)
    pygame.draw.circle(screen, triColour_WHITE, [590, 150], 15, 2)
    pygame.draw.ellipse(screen, triColour_LIGHT_BLUE, [490, 85, 70, 40])
    pygame.draw.ellipse(screen, triColour_WHITE, [490, 85, 70, 40], 2)
  
    # fade away the UFO to the background colour of the sky
    # fade away body
    if (triColour_GREY[0] > 6):
      triColour_GREY[0] -= 1
    if (triColour_GREY[1] > 26):
      triColour_GREY[1] -= 1
    if (triColour_GREY[2] > 42):
      triColour_GREY[2] -= 1
    # fade away glowing ring and beams
    if (triColour_GREEN[0] > 6):
      triColour_GREEN[0] -= 1
    if (triColour_GREEN[1] > 26):
      triColour_GREEN[1] -= 1
    if (triColour_GREEN[2] < 42):
      triColour_GREEN[2] += 1
    # fade away windows
    if (triColour_WHITE[0] > 6):
      triColour_WHITE[0] -= 1
    if (triColour_WHITE[1] > 26):
      triColour_WHITE[1] -= 1
    if (triColour_WHITE[2] > 42):
      triColour_WHITE[2] -= 1
    if (triColour_LIGHT_BLUE[0] > 6):
      triColour_LIGHT_BLUE[0] -= 1
    if (triColour_LIGHT_BLUE[1] > 26):
      triColour_LIGHT_BLUE[1] -= 1
    if (triColour_LIGHT_BLUE[2] > 42):
      triColour_LIGHT_BLUE[2] -= 1
    # fade away arcs
    if (triColour_PINK[0] > 6):
      triColour_PINK[0] -= 1
    if (triColour_PINK[1] > 26):
      triColour_PINK[1] -= 1
    if (triColour_PINK[2] > 42):
      triColour_PINK[2] -= 1
      
    # These arcs imply the direction of movement of the UFO, not just random arcs
    pygame.draw.arc(screen, triColour_PINK, [400,80,300,200], 0, pi/2, 2)
    pygame.draw.arc(screen, triColour_PINK, [380,50,350,250], 0, pi/2, 2)
  
    ##Tank
    pygame.draw.ellipse(screen, DARK_GREEN, [50,450,250,80])
    pygame.draw.ellipse(screen, DARK_GREEN, [100, 400, 150, 100])
    pygame.draw.ellipse(screen, BLACK, [60,460,230,60], 5)
    pygame.draw.circle(screen, YELLOW, [140, 430], 20)
    pygame.draw.circle(screen, YELLOW, [170, 430], 20)
    pygame.draw.circle(screen, YELLOW, [200, 430], 20)
  
    # Create multiple tank wheels
    for x_offset in range(0, 200, 50):
      pygame.draw.circle(screen, GREY, [100+x_offset, 490], 15)
    pygame.draw.rect(screen, DARK_GREEN, [150, 390, 50, 20])
    pygame.draw.line(screen, DARK_GREEN, [200, 450], [300, 350], 20)
    pygame.draw.circle(screen, triColour_DARK_GREEN, [300, 350], 20)

    # Creating Ammo for Tank
    pygame.draw.circle(screen, triColour_YELLOW1, [140, 430], 20)
    pygame.draw.circle(screen, triColour_YELLOW2, [170, 430], 20)
    pygame.draw.circle(screen, triColour_YELLOW3, [200, 430], 20)
    # assign different messages to number of misses as well as make shots "disappear" as being shot accordingly 
    # if tank missed once
    if (reload_counter == 1):
      triColour_YELLOW1[0] = 75
      triColour_YELLOW1[1] = 83
      triColour_YELLOW1[2] = 32
      text1 = font.render("WE'VE MISSED!",True,WHITE)
      screen.blit(text1, [110,350])
    # if tank missed twice
    if (reload_counter == 2):
      triColour_YELLOW2[0] = 75
      triColour_YELLOW2[1] = 83
      triColour_YELLOW2[2] = 32
      text2 = font.render("TRY AGAIN!",True,WHITE)
      screen.blit(text2, [120,350])
    # if tank missed three times
    if (reload_counter == 3):
      triColour_YELLOW3[0] = 75
      triColour_YELLOW3[1] = 83
      triColour_YELLOW3[2] = 32
      text3 = font.render("AARGH!",True,WHITE)
      screen.blit(text3, [135,350])
    # reset the counter to 0 and reset the shots to appear on the screen again
    if (reload_counter == 4):
      reload_counter = 0
      triColour_YELLOW1 = [237, 246, 37]
      triColour_YELLOW2 = [237, 246, 37]
      triColour_YELLOW3 = [237, 246, 37]
      triColour_DARK_GREEN = [75, 83, 32]
      
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
      
    ##"STOP" word
    text4 = font.render("UFO Ahead!",True,WHITE)
    screen.blit(text4, [text4_x,450])
    if (triColour_GREY[0] == 6):
      text4 = font.render("UFO Ahead!",True,RED)
      screen.blit(text4, [text4_x,450])
      text5 = font.render("BEWARE!",True,WHITE)
      screen.blit(text5, [text5_x,450])

    ##Update Screen
    pygame.display.flip()
    clock.tick(60)

# Close the window and quit
pygame.quit()
