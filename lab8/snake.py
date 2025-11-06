import pygame
import time
import random
pygame.init()
FramePerSec = pygame.time.Clock()     # Объект таймера для управления FPS
#Цвета в формате RGB
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
#Размеры экрана и игровые переменные
SCREEN_WIDTH = 800                   # Ширина окна
SCREEN_HEIGHT = 600                  # Высота окна
# Инициализирование игрового окно
game_window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Змейка')
# определение положения змеи по умолчанию
snake_position = [100, 50]
snake_speed = 15

# определение первых 4 блоков тела змеи
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]

# fruit position
fruit_position = [random.randrange(1, (SCREEN_WIDTH // 10)) * 10,
                  random.randrange(1, (SCREEN_HEIGHT // 10)) * 10]

fruit_spawn = True

# установка направления змеи по умолчанию к
# право
direction = 'RIGHT'
change_to = direction

# начальная оценка
score = 0

fruit_time = 5

# отображение функции Score
def show_score(choice, color, font, size) :
    # создание объекта шрифта score_font
    score_font = pygame.font.SysFont(font, size)

    # создать объект поверхности отображения
    # score_surface
    score_surface = score_font.render('Score : ' + str(score), True, color)

    # создаем прямоугольный объект для текста
    # поверхностный объект
    score_rect = score_surface.get_rect()

    # отображение текста
    game_window.blit(score_surface, score_rect)


# функция завершения игры
def game_over() :
    # создание объекта шрифта my_font
    my_font = pygame.font.SysFont('times new roman', 50)

    # создание текстовой поверхности, на которой текст
    # будет нарисовано
    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, RED)

    # создать прямоугольный объект для текста
    # surface object
    game_over_rect = game_over_surface.get_rect()

    # установка положения текста
    game_over_rect.midtop = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)

    # blit нарисует текст на экране
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    # через 2 секунды мы выйдем из программы
    time.sleep(2)

    # деактивация библиотеки pygame
    pygame.quit()

    # quit the program
    quit()

# Main Function
while True :

    # обработка ключевых событий
    for event in pygame.event.get() :
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_UP :
                change_to = 'UP'
            if event.key == pygame.K_DOWN :
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT :
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT :
                change_to = 'RIGHT'

    # Если две клавиши нажаты одновременно
    # мы не хотим, чтобы змея разделялась на две
    # направлений одновременно
    if change_to == 'UP' and direction != 'DOWN' :
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP' :
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT' :
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT' :
        direction = 'RIGHT'

    # Перемещение змеи
    if direction == 'UP' :
        snake_position[1] -= 10
    if direction == 'DOWN' :
        snake_position[1] += 10
    if direction == 'LEFT' :
        snake_position[0] -= 10
    if direction == 'RIGHT' :
        snake_position[0] += 10

    # Механизм роста тела змеи
    # если фрукты и змеи сталкиваются, то очки
    # будет увеличено на 10
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1] :
        score += 10
        fruit_spawn = False
    else :
        snake_body.pop()

    if not fruit_spawn :
        fruit_position = [random.randrange(1, (SCREEN_WIDTH // 10)) * 10,
                          random.randrange(1, (SCREEN_HEIGHT // 10)) * 10]

    fruit_spawn = True
    game_window.fill(BLACK)

    for pos in snake_body :
        pygame.draw.rect(game_window, GREEN,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, WHITE, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))

    # Game Over conditions
    if snake_position[0] < 0 or snake_position[0] > SCREEN_WIDTH - 10 :
        game_over()
    if snake_position[1] < 0 or snake_position[1] > SCREEN_HEIGHT - 10 :
        game_over()

    # Touching the snake body
    for block in snake_body[1 :] :
        if snake_position[0] == block[0] and snake_position[1] == block[1] :
            game_over()

    # displaying score countinuously
    show_score(1, WHITE, 'times new roman', 20)

    # Refresh game screen
    pygame.display.update()

    # Frame Per Second /Refresh Rate
    FramePerSec.tick(snake_speed)