import pygame
import random
import sys
pygame.init()

w, h = 600, 400
c = 20
win = pygame.display.set_mode((w, h))
pygame.display.set_caption("Snake Game")

# Colors
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
white = (255, 255, 255)
blue = (0, 150, 255)
yellow = (255, 255, 0)

# Snake body
s = [(100, 100), (80, 100), (60, 100)]
d = "RIGHT"

food_weights = {
    1: (red, 1),      
    2: (blue, 2),     
    3: (yellow, 3)    
}

def create_food():
    pos = (random.randrange(0, w, c), random.randrange(0, h, c))
    f_type = random.choice([1, 2, 3])
    return pos, f_type

f, f_type = create_food()


food_timer_max = 120  
food_timer = food_timer_max

sc = 0
lvl = 1
sp = 8

font = pygame.font.SysFont("Arial", 20)
clock = pygame.time.Clock()

while True:
    # Event checker
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP and d != "DOWN": d = "UP"
            elif e.key == pygame.K_DOWN and d != "UP": d = "DOWN"
            elif e.key == pygame.K_LEFT and d != "RIGHT": d = "LEFT"
            elif e.key == pygame.K_RIGHT and d != "LEFT": d = "RIGHT"

    x, y = s[0]

    # Move snake
    if d == "UP": y -= c
    elif d == "DOWN": y += c
    elif d == "LEFT": x -= c
    elif d == "RIGHT": x += c

    new = (x, y)

    # Game over conditions
    if x < 0 or x >= w or y < 0 or y >= h or new in s:
        pygame.quit()

    s.insert(0, new)

    if new == f:
        color, value = food_weights[f_type]   
        sc += value                         

    
        if sc % 3 == 0: 
            lvl += 1
            sp += 2

        # Generate NEW food
        while True:
            f, f_type = create_food()
            if f not in s:
                break

        food_timer = food_timer_max  

    else:
        s.pop()

   
    food_timer -= 1

    if food_timer <= 0:
        f, f_type = create_food()
        food_timer = food_timer_max

    # Drawing screen
    win.fill(black)

    # Draw snake
    for p in s:
        pygame.draw.rect(win, green, (p[0], p[1], c, c))

    food_color, _ = food_weights[f_type]
    pygame.draw.rect(win, food_color, (f[0], f[1], c, c))

    txt = "Score: " + str(sc) + "  Level: " + str(lvl)
    win.blit(font.render(txt, True, white), (10, 10))

    pygame.display.flip()
    clock.tick(sp)
