import pygame
from random import uniform as func
from time import sleep

# ініціалізація pygame
pygame.init()

# Розміри вікна гри
WIDTH, HEIGHT = 400, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("My Game")

clock = pygame.time.Clock()

# Колірні налаштування
bound = 5
c2s = 30
white = (255, 255, 255)
black = (0, 0, 0)

# Налаштування м'яча
x, y = WIDTH // 2, HEIGHT // 2
radius = 10

# Налаштування швидкості
velocity = 8
vx = velocity * func(-1, 1)
vy = velocity * func(-1, 1)

# Налаштування границь
border_u = bound + radius
border_d = HEIGHT - (bound + radius)
border_l = bound + radius
border_r = WIDTH - (bound + radius)

# Налаштування майданчика
height = 10
width = 80
xp = (WIDTH - width) // 2
yp = HEIGHT - height
vp = 10

# Змінна для підрахунку очок
score = 0

# Функція для відображення екрану
def drawWindow():
    win.fill(black)
    pygame.draw.rect(win, white, (0, 0, WIDTH, bound))  # up
    pygame.draw.rect(win, white, (0, 0, bound, HEIGHT))  # left
    pygame.draw.rect(win, white, (WIDTH - bound, 0, bound, HEIGHT))  # right
    pygame.draw.rect(win, white, (0, HEIGHT - bound, WIDTH, bound))  # down
    pygame.draw.rect(win, white, (xp, yp, width, height))  # paddle
    pygame.draw.circle(win, (0, 255, 0), (x, y), radius)  # ball
    pygame.display.update()

# Функція для виведення результату гри
def drawScore():
    win.fill(black)
    pygame.font.init()
    path = pygame.font.match_font("arial")
    Font = pygame.font.Font(path, 30)
    text = f'Your score: {score}'
    a = Font.render(text, 1, (255, 255, 255))
    win.blit(a, (WIDTH // 2 - 70, HEIGHT // 3))
    pygame.display.update()

# Головний цикл гри
run = True
while run:
    clock.tick(c2s)
    
    # Обробка подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Оновлення позиції м'яча
    x += vx
    y += vy

    # Перевірка відбиття від меж вікна
    if x + vx < border_l or x + vx > border_r:
        vx = -vx
    if y + vy < border_u:
        vy = -vy

    # Перевірка відбиття від майданчика
    if yp <= y + vy <= yp + height:
        if xp <= x + vx <= xp + width:
            vy = -vy
            score += 1  # Збільшуємо очки при відбитті м'яча
        else:
            drawScore()  # Виведення результату
            sleep(10)  # Затримка на 10 секунд
            run = False  # Закінчення гри

    # Переміщення майданчика
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and xp > bound:
        xp -= vp
    if keys[pygame.K_RIGHT] and xp < WIDTH - width - bound:
        xp += vp

    # Малюємо екран
    drawWindow()

pygame.quit()
