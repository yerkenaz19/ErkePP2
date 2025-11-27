import pygame
import random
import sys
import psycopg2
import ast
pygame.init()
con = psycopg2.connect(
    dbname='snake_game',
    user='erkenaz',
    password='12345',
    host='localhost',
    port='5432'
)
cur = con.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS user_account(
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE,
    level INT DEFAULT 1
);
""")
cur.execute("""
CREATE TABLE IF NOT EXISTS user_score(
    user_id INT REFERENCES user_account(id),
    score INT,
    level INT,
    speed INT,
    snake TEXT,
    food_x INT,
    food_y INT
);
""")
con.commit()
def get_user(username):
    cur.execute("SELECT * FROM user_account WHERE username=%s", (username,))
    return cur.fetchone()
def create_user(username):
    cur.execute("INSERT INTO user_account(username) VALUES (%s) RETURNING *", (username,))
    con.commit()
    return cur.fetchone()
def save_game(user_id, score, level, speed, snake, food):
    cur.execute("DELETE FROM user_score WHERE user_id=%s", (user_id,))
    cur.execute(
        "INSERT INTO user_score(user_id, score, level, speed, snake, food_x, food_y) "
        "VALUES (%s,%s,%s,%s,%s,%s,%s)",
        (user_id, score, level, speed, str(snake), food[0], food[1])
    )
    con.commit()
def load_game(user_id):
    cur.execute("SELECT * FROM user_score WHERE user_id=%s", (user_id,))
    return cur.fetchone()
username = input("Enter your username: ")
user = get_user(username)
if user:
    print(f"Welcome back, {username}! Your current level: {user[2]}")
else:
    user = create_user(username)
    print(f"New user created! Level set to 1.")

user_id = user[0]
saved = load_game(user_id)
resume = False
if saved:
    ans = input("Resume last saved game? (y/n): ")
    if ans.lower() == "y":
        resume = True
w, h = 600, 400
c = 20
win = pygame.display.set_mode((w, h))
pygame.display.set_caption("Snake Game")

black = (0,0,0)
green = (0,255,0)
red = (255,0,0)
white = (255,255,255)
blue = (0,150,255)
yellow = (255,255,0)

food_weights = {
    1: (red, 1),
    2: (blue, 2),
    3: (yellow, 3)
}
def create_food():
    pos = (random.randrange(0, w, c), random.randrange(0, h, c))
    f_type = random.choice([1,2,3])
    return pos, f_type
if resume:
    sc = saved[1]
    lvl = saved[2]
    sp = saved[3]
    s = ast.literal_eval(saved[4])
    f = (saved[5], saved[6])
    f_type = 1
else:
    s = [(100,100),(80,100),(60,100)]
    sc = 0
    lvl = user[2]
    sp = 6 + lvl * 2
    f, f_type = create_food()

d = "RIGHT"

font = pygame.font.SysFont("Arial", 20)
clock = pygame.time.Clock()

paused = False
while True:

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP and d != "DOWN": d = "UP"
            elif e.key == pygame.K_DOWN and d != "UP": d = "DOWN"
            elif e.key == pygame.K_LEFT and d != "RIGHT": d = "LEFT"
            elif e.key == pygame.K_RIGHT and d != "LEFT": d = "RIGHT"
            if e.key == pygame.K_p:
                paused = True
                save_game(user_id, sc, lvl, sp, s, f)
                print("Game saved! Press R to resume.")
            if e.key == pygame.K_r:
                paused = False

    if paused:
        continue

    x, y = s[0]

    if d == "UP": y -= c
    elif d == "DOWN": y += c
    elif d == "LEFT": x -= c
    elif d == "RIGHT": x += c

    new = (x, y)

    if x < 0 or x >= w or y < 0 or y >= h or new in s:
        print("Game Over!")
        pygame.quit()
        sys.exit()

    s.insert(0, new)

    if new == f:
        color, value = food_weights[f_type]
        sc += value

        if sc % 5 == 0:
            lvl += 1
            sp += 1

        f, f_type = create_food()

    else:
        s.pop()
    win.fill(black)

    for p in s:
        pygame.draw.rect(win, green, (p[0], p[1], c, c))

    food_color, _ = food_weights[f_type]
    pygame.draw.rect(win, food_color, (f[0], f[1], c, c))

    txt = f"User: {username}  Score: {sc}  Level: {lvl}"
    win.blit(font.render(txt, True, white), (10,10))

    pygame.display.flip()
    clock.tick(sp)
