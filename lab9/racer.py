import pygame, sys
from pygame.locals import *
import random, time

#Initialzing 
pygame.init()

#FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SPEED = 5
SCORE = 0
coinss = 0    #счетчик
COIN_THRESHOLD = 5 #количество монет для увеличения скорости
#Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

#Background image
background = pygame.image.load(r"/Users/erkenazsagynbaeva/Downloads/PygameTutorial_3_0/AnimatedStreet.png")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r"/Users/erkenazsagynbaeva/Downloads/PygameTutorial_3_0/Enemy.png")
        self.image = pygame.transform.scale(self.image, (90, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  

      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("/Users/erkenazsagynbaeva/Downloads/PygameTutorial_3_0/Player.png")
        self.image = pygame.transform.scale(self.image, (90, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.value = random.choice([1, 2, 3, 5])   #вес монеты (1, 2, 3)
        self.image = pygame.image.load(r"/Users/erkenazsagynbaeva/Downloads/PygameTutorial_3_0/Coin.png")  
        # Scale coin size based on weight 
        size = 30 + self.value * 3
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)
        
    def move(self):
        self.rect.move_ip(0, SPEED)
        # Respawn when coin leaves screen
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

#Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1 = Coin()

#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

while True: 
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5   
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 
    DISPLAYSURF.blit(background, (0,0))
    # Show score and coin count
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))

    text = font_small.render("Coins: " + str(coinss), True, BLACK)
    DISPLAYSURF.blit(text, (300,10))
 
    # Move and redraw all sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    a = pygame.sprite.spritecollide(P1, coins, True)
    if a:
        # Add weighted coin values
        for c in a:
            coinss += c.value

        # Spawn a new coin after collecting one
        new = Coin()
        coins.add(new)
        all_sprites.add(new)

        # Increase enemy speed every N coins
        if coinss % COIN_THRESHOLD == 0:
            SPEED += 1
 
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound(r'/Users/erkenazsagynbaeva/Downloads/PygameTutorial_3_0/crash.wav').play()
          time.sleep(0.5)
                    
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
           
          pygame.display.update()

          for entity in all_sprites:
                entity.kill() 

          time.sleep(2)
          pygame.quit()
          sys.exit()        
         
    pygame.display.update()
    FramePerSec.tick(FPS)
