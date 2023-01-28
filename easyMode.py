"""
Use sprites to collect blocks.
 
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
  
"""
import pygame
import random

 
# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)


class Player(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """
    
    
    # -- Methods
    def __init__(self, x, y):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        self.image = pygame.Surface([15, 15])
        self.image.fill(BLUE)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
 
        # -- Attributes
        # Set speed vector
        self.change_x = 0
        self.change_y = 0
 
    def changespeed(self, x, y):
        """ Change the speed of the player"""
        self.change_x += x
        self.change_y += y
 
    def update(self):

        bump_sound = pygame.mixer.Sound("bump.wav")
      
        """ Find a new position for the player"""
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        if self.rect.x > 680:
            self.rect.x = 680
            bump_sound.play()
        if self.rect.x < 0:
            self.rect.x = 0
            bump_sound.play()
        if self.rect.y < 0:
            self.rect.y = 0
            bump_sound.play()
        if self.rect.y > 380:
            self.rect.y = 380
            bump_sound.play()
 
      
class Block(pygame.sprite.Sprite):
    """
    This class represents the ball.
    It derives from the "Sprite" class in Pygame.
    """
 
    def __init__(self, color, width, height,filename):
        """ Constructor. Pass in the color of the block,
        and its size. """
 
        # Call the parent class (Sprite) constructor
        super().__init__()
  

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.image.load(filename).convert()
 
        # Set background color to be transparent. Adjust to WHITE if your
        # background is WHITE.
        self.image.set_colorkey(BLACK)
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()

# Initialize Pygame
pygame.init()
 
# Set the height and width of the screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
font = pygame.font.SysFont('Calibri', 25, True, False)
  
# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
block_list = pygame.sprite.Group()
good_block_list = pygame.sprite.Group()
bad_block_list = pygame.sprite.Group()

# This is a list of every sprite. 
# All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
 
for i in range(10):
    # This represents a block
    block = Block(GREEN, 20, 15,"goodStar.PNG")
 
    # Set a random location for the block
    block.rect.x = random.randrange(screen_width-50)
    block.rect.y = random.randrange(screen_height-50)
 
    # Add the block to the list of objects 
    good_block_list.add(block)
    all_sprites_list.add(block) 

    # This represents a block
    block = Block(RED, 20, 15,"badStar.PNG")
    # Set a random location for the block
    block.rect.x = random.randrange(screen_width-50)
    block.rect.y = random.randrange(screen_height-50)
 
    # Add the block to the list of objects 
    bad_block_list.add(block) 
    all_sprites_list.add(block)  
 
# Create a RED player block
player = Player(20, 15)
all_sprites_list.add(player)
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
score = 0

#sound:

good_sound = pygame.mixer.Sound("good_block.wav")

bad_sound = pygame.mixer.Sound("bad_block.wav")


# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
        # Set the speed based on the key pressed
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, -3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, 3)
 
        # Reset speed when key goes up
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, 3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, -3)
 
    # Clear the screen
    screen.fill(WHITE)
  
    
    # See if the player block has collided with anything.
    blocks_hit_list = pygame.sprite.spritecollide(player, good_block_list, True)

    blocks_hit_list2 = pygame.sprite.spritecollide(player, bad_block_list, True)

    # Check the list of collisions.
    for block in blocks_hit_list:
        score += 1 
        good_sound.play()

    for block in blocks_hit_list2:
        score = score - 1 
        bad_sound.play()

    text = font.render("Score:" + str(score), True,BLACK)
    text1 = font.render("WINNER WINNER!", True,WHITE)
    if (score == 10):
      text1 = font.render("WINNER WINNER!", True,BLACK)

    # Put the image of the text on the screen at 250x250
    screen.blit(text, [10, 10])

    
    screen.blit(text1, [250,180])
  
    # This calls update on all the sprites
    all_sprites_list.update()
  
    # Draw all the spites
    all_sprites_list.draw(screen)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 60 frames per second
    clock.tick(60)
 
pygame.quit()
