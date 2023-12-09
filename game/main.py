import pygame
import random



pygame.init()

screen_width = 1500
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))

font2 = pygame.font.SysFont('Algerian', 70)
font = pygame.font.SysFont("Algerian", 110)

img = pygame.image.load('pct/levushka.jpg')
img2 = pygame.image.load('pct/Без названия.jpg')
img3 = pygame.image.load('pct/4.jpg')

img = pygame.transform.scale(img, (150, 150))
img3 = pygame.transform.scale(img3, (10000, 10000))

x_e = 500
y_e = 500

x = 0
y = 0

lev_speed = 1
en_speed = 1


def player():
    global lev_speed
    global x
    global y
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        print('Верх')
        y -= lev_speed

    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        print('Вправо')
        x += lev_speed

    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        print('Влево')
        x -= lev_speed

    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        print('Вниз')
        y += lev_speed

    screen.blit(img, (x, y))

def enemy():
    global en_speed
    global x_e
    global y_e

    while x_e != x:
        x_e + 1
    screen.blit(img2, (x_e, y_e))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.blit(img3, (0, 0))
    enemy()
    player()
    text = font.render("Hello", True, (10,200,100))
    screen.blit(text, (600,220))

    text2 = font2.render('Settings', True, (200, 0, 0))
    screen.blit(text2, (100, 60))

    text3 = font2.render('Start Play!', True, (10, 220, 80))
    screen.blit(text3, (600, 350))

    pygame.display.update()
