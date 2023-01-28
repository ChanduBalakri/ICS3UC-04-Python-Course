##
# Pygame base template for opening a window
# MVC version
#
# @author Chandresh Balakrishnan
# @course ICS3UC
# @date 2022/05/18 Last modified
#
# Simpson College Computer Science
# http://programarcadegames.com/
# http://simpson.edu/computer-science/
##

## Pygame setup
import pygame


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
font = pygame.font.SysFont('Calibri', 20, True, False)
pi = 21/7

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
    pygame.draw.rect(screen, BLUE, [0, 0, 800, 300])

    ##Road
    pygame.draw.rect(screen, BLACK, [0, 300, 800, 400])

    ##Ground
    pygame.draw.rect(screen, GREY, [0, 550, 800, 50])

    ##Moon
    pygame.draw.circle(screen, YELLOW, [100, 75], 40)
    pygame.draw.ellipse(screen, BLUE, [80, 20, 100, 100])

    ##Road Lines
    for x_offset in range(0, 601, 200):
      pygame.draw.line(screen, YELLOW, [25 + x_offset, 425], [100 + x_offset, 425], 10)
      
    ##StopSign
    pygame.draw.line(screen, BROWN, [550, 540],[550, 600], 20)
    pygame.draw.polygon(screen, RED, [[520, 380], [580, 380], [630, 430], [630, 490], [580, 540], [520, 540], [470, 490], [470, 430]])
    pygame.draw.polygon(screen, WHITE, [[520, 380], [580, 380], [630, 430], [630, 490], [580, 540], [520, 540], [470, 490], [470, 430]], 5)
    
    
    ##Stars
    for x_offset in range(0, 800, 150):
      for y_offset in range(0, 201, 100):        pygame.draw.polygon(screen, WHITE, [[15 + x_offset, 15 + y_offset], [20 + x_offset, 20 + y_offset], [25 + x_offset, 20 + y_offset], [20 + x_offset, 25 + y_offset], [25 + x_offset, 30 + y_offset], [15 + x_offset, 27 + y_offset], [5 + x_offset, 30 + y_offset], [10 + x_offset, 25 + y_offset], [5 + x_offset, 20 + y_offset], [10 + x_offset, 20 + y_offset]])

    ##UFO
    # Create UFO Beams
    for y_offset in range(0, 50, 10):
      pygame.draw.line(screen, GREEN, [525, 100], [300, 500+y_offset])
    for y_offset in range(0, 50, 10):
      pygame.draw.line(screen, GREEN, [570, 100], [400, 500+y_offset])
    for y_offset in range(0, 50, 10): 
      pygame.draw.line(screen, GREEN, [550, 100], [350, 500+y_offset])
      
    # Create UFO Body
    pygame.draw.ellipse(screen, GREY, [400, 100, 250, 100]) 
    pygame.draw.ellipse(screen, GREEN, [400, 100, 250, 100],10) 
    pygame.draw.ellipse(screen, GREY, [475, 75, 100, 100])  

    # Create UFO Windows
    pygame.draw.circle(screen, LIGHT_BLUE, [460, 150], 15)
    pygame.draw.circle(screen, WHITE, [460, 150], 15, 2)
    pygame.draw.circle(screen, LIGHT_BLUE, [525, 160], 15)
    pygame.draw.circle(screen, WHITE, [525, 160], 15, 2)
    pygame.draw.circle(screen, LIGHT_BLUE, [590, 150], 15)
    pygame.draw.circle(screen, WHITE, [590, 150], 15, 2)
    pygame.draw.ellipse(screen, LIGHT_BLUE, [490, 85, 70, 40])
    pygame.draw.ellipse(screen, WHITE, [490, 85, 70, 40], 2)

    # These arcs imply the direction of movement of the UFO, not just random arcs
    pygame.draw.arc(screen, PINK, [400,80,300,200], 0, pi/2, 2)
    pygame.draw.arc(screen, PINK, [380,50,350,250], 0, pi/2, 2)
  
    ##Tank
    pygame.draw.ellipse(screen, DARK_GREEN, [50,450,250,80])
    pygame.draw.ellipse(screen, DARK_GREEN, [100, 400, 150, 100])
    pygame.draw.ellipse(screen, BLACK, [60,460,230,60], 5)
  
    # Create multiple tank wheels
    for x_offset in range(0, 200, 50):
      pygame.draw.circle(screen, GREY, [100+x_offset, 490], 15)
    pygame.draw.rect(screen, DARK_GREEN, [150, 390, 50, 20])
    pygame.draw.line(screen, DARK_GREEN, [200, 450], [300, 350], 20)
    pygame.draw.circle(screen, DARK_GREEN, [300, 350], 20)

    # Create tank shot
    pygame.draw.circle(screen, YELLOW, [350, 300], 15)
    pygame.draw.arc(screen, LIGHT_BLUE, [330,280,30,30],  pi/2,     pi, 2)
    pygame.draw.arc(screen, LIGHT_BLUE,   [340,290,30,30],3*pi/2,   2*pi, 2)
    pygame.draw.arc(screen, LIGHT_BLUE, [325,275,35,35],  pi/2,     pi, 2)
    pygame.draw.arc(screen, LIGHT_BLUE,   [340,290,35,35],3*pi/2,   2*pi, 2)
  
    ##"STOP" word
    text = font.render("UFO Ahead!",True,WHITE)
    screen.blit(text, [493,450])
  
    ##Update Screen
    pygame.display.flip()
    clock.tick(60)

# Close the window and quit
pygame.quit()
