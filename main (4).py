##
# Tank Stars
# @author: Chandresh
# @course: ICS3UC
# @date: 22/06/2022
# @teacher: Mr. Reid

# import libraries
import pygame
import random

## Classes
# Player class
class Player(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """
   
    # -- Methods
    def __init__(self, x, y, file, width, height, color):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()
        self.degrees = 270
        # Set height, width
        self.image = pygame.image.load(file).convert()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.image = pygame.transform.rotate(self.image, self.degrees)
        self.image1 = self.image
        self.image.set_colorkey(color)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
 
        # -- Attributes
        # Set speed vector
        self.change_x = 0
        self.change_y = 0
 
    def changespeedDown(self, x, y, z):
        """ Change the speed of the player"""
        self.change_x += x
        self.change_y += y
        self.degrees = z
        self.image = pygame.transform.rotate(self.image1, self.degrees)

    def changespeedUp(self, x, y):
        """ Change the speed of the player"""
        self.change_x += x
        self.change_y += y
     
    def update(self):
     
        """ Find a new position for the player"""
        self.rect.x += self.change_x
        self.rect.y += self.change_y
     
# NPC class
class NPC(pygame.sprite.Sprite):
  def __init__(self, x, y, width, height, file, color):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()
        # Set height, width
        self.image =  pygame.image.load(file).convert()
        self.image =  pygame.transform.scale(self.image, (width, height))
        self.image.set_colorkey(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
 
        # -- Attributes
        # Set speed vector
        self.change_x = 0
        self.change_y = 0
  def changespeed(self, x, y):
        self.change_x = x
        self.change_y = y

  def update(self):      
        """ Find a new position for the player"""
        self.rect.x += self.change_x
        self.rect.y += self.change_y
         
# Shuriken class
class Shuriken(pygame.sprite.Sprite):
  # -- Methods
    def __init__(self, x, y, file, width, height, color):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()
        self.degrees = 0
        self.image = pygame.image.load(file).convert()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.image = pygame.transform.rotate(self.image, self.degrees)
        self.image.set_colorkey(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.change_x = 0
        self.change_y = 0

    def changespeed(self, x, y, z):
        self.change_x = x
        self.change_y = y
        self.degrees = z
        self.image = pygame.transform.rotate(self.image, self.degrees)

    def update(self):      
        """ Find a new position for the player"""
        self.rect.x += self.change_x
        self.rect.y += self.change_y

# Portal Class
class Portal(pygame.sprite.Sprite):
  # -- Methods
    def __init__(self, x, y, file, width, height, color):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()
        self.image = pygame.image.load(file).convert()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.image.set_colorkey(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.change_x = 0
        self.change_y = 0

# Hellfire class
class Hellfire(pygame.sprite.Sprite):
  # -- Methods
    def __init__(self, x, y, file, width, color):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()
        self.image = pygame.image.load(file).convert()
        self.height = 100
        self.image = pygame.transform.scale(self.image, (width, self.height))
        self.image.set_colorkey(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.change_y = 0
        self.change_x = 0

    def changespeed(self, x):
        self.change_y = x

    def update(self):      
        """ Find a new position for the player"""
        self.height += self.change_y

 
# Cannonball Class
class Cannonball(pygame.sprite.Sprite):
    # -- Methods
    def __init__(self, x, y, file, width, height, color):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()
        self.degrees = 0
        self.image = pygame.image.load(file).convert()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.image = pygame.transform.rotate(self.image, self.degrees)
        self.image.set_colorkey(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.change_x = 0
        self.change_y = 0

    def changespeed(self, x, y, z):
        self.change_x = x
        self.change_y = y
        self.degrees = z
        self.image = pygame.transform.rotate(self.image, self.degrees)

    def update(self):      
        """ Find a new position for the player"""
        self.rect.x += self.change_x
        self.rect.y += self.change_y

   
# Healthbar calss
class Healthbar():
  def __init__(self, color, color2):
      """Constructor function"""
      # Call the parent's constructor
      super().__init__()
      # Set height, width
      self.x = 50
      self.y = 25
      self.x2 = 40
      self.y2 = 30
      self.x3 = 50
      self.y3 = 35
      self.x4 = 750
      self.y4 = 35
      self.x5 = 760
      self.y5 = 30
      self.x6 = 750
      self.y6 = 25
      self.outerx4 = 750
      self.outerx5 = 760
      self.outerx6 = 750
      self.color = color
      self.color2 = color2
  def drawing(self, space):
      pygame.draw.polygon(space, self.color, [[self.x, self.y], [self.x2, self.y2], [self.x3, self.y3], [self.x4, self.y4], [self.x5, self.y5], [self.x6, self.y6]])
      pygame.draw.polygon(space, self.color2, [[self.x, self.y], [self.x2, self.y2], [self.x3, self.y3], [self.outerx4, self.y4], [self.outerx5, self.y5], [self.outerx6, self.y6]], 3)

# Generator class
class Generator(pygame.sprite.Sprite):
  def __init__(self, x, y, file, width, height, color):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()
        self.degrees = 0
        self.image = pygame.image.load(file).convert()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.image = pygame.transform.rotate(self.image, self.degrees)
        self.image.set_colorkey(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.change_x = 0
        self.change_y = 0

  def update(self):      
      """ Find a new position for the player"""
      self.rect.x += self.change_x
      self.rect.y += self.change_y

# Powerup Class
class Powerup(pygame.sprite.Sprite):
  def __init__(self, x, y, file, width, height, color):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()
        self.degrees = 0
        self.image = pygame.image.load(file).convert()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.image = pygame.transform.rotate(self.image, self.degrees)
        self.image.set_colorkey(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.change_x = 0
        self.change_y = 0

  def update(self):      
      """ Find a new position for the player"""
      self.rect.x += self.change_x
      self.rect.y += self.change_y

# Barrier Class
class Barrier(pygame.sprite.Sprite):
  def __init__(self, x, y, file, width, height, color):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()
        self.image = pygame.image.load(file).convert()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.image.set_colorkey(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.change_x = 0
        self.change_y = 0

  def update(self):      
      """ Find a new position for the player"""
      self.rect.x += self.change_x
      self.rect.y += self.change_y
   
   
##Subprograms
# scene1
def scene1(texts):
  background = pygame.image.load("CptImages/backgroundimageScene1.webp").convert()
  background = pygame.transform.scale(background, (800, 600))
  screen.blit(background, [0, 0])
  screen.blit(texts, [365, 45])
 
# scene2
def scene2(texts, x, y):
  background1 = pygame.image.load("CptImages/maze.png").convert()
  background1 = pygame.transform.scale(background1, (800, 600))
  screen.blit(background1, [0, 0])
  screen.blit(texts, [x, y])
 
## Pygame setup
pygame.init()

# set width and height of screen
width = 800
height = 600

# send font of texts
font = pygame.font.SysFont('Helvetica', 15, True, False)

# set base variables to static values
scene = 0
end = 0
health = 700
stopper = "go"
stopper1 = "go"
stopper2 = "go"
stopper3 = "go"
stopper4 = "go"
stopper5 = "go"
stopper6 = "go"
stopper7 = "go"
stopper8 = "go"
stopper9 = "go"
stopper10 = "go"
stopper11 = "go"
stopper12 = "go"
stopper13 = "go"
dontHit = 0
fail = 0
power1 = 0
power2 = 0
power3 = 0
bossShoot1 = 1
bossShoot2 = 1
bossShoot3 = 1
shoot = 0
x1 = 230
y1 = 570
ability = 0
tornado = 0
reset = 0
fire = 0
resetter = 0
connection = 0
reAdd = 0
reAdjust = 1
hellShoot = 0
lifeCounter = 0

#create sounds variables
tornadoSound = pygame.mixer.Sound("CptSounds/tornadoSound.mp3")
cannonballSound = pygame.mixer.Sound("CptSounds/cannonballSound.mp3")

#create the screen
screen = pygame.display.set_mode((width,height))

# set the name of the window
pygame.display.set_caption("Tank Stars!")

## MODEL - Data used in the system
# Define some colors
BLACK    = (0, 0, 0)
WHITE    = (255, 255, 255)
BLUE     = (0, 0, 255)
GREEN    = (0, 255, 0)
RED      = (255, 0, 0)
GREY = (141, 141, 141)
YELLOW = (224,196,87)

# Loop until the user clicks the close button.
done = False

# create text of level boss
text = font.render("Elden Lord",True,WHITE)

# create empty sprite groups
shuriken1SpritesGroup = pygame.sprite.Group()
shuriken2SpritesGroup = pygame.sprite.Group()
shuriken3SpritesGroup = pygame.sprite.Group()
playerSpritesGroup = pygame.sprite.Group()
cannonSpritesGroup = pygame.sprite.Group()
allSpritesGroup1 = pygame.sprite.Group()
allSpritesGroup = pygame.sprite.Group()
npcSpritesGroup = pygame.sprite.Group()
npcSpritesGroup1 = pygame.sprite.Group()
portalSpritesGroup = pygame.sprite.Group()
allSpritesGroup2 = pygame.sprite.Group()
chargerSpritesGroup = pygame.sprite.Group()
charger1SpritesGroup = pygame.sprite.Group()
charger2SpritesGroup = pygame.sprite.Group()
charger3SpritesGroup = pygame.sprite.Group()
powerupSpritesGroup = pygame.sprite.Group()
hellfireSpritesGroup = pygame.sprite.Group()
barrierHorizontal1SpritesGroup = pygame.sprite.Group()
barrierHorizontal2SpritesGroup = pygame.sprite.Group()
barrierVertical1SpritesGroup = pygame.sprite.Group()
barrierVertical2SpritesGroup = pygame.sprite.Group()

# clock to include frames
clock = pygame.time.Clock()

# create the sprites for scene 0
person = Player(500, 550, "CptImages/TopDownTank.png", 50, 50, BLACK)
npc = NPC(700, 510, 90, 90, "CptImages/NPC1.png", WHITE)

# add the sprites for scene 0
allSpritesGroup.add(person)
allSpritesGroup.add(npc)
npcSpritesGroup.add(npc)

# create a healthbar
healthbar = Healthbar(RED, WHITE)

# create the sprites for scene 1
person1 = Player(160, 300, 'CptImages/fightTank.png', 150, 150, BLACK)
playerHitbox = Player(170, 355, 'CptImages/Black.png', 60, 100, BLACK)
person1.changespeedDown(0, 0, 90)
npc1 = NPC(465, 120, 180, 180, "CptImages/NPC1.png", WHITE)
npc1Hitbox = NPC(540, 140, 20, 140, "CptImages/Black.png", BLACK)
shuriken1 = Shuriken(npc1.rect.x, npc1.rect.y+100, "CptImages/shuriken.png", 20, 20, BLACK)
shuriken2 = Shuriken(npc1.rect.x+25, npc1.rect.y+50, "CptImages/shuriken.png", 20, 20, BLACK)
shuriken3 = Shuriken(npc1.rect.x+50, npc1.rect.y+50, "CptImages/shuriken.png", 20, 20, BLACK)
cannonball = Cannonball(person1.rect.x+155, person1.rect.y+7, "CptImages/cannonball.gif", 35, 35, BLACK)
portal = Portal(random.randrange(0,800), 420, "CptImages/portal.png", 100, 100, BLACK)
hellfire = Hellfire(portal.rect.x, -50, "CptImages/hellfire.png", 100, BLACK)
tornadoMove = Shuriken(person1.rect.x+150, person1.rect.y-50, "CptImages/tornadoMove.png", 150, 150, BLACK)
fireball = Cannonball(person1.rect.x+155, person1.rect.y+7, "CptImages/fireball.png", 35, 35, BLACK)
fireball.changespeed(0, 0, 180)
tornadoMoveHitbox = Shuriken(person1.rect.x+212, person1.rect.y-50, "CptImages/Black.png", 30, 150, BLACK)

# add the sprites to scene 1
allSpritesGroup1.add(person1)
allSpritesGroup1.add(playerHitbox)
allSpritesGroup1.add(npc1)
allSpritesGroup1.add(npc1Hitbox)
npcSpritesGroup1.add(npc1Hitbox)
shuriken1SpritesGroup.add(shuriken1)
shuriken2SpritesGroup.add(shuriken2)
shuriken3SpritesGroup.add(shuriken3)

# create the sprites for scene 2
person2 = Player(130, 50, "CptImages/mazePlayer.png", 50, 50, BLACK)
person2.changespeedDown(0, 0, 90)
generator = Generator(610, 470, "CptImages/generator.png", 50, 80, GREY)
charger1 = Generator(610, 50, "CptImages/charger.png", 50, 50, GREY)
charger2 = Generator(135, 500, "CptImages/charger.png", 50, 50, GREY)
charger3 = Generator(70, 100, "CptImages/charger.png", 50, 50, GREY)
tornadoObject = Powerup(670, 100, "CptImages/tornado.gif", 50, 50, BLACK)
text1 = font.render("Connect the 3 chargers to the generators to revive your tank!",True,WHITE)

# 1 version of Horizontal Barrier
barrier1 = Barrier(125, 40, "CptImages/Black.png", 550, 2, BLACK)
barrier4 = Barrier(60, 100, "CptImages/Black.png", 75, 2, BLACK)
barrier7 = Barrier(400, 143, "CptImages/Black.png", 140, 2, BLACK)
barrier17 = Barrier(130, 142, "CptImages/Black.png", 100, 2, BLACK)
barrier18 = Barrier(600, 140, "CptImages/Black.png", 60, 2, BLACK)
barrier21 = Barrier(330, 340, "CptImages/Black.png", 335, 2, BLACK)
barrier22 = Barrier(130, 340, "CptImages/Black.png", 100, 2, BLACK)
barrier24 = Barrier(60, 245, "CptImages/Black.png", 75, 2, BLACK)
barrier25 = Barrier(660, 95, "CptImages/Black.png", 90, 2, BLACK)
barrier26 = Barrier(60, 440, "CptImages/Black.png", 75, 2, BLACK)
barrier27 = Barrier(200, 440, "CptImages/Black.png", 140, 2, BLACK)
barrier28 = Barrier(465, 440, "CptImages/Black.png", 135, 2, BLACK)
barrier29 = Barrier(660, 440, "CptImages/Black.png", 100, 2, BLACK)
barrier30 = Barrier(260, 245, "CptImages/Black.png", 140, 2, BLACK)
barrier31 = Barrier(660, 245, "CptImages/Black.png", 75, 2, BLACK)

# 2 version of Horizontal Barrier
barrier5 = Barrier(130, 95, "CptImages/Black.png", 138, 2, BLACK)
barrier6 = Barrier(400, 95, "CptImages/Black.png", 270, 2, BLACK)
barrier19 = Barrier(130, 300, "CptImages/Black.png", 100, 2, BLACK)
barrier20 = Barrier(330, 310, "CptImages/Black.png", 335, 2, BLACK)
barrier23 = Barrier(60, 200, "CptImages/Black.png", 75, 2, BLACK)
barrier32 = Barrier(250, 210, "CptImages/Black.png", 150, 2, BLACK)
barrier33 = Barrier(660, 200, "CptImages/Black.png", 75, 2, BLACK)
barrier34 = Barrier(60, 400, "CptImages/Black.png", 75, 2, BLACK)
barrier35 = Barrier(270, 400, "CptImages/Black.png", 75, 2, BLACK)
barrier36 = Barrier(470, 400, "CptImages/Black.png", 75, 2, BLACK)
barrier37 = Barrier(660, 400, "CptImages/Black.png", 75, 2, BLACK)
barrier38 = Barrier(60, 500, "CptImages/Black.png", 75, 2, BLACK)
barrier39 = Barrier(340, 500, "CptImages/Black.png", 120, 2, BLACK)
barrier40 = Barrier(660, 500, "CptImages/Black.png", 75, 2, BLACK)
barrier54 = Barrier(125, 550, "CptImages/Black.png", 550, 2, BLACK)

# 1 version of Vertical Barrier
barrier2 = Barrier(140, 40, "CptImages/Black.png", 2, 60, BLACK)
barrier10 = Barrier(660, 95, "CptImages/Black.png", 2, 40, BLACK)
barrier11 = Barrier(60, 90, "CptImages/Black.png", 2, 415, BLACK)
barrier12 = Barrier(130, 95, "CptImages/Black.png", 2, 40, BLACK)
barrier13 = Barrier(258, 95, "CptImages/Black.png", 2, 310, BLACK)
barrier41 = Barrier(130, 200, "CptImages/Black.png", 2, 40, BLACK)
barrier42 = Barrier(130, 400, "CptImages/Black.png", 2, 40, BLACK)
barrier43 = Barrier(400, 200, "CptImages/Black.png", 2, 40, BLACK)
barrier44 = Barrier(330, 400, "CptImages/Black.png", 2, 40, BLACK)
barrier45 = Barrier(460, 500, "CptImages/Black.png", 2, 40, BLACK)
barrier46 = Barrier(130, 500, "CptImages/Black.png", 2, 40, BLACK)
barrier53 = Barrier(660, 300, "CptImages/Black.png", 2, 40, BLACK)

# 2 version of Vertical Barrier
barrier3 = Barrier(665, 50, "CptImages/Black.png", 2, 90, BLACK)
barrier8 = Barrier(395, 95, "CptImages/Black.png", 2, 40, BLACK)
barrier9 = Barrier(730, 95, "CptImages/Black.png", 2, 410, BLACK)
barrier14 = Barrier(530, 95, "CptImages/Black.png", 2, 310, BLACK)
barrier15 = Barrier(200, 140, "CptImages/Black.png", 2, 310, BLACK)
barrier16 = Barrier(590, 140, "CptImages/Black.png", 2, 310, BLACK)
barrier47 = Barrier(130, 300, "CptImages/Black.png", 2, 40, BLACK)
barrier48 = Barrier(330, 300, "CptImages/Black.png", 2, 40, BLACK)
barrier49 = Barrier(470, 400, "CptImages/Black.png", 2, 45, BLACK)
barrier50 = Barrier(330, 500, "CptImages/Black.png", 2, 40, BLACK)
barrier51 = Barrier(660, 200, "CptImages/Black.png", 2, 40, BLACK)
barrier52 = Barrier(660, 400, "CptImages/Black.png", 2, 40, BLACK)
barrier55 = Barrier(660, 500, "CptImages/Black.png", 2, 50, BLACK)

# add all of the barriers to scene 2
allSpritesGroup2.add(barrier1)
allSpritesGroup2.add(barrier2)
allSpritesGroup2.add(barrier3)
allSpritesGroup2.add(barrier4)
allSpritesGroup2.add(barrier5)
allSpritesGroup2.add(barrier6)
allSpritesGroup2.add(barrier7)
allSpritesGroup2.add(barrier8)
allSpritesGroup2.add(barrier9)
allSpritesGroup2.add(barrier10)
allSpritesGroup2.add(barrier11)
allSpritesGroup2.add(barrier12)
allSpritesGroup2.add(barrier13)
allSpritesGroup2.add(barrier14)
allSpritesGroup2.add(barrier15)
allSpritesGroup2.add(barrier16)
allSpritesGroup2.add(barrier17)
allSpritesGroup2.add(barrier18)
allSpritesGroup2.add(barrier19)
allSpritesGroup2.add(barrier20)
allSpritesGroup2.add(barrier21)
allSpritesGroup2.add(barrier22)
allSpritesGroup2.add(barrier23)
allSpritesGroup2.add(barrier24)
allSpritesGroup2.add(barrier25)
allSpritesGroup2.add(barrier26)
allSpritesGroup2.add(barrier27)
allSpritesGroup2.add(barrier28)
allSpritesGroup2.add(barrier29)
allSpritesGroup2.add(barrier30)
allSpritesGroup2.add(barrier31)
allSpritesGroup2.add(barrier32)
allSpritesGroup2.add(barrier33)
allSpritesGroup2.add(barrier34)
allSpritesGroup2.add(barrier35)
allSpritesGroup2.add(barrier36)
allSpritesGroup2.add(barrier37)
allSpritesGroup2.add(barrier38)
allSpritesGroup2.add(barrier39)
allSpritesGroup2.add(barrier40)
allSpritesGroup2.add(barrier41)
allSpritesGroup2.add(barrier42)
allSpritesGroup2.add(barrier43)
allSpritesGroup2.add(barrier44)
allSpritesGroup2.add(barrier45)
allSpritesGroup2.add(barrier46)
allSpritesGroup2.add(barrier47)
allSpritesGroup2.add(barrier48)
allSpritesGroup2.add(barrier49)
allSpritesGroup2.add(barrier50)
allSpritesGroup2.add(barrier51)
allSpritesGroup2.add(barrier52)
allSpritesGroup2.add(barrier53)
allSpritesGroup2.add(barrier54)
allSpritesGroup2.add(barrier55)

# 1 version of Horizontal Barrier
barrierHorizontal1SpritesGroup.add(barrier1)
barrierHorizontal1SpritesGroup.add(barrier4)
barrierHorizontal1SpritesGroup.add(barrier7)
barrierHorizontal1SpritesGroup.add(barrier17)
barrierHorizontal1SpritesGroup.add(barrier18)
barrierHorizontal1SpritesGroup.add(barrier21)
barrierHorizontal1SpritesGroup.add(barrier22)
barrierHorizontal1SpritesGroup.add(barrier24)
barrierHorizontal1SpritesGroup.add(barrier25)
barrierHorizontal1SpritesGroup.add(barrier26)
barrierHorizontal1SpritesGroup.add(barrier27)
barrierHorizontal1SpritesGroup.add(barrier28)
barrierHorizontal1SpritesGroup.add(barrier29)
barrierHorizontal1SpritesGroup.add(barrier30)
barrierHorizontal1SpritesGroup.add(barrier31)

# 2 version of Horizontal Barrier
barrierHorizontal2SpritesGroup.add(barrier5)
barrierHorizontal2SpritesGroup.add(barrier6)
barrierHorizontal2SpritesGroup.add(barrier19)
barrierHorizontal2SpritesGroup.add(barrier20)
barrierHorizontal2SpritesGroup.add(barrier23)
barrierHorizontal2SpritesGroup.add(barrier32)
barrierHorizontal2SpritesGroup.add(barrier33)
barrierHorizontal2SpritesGroup.add(barrier34)
barrierHorizontal2SpritesGroup.add(barrier35)
barrierHorizontal2SpritesGroup.add(barrier36)
barrierHorizontal2SpritesGroup.add(barrier37)
barrierHorizontal2SpritesGroup.add(barrier38)
barrierHorizontal2SpritesGroup.add(barrier39)
barrierHorizontal2SpritesGroup.add(barrier40)
barrierHorizontal2SpritesGroup.add(barrier54)

# 1 version of Vertical Barrier
barrierVertical1SpritesGroup.add(barrier2)
barrierVertical1SpritesGroup.add(barrier10)
barrierVertical1SpritesGroup.add(barrier11)
barrierVertical1SpritesGroup.add(barrier13)
barrierVertical1SpritesGroup.add(barrier16)
barrierVertical1SpritesGroup.add(barrier41)
barrierVertical1SpritesGroup.add(barrier42)
barrierVertical1SpritesGroup.add(barrier43)
barrierVertical1SpritesGroup.add(barrier44)
barrierVertical1SpritesGroup.add(barrier45)
barrierVertical1SpritesGroup.add(barrier46)
barrierVertical1SpritesGroup.add(barrier53)

# 2 version of Vertical Barrier
barrierVertical2SpritesGroup.add(barrier3)
barrierVertical2SpritesGroup.add(barrier8)
barrierVertical2SpritesGroup.add(barrier9)
barrierVertical2SpritesGroup.add(barrier12)
barrierVertical2SpritesGroup.add(barrier14)
barrierVertical2SpritesGroup.add(barrier15)
barrierVertical2SpritesGroup.add(barrier47)
barrierVertical2SpritesGroup.add(barrier48)
barrierVertical2SpritesGroup.add(barrier49)
barrierVertical2SpritesGroup.add(barrier50)
barrierVertical2SpritesGroup.add(barrier51)
barrierVertical2SpritesGroup.add(barrier52)
barrierVertical2SpritesGroup.add(barrier55)

# add the sprites to scene 2
allSpritesGroup2.add(person2)
allSpritesGroup2.add(generator)
allSpritesGroup2.add(charger1)
allSpritesGroup2.add(charger2)
allSpritesGroup2.add(charger3)
chargerSpritesGroup.add(charger1)
chargerSpritesGroup.add(charger2)
chargerSpritesGroup.add(charger3)
charger1SpritesGroup.add(charger1)
charger2SpritesGroup.add(charger2)
charger3SpritesGroup.add(charger3)

## Main Program Loop
while not done:
    ## CONTROL
    # Check for events

    for event in pygame.event.get():
        # User key commands
        if event.type == pygame.QUIT:
            done = True

        # allow scene 0 tank to move in all directions
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                person.changespeedDown(-4, 0, 180)
                person2.changespeedDown(-4, 0, 0)
            elif event.key == pygame.K_d:
                person.changespeedDown(4, 0, 0)
                person2.changespeedDown(4, 0, 0)
            elif event.key == pygame.K_w:
                person.changespeedDown(0, -4, 90)
                person2.changespeedDown(0, -4, 0)
            elif event.key == pygame.K_s:
                person.changespeedDown(0, 4, 270)
                person2.changespeedDown(0, 4, 0)

        # allow scene 1 tank to move left and right      
            elif event.key == pygame.K_RIGHT:
                person1.changespeedUp(5, 0)
                playerHitbox.changespeedUp(5, 0)
            elif event.key == pygame.K_LEFT:
                person1.changespeedUp(-5, 0)
                playerHitbox.changespeedUp(-5, 0)
                 
        # allow scene 0 tank to move in all directions
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                person.changespeedUp(4, 0)
                person2.changespeedDown(4, 0, 0)
            elif event.key == pygame.K_d:
                person.changespeedUp(-4, 0)
                person2.changespeedDown(-4, 0, 0)
            elif event.key == pygame.K_w:
                person.changespeedUp(0, 4)
                person2.changespeedDown(0, 4, 0)
            elif event.key == pygame.K_s:
                person.changespeedUp(0, -4)
                person2.changespeedDown(0, -4, 0)

          # allow scene 1 tank to move left and right      
            elif event.key == pygame.K_RIGHT:
                person1.changespeedUp(-5, 0)
                playerHitbox.changespeedUp(-5, 0)
            elif event.key == pygame.K_LEFT:
                person1.changespeedUp(5, 0)
                playerHitbox.changespeedUp(5, 0)

          # make shoot variable 1 when user hits space on scene 1
            elif event.key == pygame.K_SPACE:
              if(scene == 1):
                 shoot = 1
                 cannonballSound.play()

            # make fire variable 1 when user hits f on scene 1
            elif event.key == pygame.K_f:
              if (scene == 1):
                fire = 1

          # make tornado variable 1 when use hits t when ability variable is 1
            elif event.key == pygame.K_t and ability == 1:
              tornado = 1
              tornadoSound.play()
               
    # create lists for collisions
    hitList = pygame.sprite.spritecollide(person, npcSpritesGroup, False)
    hitList1 = pygame.sprite.spritecollide(cannonball, npcSpritesGroup1, False)
    hitList2 = pygame.sprite.spritecollide(playerHitbox, shuriken1SpritesGroup, False)
    hitList3 = pygame.sprite.spritecollide(person2, chargerSpritesGroup, False)
    hitList4 = pygame.sprite.spritecollide(generator, charger1SpritesGroup, False)
    hitList5 = pygame.sprite.spritecollide(generator, charger2SpritesGroup, False)
    hitList6 = pygame.sprite.spritecollide(generator, charger3SpritesGroup, False)
    hitList7 = pygame.sprite.spritecollide(person2, powerupSpritesGroup, False)
    hitList8 = pygame.sprite.spritecollide(tornadoMoveHitbox, npcSpritesGroup1, False)
    hitList9 = pygame.sprite.spritecollide(playerHitbox, shuriken2SpritesGroup, False)
    hitList10 = pygame.sprite.spritecollide(playerHitbox, shuriken3SpritesGroup, False)
    hitList11 = pygame.sprite.spritecollide(playerHitbox, hellfireSpritesGroup, False)
    hitList12 = pygame.sprite.spritecollide(fireball, npcSpritesGroup1, False)
    hitList13 = pygame.sprite.spritecollide(person2, barrierHorizontal1SpritesGroup, False)
    hitList14 = pygame.sprite.spritecollide(person2, barrierHorizontal2SpritesGroup, False)
    hitList15 = pygame.sprite.spritecollide(person2, barrierVertical1SpritesGroup, False)
    hitList16 = pygame.sprite.spritecollide(person2, barrierVertical2SpritesGroup, False)
 
    # if user powered the generator and resets the game
    if(reset == 1):
      person2.rect.x = 300
      person2.rect.y = 100
      stopper = "go"
      stopper1 = "go"
      stopper2 = "go"
      stopper3 = "go"
      stopper4 = "go"
      stopper5 = "go"
      stopper6 = "go"
      stopper7 = "go"
      stopper8 = "go"
      stopper9 = "go"
      stopper10 = "go"
      stopper11 = "go"
      stopper12 = "go"
      dontHit = 0
      fail = 0
      power1 = 0
      power2 = 0
      power3 = 0
      bossShoot1 = 1
      bossShoot2 = 1
      bossShoot3 = 1
      shoot = 0
      x1 = 230
      y1 = 570
      tornado = 0
      bossShoot1 == 1
      bossShoot2 == 1
      bossShoot3 == 1
      scene = 1
      reset = 0
      resetter = 1
      end = 0
      fire = 0
      reAdjust = 1
      hellShoot = 0
      shuriken1.rect.x = npc1.rect.x
      shuriken1.rect.y = npc1.rect.y+100
      shuriken2.rect.x = npc1.rect.x+25
      shuriken2.rect.y = npc1.rect.y+100
      shuriken3.rect.x = npc1.rect.x+50
      shuriken3.rect.y = npc1.rect.y+100
      hellfire.rect.x = portal.rect.x
      hellfire.rect.y = -50
     
    ## SCENE 0
    if (scene == 0):

      # check if the tank hits the npc to start the minigame
      for npc in hitList:
        scene = 1

      # set background for scene 0
      background = pygame.image.load("CptImages/gameStart.jpg").convert()
      background = pygame.transform.scale(background, (800, 600))
      screen.blit(background, [0, 0])

      # set instructions texts for player to understand the game
      text10 = font.render("Tank Stars", True, YELLOW)
      screen.blit(text10, [380, 20])
      text3 = font.render("Instructions:",True,RED)
      screen.blit(text3, [0, 50])
      text4 = font.render("Use left and right arrow to control your fighter tank. Use spacebar to shoot a cannonball at the enemy.",True,WHITE)
      screen.blit(text4, [0, 100])
      text10 = font.render("You can also use the 'f' key to shoot a fireball!",True,WHITE)
      screen.blit(text10, [0, 125])
      text5 = font.render("If you die, dont worry. You can revive by using your character to power on the generator. Use WASD to control",True,WHITE)
      screen.blit(text5, [0, 175])
      text6 = font.render("this character. Watch out, as soon as you power on the generators you are back into the action!",True,WHITE)
      screen.blit(text6, [0, 200])
      text7 = font.render("If you manage to find the secret tornado powerup, use the key 't' to use the tornado during battle.",True,WHITE)
      screen.blit(text7, [0, 250])
      text8 = font.render("When you are ready, use the tank and go up to the NPC (with WASD), you will be telported to the battlefield",True,WHITE)
      screen.blit(text8, [0, 300])
      text9 = font.render("Good Luck and Have Fun!",True,WHITE)
      screen.blit(text9, [0, 325])

      # update allSpritesGroup
      allSpritesGroup.update()
     
      # draw allSpritesGroup to the screen
      allSpritesGroup.draw(screen)
     
    ## SCENE 1
    if (scene == 1):

    # call scene1 function
      scene1(text)
     
    # dont let player go out of bounds
      if person1.rect.x > 650:
        person1.rect.x = 650
        playerHitbox.rect.x = 640
      elif person1.rect.x < 0:
        person1.rect.x = 0
        playerHitbox.rect.x = 10
       
    # check if shurikens hit
      for shuriken1 in hitList2:
        if(resetter == 0):
          scene = 2
          end = 1
          allSpritesGroup2.add(generator)
          allSpritesGroup2.add(charger1)
          allSpritesGroup2.add(charger2)
          allSpritesGroup2.add(charger3)
          chargerSpritesGroup.add(charger1)
          chargerSpritesGroup.add(charger2)
          chargerSpritesGroup.add(charger3)
          charger1SpritesGroup.add(charger1)
          charger2SpritesGroup.add(charger2)
          charger3SpritesGroup.add(charger3)
          allSpritesGroup.remove(shuriken1)
          reAdd = 1
         
      for shuriken2 in hitList9:
        if(resetter == 0):
          scene = 2
          end = 1
          allSpritesGroup2.add(generator)
          allSpritesGroup2.add(charger1)
          allSpritesGroup2.add(charger2)
          allSpritesGroup2.add(charger3)
          chargerSpritesGroup.add(charger1)
          chargerSpritesGroup.add(charger2)
          chargerSpritesGroup.add(charger3)
          charger1SpritesGroup.add(charger1)
          charger2SpritesGroup.add(charger2)
          charger3SpritesGroup.add(charger3)
          allSpritesGroup.remove(shuriken2)
          reAdd = 1
         
      for shuriken3 in hitList10:
        if(resetter == 0):
          scene = 2
          end = 1
          allSpritesGroup2.add(generator)
          allSpritesGroup2.add(charger1)
          allSpritesGroup2.add(charger2)
          allSpritesGroup2.add(charger3)
          chargerSpritesGroup.add(charger1)
          chargerSpritesGroup.add(charger2)
          chargerSpritesGroup.add(charger3)
          charger1SpritesGroup.add(charger1)
          charger2SpritesGroup.add(charger2)
          charger3SpritesGroup.add(charger3)
          allSpritesGroup.remove(shuriken3)
          reAdd = 1
         
      resetter = 0
     
      # if shurikens have not hit yet
      if (end != 1):

        # add shurikens to sprite list
        allSpritesGroup1.add(shuriken1)
        allSpritesGroup1.add(shuriken2)
        allSpritesGroup1.add(shuriken3)
       
        if (bossShoot1 == 0 and bossShoot2 == 0 and bossShoot3 == 0):
         
        # make sure shurikens do not go out of bounds
          if (shuriken1.rect.x > 800 or shuriken1.rect.x < 0):
              shuriken1.rect.x = npc1.rect.x
              shuriken1.rect.y = npc1.rect.y+100
              bossShoot1 = 1
              hellShoot = 1
              stopper11 = "go"
          if (shuriken1.rect.y > 700 or shuriken1.rect.y < -100):
              shuriken1.rect.x = npc1.rect.x
              shuriken1.rect.y = npc1.rect.y+100
              bossShoot1 = 1
              hellShoot = 1
              stopper11 = "go"
          if (shuriken2.rect.x > 800 or shuriken2.rect.x < 0):
              shuriken2.rect.x = npc1.rect.x+25
              shuriken2.rect.y = npc1.rect.y+100
              bossShoot2 = 1
          if (shuriken2.rect.y > 600 or shuriken2.rect.y < 0):
              shuriken2.rect.x = npc1.rect.x+25
              shuriken2.rect.y = npc1.rect.y+100
              bossShoot2 = 1
          if (shuriken3.rect.x > 800 or shuriken3.rect.x < 0):
              shuriken3.rect.x = npc1.rect.x+50
              shuriken3.rect.y = npc1.rect.y+100
              bossShoot3 = 1
          if (shuriken3.rect.y > 600 or shuriken3.rect.y < 0):
              shuriken3.rect.x = npc1.rect.x+50
              shuriken3.rect.y = npc1.rect.y+100
              bossShoot3 = 1

        # make shurikens move
        if (bossShoot1 == 1):
          shuriken1.changespeed(random.randrange(-4,4),random.randrange(1,5),90)
          bossShoot1 = 0
        if (bossShoot2 == 1):
          shuriken2.changespeed(-random.randrange(-4,4),random.randrange(1,5),90)
          bossShoot2 = 0
        if (bossShoot3 == 1):
          shuriken3.changespeed(-random.randrange(-4,4),random.randrange(1,5),90)
          bossShoot3 = 0

        # make npc1 move back and forth
        if(stopper3 != "stop"):
          npc1.changespeed(4, 0)
          npc1Hitbox.changespeed(4, 0)

        # make sure npc1 does not go out of bounds
        if npc1.rect.x > 700:
          npc1.changespeed(-4, 0)
          npc1Hitbox.changespeed(-4, 0)
          stopper3 = "stop"
        elif npc1.rect.x < -50:
          npc1.changespeed(4, 0)
          npc1Hitbox.changespeed(4, 0)

        # if the user has not shot the fireball yet
        if (fire == 0):
          fireball.rect.x = person1.rect.x + 155
          fireball.rect.y = person1.rect.y + 7

        # if the user has shot the fireball
        if (fire == 1):
          allSpritesGroup1.add(fireball)
          fireball.changespeed(10, -4, 0)

          if (fireball.rect.x > 800 or fireball.rect.y < 0):
            fire = 0
            fireball.changespeed(0, 0, 0)
            fireball.rect.x = person1.rect.x + 155
            fireball.rect.y = person1.rect.y + 7

        # if fireball hits the enemy
        for npc1Hitbox in hitList12:
          if (fire == 1 and healthbar.x5 >= 30 and healthbar.x4 >= 20 and healthbar.x6 >= 30):
            healthbar.x6 = healthbar.x6 - 7
            healthbar.x5 = healthbar.x5 - 7
            healthbar.x4 = healthbar.x4 - 7
            health = health - 7
            fireball.changespeed(0, 0, 0)
            fireball.rect.x = person1.rect.x + 155
            fireball.rect.y = person1.rect.y + 7
            fire = 0

        # if the user has not shot yet
        if (shoot == 0):
          cannonball.rect.x = person1.rect.x + 155
          cannonball.rect.y = person1.rect.y + 7

        # if the user shot the cannonball
        if (shoot == 1):
          allSpritesGroup1.add(cannonball)
          cannonball.changespeed(10, -4, 90)

          # if cannonball goes out of bounds
          if (cannonball.rect.x > 800 or cannonball.rect.y < 0):
            shoot = 0
            cannonball.changespeed(0, 0, 0)
            cannonball.rect.x = person1.rect.x + 155
            cannonball.rect.y = person1.rect.y + 7

        # if cannonball hits the enemy
        for npc1Hitbox in hitList1:
          if (shoot == 1 and healthbar.x5 >= 30 and healthbar.x4 >= 20 and healthbar.x6 >= 30):
            healthbar.x6 = healthbar.x6 - 5
            healthbar.x5 = healthbar.x5 - 5
            healthbar.x4 = healthbar.x4 - 5
            health = health - 5
            cannonball.changespeed(0, 0, 0)
            cannonball.rect.x = person1.rect.x + 155
            cannonball.rect.y = person1.rect.y + 7
            shoot = 0

        # use tornado move
        if (tornado == 1):
          if (stopper8 == "go"):
            tornadoMove.rect.x = person1.rect.x + 150
            tornadoMoveHitbox.rect.x = person1.rect.x + 212
          allSpritesGroup1.add(tornadoMove)
          allSpritesGroup1.add(tornadoMoveHitbox)
          tornadoMove.changespeed(6, 0, 0)
          tornadoMoveHitbox.changespeed(6, 0, 0)
          dontHit = 0
          stopper8 = "stop"

        # check if tornado hits npc  
        for npc1Hitbox in hitList8:
          if (dontHit != 1):
            healthbar.x6 = healthbar.x6 - 15
            healthbar.x5 = healthbar.x5 - 15
            healthbar.x4 = healthbar.x4 - 15
            health = health - 15
            allSpritesGroup1.remove(tornadoMove)
            allSpritesGroup1.remove(tornadoMoveHitbox)
            tornadoMove.changespeed(0, 0, 0)
            tornadoMoveHitbox.changespeed(0, 0, 0)
            tornadoMove.rect.x = person1.rect.x + 150
            tornadoMoveHitbox.rect.x = person1.rect.x + 212
            tornado = 0
            dontHit = 1
            stopper8 = "go"
            npc1.changespeed(4, 0)
            npc1Hitbox.changespeed(4, 0)

        # check if tornado goes out of bounds
        if (tornadoMove.rect.x > 800):
          allSpritesGroup1.remove(tornadoMove)
          allSpritesGroup1.remove(tornadoMoveHitbox)
          tornadoMove.changespeed(0, 0, 0)
          tornadoMoveHitbox.changespeed(0, 0, 0)
          tornadoMove.rect.x = person1.rect.x + 150
          tornadoMoveHitbox.rect.x = person1.rect.x + 212
          tornado = 0
          dontHit = 1
          stopper8 = "go"

        # add portals and hellfire randomly to the map
        if (hellShoot == 1):
          if (stopper11 != "stop"):
            portal.rect.x = random.randrange(0,800)
            hellfire.rect.x = portal.rect.x
            hellfire.rect.y = -50
            stopper11 = "stop"
          hellfire.rect.y = hellfire.rect.y + 5
          allSpritesGroup1.add(portal)
          allSpritesGroup1.add(hellfire)
          hellfireSpritesGroup.add(hellfire)

          # check if hellfire goes out of bounds
          if (hellfire.rect.y == 600):
            allSpritesGroup1.remove(portal)
            allSpritesGroup1.remove(hellfire)
            hellShoot = 0

          # check for hellfire collisions
          for hellfire in hitList11:
            scene = 2
            end = 1
            allSpritesGroup2.add(generator)
            allSpritesGroup2.add(charger1)
            allSpritesGroup2.add(charger2)
            allSpritesGroup2.add(charger3)
            chargerSpritesGroup.add(charger1)
            chargerSpritesGroup.add(charger2)
            chargerSpritesGroup.add(charger3)
            charger1SpritesGroup.add(charger1)
            charger2SpritesGroup.add(charger2)
            charger3SpritesGroup.add(charger3)
            allSpritesGroup1.remove(hellfire)
            hellfireSpritesGroup.remove(hellfire)
            reAdd = 1
         
        # update the allSpritesGroup1
        allSpritesGroup1.update()

        # draw the healthbar
        healthbar.drawing(screen)

        # draw allSpritesGroup1 to the screen
        allSpritesGroup1.draw(screen)
       
    ## SCENE 2
    if (scene == 2):
      if (stopper9 == "go"):
        charger1.rect.x = 610
        charger1.rect.y = 50
        charger2.rect.x = 135
        charger2.rect.y = 500
        charger3.rect.x = 70
        charger3.rect.y = 100
        person2.rect.x = 300
        person2.rect.y = 100
        stopper9 = "stop"
       
      # call scene 2 subprogram
      scene2(text1, x1, y1)
      x1 = 230
      y1 = 570
     
      # rotate image properly to start
      person2.changespeedDown(0, 0, 90)
     
      # when user picks up powerup
      if (ability != 1):
        allSpritesGroup2.add(tornadoObject)
        powerupSpritesGroup.add(tornadoObject)
        for tornadoObject in hitList7:
          allSpritesGroup2.remove(tornadoObject)
          text1 = font.render("You have unlocked a new move for your tank!!",True,WHITE)
          x1 = 230
          ability = 1

      # make sure person2 cannot got out of bounds
      for barrier1 in hitList13:
        person2.rect.y = person2.rect.y + 4

      for barrier1 in hitList14:
        person2.rect.y = person2.rect.y - 4

      for barrier1 in hitList15:
        person2.rect.x = person2.rect.x + 4

      for barrier1 in hitList16:
        person2.rect.x = person2.rect.x - 4
       
      # when user picks up power units
      if(stopper10 == "go"):
        for charger1 in hitList3:
          charger1.rect.x = person2.rect.x + 30
          charger1.rect.y = person2.rect.y + 30
        for charger2 in hitList3:
          charger2.rect.x = person2.rect.x + 30
          charger2.rect.y = person2.rect.y + 30
        for charger3 in hitList3:
          charger3.rect.x = person2.rect.x + 30
          charger3.rect.y = person2.rect.y + 30
        stopper10 = "go"

      # when user adds to generator
      if (reAdd == 0):
        for charger1 in hitList4:
          allSpritesGroup2.remove(charger1)
          if (stopper5 != "stop"):
            power1 = 1
            stopper5 = "stop"
         
        for charger2 in hitList5:
          allSpritesGroup2.remove(charger2)
          if (stopper6 != "stop"):
            power2 = 1
            stopper6 = "stop"
         
        for charger3 in hitList6:
          allSpritesGroup2.remove(charger3)
          if (stopper7 != "stop"):
            power3 = 1
            stopper7 = "stop"
 
      reAdd = 0
      reAdjust = 0
     
      # update allSpritesGroup2
      allSpritesGroup2.update()

      # draw allSpritesGroup2 to the screen
      allSpritesGroup2.draw(screen)

    # if all the generators are turned on
    if (power1 == 1 and power2 == 1 and power3 == 1):
      reset = 1
      if (stopper12 != "stop"):
        lifeCounter = lifeCounter + 1
        stopper12 = "stop"

    # if the boss is killed
    if (health <= 0):
      if (stopper13 != "stop"):
        lifeCounter = lifeCounter + 1
        stopper13 = "stop"
      lifeCounter = str(lifeCounter)
      background2 = pygame.image.load("CptImages/gameOver.webp").convert()
      background2 = pygame.transform.scale(background2, (800, 600))

      # If user did not die once
      if (lifeCounter == "1"):
        background2 = pygame.image.load("CptImages/winner.jpeg").convert()
        background2 = pygame.transform.scale(background2, (800, 600))
      screen.blit(background2, [0, 0])
      text2 = font.render("It took you "+lifeCounter+" try! Can you do any better!?!?!?",True,RED)
      x2 = 235
      y2 = 400

      # If user did not die once
      if (lifeCounter == "1"):
        text2 = font.render("It took you "+lifeCounter+" try! Congrats! That is the best possible score!",True,WHITE)
        x2 = 215
        y2 = 400

      # If user only died once
      else:
        text2 = font.render("It took you "+lifeCounter+" tries! Can you do any better!?!?!?",True,RED)
        x2 = 235
        y2 = 400
      screen.blit(text2, [x2, y2])
     
    ## VIEW
    pygame.display.flip()
    clock.tick(60)

# Close the window and quit
pygame.quit()