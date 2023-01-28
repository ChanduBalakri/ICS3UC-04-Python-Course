"""
 Pygame base template for opening a window
 @author Chandresh Balakrishnan
 @class ICS3UC
 @date 31-05-2022
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
# pygame setup 
import pygame

# random setup
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# rectangle parent class
class Rectangle():
  def __init__(self):
    # self.x variable
    self.x = random.randint(0, 700)
    # self.y variable
    self.y = random.randint(0, 500)
    # self.x2 variable
    self.x2 = random.randint(0, 700)
    # self.y2 variable
    self.y2 = random.randint(0, 500)
    # self.x3 variable
    self.x3 = random.randint(0, 700)
    # self.y3 variable
    self.y3 = random.randint(0, 500)
    # self.length variable
    self.length = random.randint(20, 70)
    # self.width variable
    self.width = random.randint(20, 70)
    # self.radius variable
    self.radius = random.randint(20, 70)
    # self.lineLength variable for lines
    self.lineLength = random.randint(10, 20)
    # self.change_x variable for movement
    self.change_x = random.randint(1, 10)
    # self.change_y variable for movement
    self.change_y = random.randint(1, 10)
    # self.thickness variable
    self.thickness = random.randint(5,10)
    # self.colour changeable variable
    self.colour = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]
    
  # drawing method
  def drawing(self):
    pygame.draw.rect(screen, self.colour, [self.x, self.y, self.length, self.width], self.thickness)
    
  # movement method
  def move(self):
    self.x = self.x + self.change_x
    self.y = self.y + self.change_y
    self.x2 = self.x2 + self.change_x
    self.y2 = self.y2 + self.change_y
    self.x3 = self.x3 + self.change_x
    self.y3 = self.y3 + self.change_y
    
    ##dont let shapes exit the screen
    # if self.x exits the screen
    if (self.x > 700):
      self.change_x = self.change_x * -1
      self.colour = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    if (self.x < 0):
      self.change_x = self.change_x * -1
      self.colour = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

    # if self.y exits the screen
    if (self.y > 500):
      self.change_y = self.change_y * -1
      self.colour = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    if (self.y < 0):
      self.change_y = self.change_y * -1
      self.colour = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

# ellipse child class    
class Ellipse(Rectangle):
  def drawing(self):
    pygame.draw.ellipse(screen, self.colour, [self.x, self.y, self.length, self.width], self.thickness)
  
# circle child class
class Circle(Rectangle):
  def drawing(self):
    pygame.draw.circle(screen, self.colour, [self.x, self.y], self.radius, self.thickness)

# line child class
#class Line(Rectangle):
  #def drawing(self):
    #pygame.draw.line(screen, self.colour, [self.x, self.y], [self.x2, self.y2], self.lineLength)

# polygon child class
class Polygon(Rectangle):
  def drawing(self):
    pygame.draw.polygon(screen, self.colour, [[self.x, self.y], [self.x2, self.y2], [self.x3, self.y3]], self.thickness)

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Chandresh Lab 12")

# Patrick child class
class Patrick(Rectangle):
  def drawing(self):
    PatrickImage = pygame.image.load("graphics/Patrick.png").convert()
    PatrickImage.set_colorkey(BLACK)
    PatrickImage =  pygame.transform.scale(PatrickImage, (100, 100))
    screen.blit(PatrickImage, [self.x, self.y])

# Shrek child class
class Shrek(Rectangle):
  def drawing(self):
    ShrekImage = pygame.image.load("graphics/shrek.jpeg").convert()
    ShrekImage.set_colorkey(BLACK)
    ShrekImage =  pygame.transform.scale(ShrekImage, (100, 100))
    screen.blit(ShrekImage, [self.x, self.y])
pygame.init()

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# create empty list
my_list = []

# create rectangles and append to list
for i in range(10):
  my_object = Rectangle()
  my_list.append(my_object)

# create ellipses and append to list
for i in range(10):
  my_object = Ellipse()
  my_list.append(my_object)

# create circles and append to list
for i in range(10):
  my_object = Circle()
  my_list.append(my_object)
  
# create lines and append to list  
#for i in range(10):
  #my_object = Line()
  #my_list.append(my_object)

# create polygons and append to list
for i in range(10):
  my_object = Polygon()
  my_list.append(my_object)

# create patricks and append to list
for i in range(20):
  my_object = Patrick()
  my_list.append(my_object)

# create shreks and append to list
for i in range(20):
  my_object = Shrek()
  my_list.append(my_object)
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
    # --- Drawing code should go here
    # call drawing and move methods for each item in the list

    # loop through each item in my_list and draw and move them
    for i in range(len(my_list)):
      my_list[i].drawing()
      my_list[i].move()

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()