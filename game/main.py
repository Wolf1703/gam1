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
img4 = pygame.image.load('pct/html.png')
img5 = pygame.image.load('pct/images.jpg')

fon_mus = pygame.mixer.Sound('sounds/zvuk_-_shagov.mp3')

img = pygame.transform.scale(img, (150, 150))
img3 = pygame.transform.scale(img3, (10000, 10000))
img4 = pygame.transform.scale(img4, (150, 150))
img5 = pygame.transform.scale(img5, (200, 200))

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
    if keys[pygame.K_w]:
        y -= lev_speed

    if keys[pygame.K_d]:
        x += lev_speed

    if keys[pygame.K_a]:
        x -= lev_speed

    if keys[pygame.K_s]:
        y += lev_speed

    screen.blit(img, (x, y))
# def enemy():
#     global en_speed
#     global x_e
#     global y_e
#
#     while x_e != x:
#         x_e + 1
#     screen.blit(img2, (x_e, y_e))

def player2():
    global x_e
    global y_e
    global en_speed
    keys_en = pygame.key.get_pressed()
    if keys_en[pygame.key]:
        pygame.mixer.Sound.play(fon_mus)
    if keys_en[pygame.K_UP]:
        y_e -= en_speed

    if keys_en[pygame.K_RIGHT]:
        x_e += en_speed

    if keys_en[pygame.K_LEFT]:
        x_e -= en_speed

    if keys_en[pygame.K_DOWN]:
        y_e += en_speed
    screen.blit(img4, (x_e, y_e))


def touch():
    if x-150 < x_e < x+150 and y-150 < y_e < y+150:
        screen.blit(img5, (x, y))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.blit(img3, (0, 0))
    player()
    player2()
    touch()
    text = font.render("Hello", True, (10,200,100))
    screen.blit(text, (600,220))

    text2 = font2.render('Settings', True, (200, 0, 0))
    screen.blit(text2, (100, 60))

    text3 = font2.render('Start Play!', True, (10, 220, 80))
    screen.blit(text3, (600, 350))

    pygame.display.update()
