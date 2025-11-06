import pygame
import random

pygame.init()

w, h = 600, 400
c = 20
win = pygame.display.set_mode((w, h))

black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
white = (255, 255, 255)

s = [(100, 100), (80, 100), (60, 100)]
d = "RIGHT"
f = (random.randrange(0, w, c), random.randrange(0, h, c))
sc = 0
lvl = 1
sp = 8

font = pygame.font.SysFont("Arial", 20)
clock = pygame.time.Clock()

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP and d != "DOWN": d = "UP"
            elif e.key == pygame.K_DOWN and d != "UP": d = "DOWN"
            elif e.key == pygame.K_LEFT and d != "RIGHT": d = "LEFT"
            elif e.key == pygame.K_RIGHT and d != "LEFT": d = "RIGHT"

    x, y = s[0]
    if d == "UP": y -= c
    elif d == "DOWN": y += c
    elif d == "LEFT": x -= c
    elif d == "RIGHT": x += c

    new = (x, y)
    if x < 0 or x >= w or y < 0 or y >= h or new in s: pygame.quit()

    s.insert(0, new)

    if new == f:
        sc += 1
        if sc % 3 == 0: lvl += 1; sp += 2
        while True:
            f = (random.randrange(0, w, c), random.randrange(0, h, c))
            if f not in s: break
    else:
        s.pop()

    win.fill(black)
    for p in s: pygame.draw.rect(win, green, (p[0], p[1], c, c))
    pygame.draw.rect(win, red, (f[0], f[1], c, c))

    txt = "Score: " + str(sc) + "  Level: " + str(lvl)
    win.blit(font.render(txt, True, white), (10, 10))

    pygame.display.flip()
    clock.tick(sp)