import pygame
import math
def draw_square(surface, center, size, color):
    half = size // 2
    rect = pygame.Rect(center[0] - half, center[1] - half, size, size)
    pygame.draw.rect(surface, color, rect, 2)

def draw_right_triangle(surface, center, size, color):
    x, y = center
    points = [(x, y), (x + size, y), (x, y - size)]
    pygame.draw.polygon(surface, color, points, 2)

def draw_equilateral_triangle(surface, center, size, color):
    x, y = center
    h = size * (math.sqrt(3)/2)
    points = [(x, y - h/2), (x - size/2, y + h/2), (x + size/2, y + h/2)]
    pygame.draw.polygon(surface, color, points, 2)

def draw_rhombus(surface, center, size, color):
    x, y = center
    points = [(x, y - size), (x + size, y), (x, y + size), (x - size, y)]
    pygame.draw.polygon(surface, color, points, 2)

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    mode = 'blue'           # начальный цвет кисти
    points = []             # точки кисти
    shapes = []             # список фигур: (type, position, color)
    shape_mode = None       # текущий режим фигуры
    
    # сопоставление клавиш с цветами
    color_map = {'r': (255, 0, 0), 'g': (0, 255, 0), 'b': (0, 0, 255)}
    
    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                
                # выбор цвета
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                
                # выбор фигуры через клавиатуру
                if event.key == pygame.K_1:
                    shape_mode = "square"
                elif event.key == pygame.K_2:
                    shape_mode = "right_triangle"
                elif event.key == pygame.K_3:
                    shape_mode = "equilateral_triangle"
                elif event.key == pygame.K_4:
                    shape_mode = "rhombus"
                elif event.key == pygame.K_d:
                    shape_mode = None   
            
            # клик мыши
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # левый клик
                    if shape_mode is None:
                        radius = min(200, radius + 1)  # увеличение кисти
                    else:
                        pos = event.pos
                        # добавляем фигуру в список
                        if mode == 'red':
                            color = (255,0,0)
                        elif mode == 'green':
                            color = (0,255,0)
                        elif mode == 'blue':
                            color = (0,0,255)
                        shapes.append((shape_mode, pos, color))
                elif event.button == 3:  # правый клик уменьшает кисть
                    if shape_mode is None:
                        radius = max(1, radius - 1)
                    else:
                        if shapes:
                            shapes.pop()  # удалить последнюю фигуру
        
            # движение мыши для кисти
            if event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0]:
                if shape_mode is None:
                    position = event.pos
                    points = points + [position]
                    points = points[-256:]
        
     
        screen.fill((0,0,0))
        
        # рисуем фигуры
        for shape, pos, color in shapes:
            if shape == "square":
                draw_square(screen, pos, radius*4, color)
            elif shape == "right_triangle":
                draw_right_triangle(screen, pos, radius*4, color)
            elif shape == "equilateral_triangle":
                draw_equilateral_triangle(screen, pos, radius*4, color)
            elif shape == "rhombus":
                draw_rhombus(screen, pos, radius*4, color)
        
        # рисуем кисть
        if shape_mode is None:
            i = 0
            while i < len(points) - 1:
                drawLineBetween(screen, i, points[i], points[i+1], radius, mode)
                i += 1
        
        pygame.display.flip()
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

main()
