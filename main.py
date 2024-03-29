import time
import threading
import pygame
import random


pygame.init()

screen_width = 1500
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))

font2 = pygame.font.SysFont('Algerian', 70)
font = pygame.font.SysFont("Algerian", 110)

imgL = pygame.image.load('pct/levushka1.png')
img = pygame.image.load('pct/levushka.png')
img2 = pygame.image.load('pct/Без названия.jpg')
img3 = pygame.image.load('pct/4.jpg')
img4 = pygame.image.load('pct/html.png')
img5 = pygame.image.load('pct/images.jpg')
kirp = pygame.image.load('pct/loft-krasnyy.jpg')
bullet = pygame.image.load('pct/png-clipart-bullets-bullets.png')

kirp = pygame.transform.scale(kirp, (200, 200))

kirp2 = kirp
kirp3 = kirp

fon_mus = pygame.mixer.Sound('sounds/9a49e1c170bd8c1.mp3')

img = pygame.transform.scale(img, (100, 100))
imgL = pygame.transform.scale(imgL, (100, 100))
img3 = pygame.transform.scale(img3, (10000, 10000))
img4 = pygame.transform.scale(img4, (150, 150))
img5 = pygame.transform.scale(img5, (300, 300))
bullet = pygame.transform.scale(bullet, (50, 50))

side = 1
score = 0

x_k = 100
y_k = 100

x_e = 500
y_e = 500

x = 0
y = 0

x_b = x
y_b = y

lev_speed = 1.5
en_speed = 0.5

bul_timer = 0
count = 0


def spawn():
    global count
    global y
    global x
    global y_e
    global x_e
    global screen_height
    global screen_width
    count += 1
    time.sleep(1)
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)
    x_e = random.randint(0, screen_width)
    y_e = random.randint(0, screen_height)
    if x_e == x and y_e == y:
        spawn()


def player():
    global side
    global lev_speed
    global x
    global y
    global side
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        y -= lev_speed

    if keys[pygame.K_d]:
        side = 0
        x += lev_speed

    if keys[pygame.K_a]:
        side = 1
        x -= lev_speed

    if keys[pygame.K_s]:
        y += lev_speed
    if side == 1:
        screen.blit(img, (x, y))
    if side == 0:
        screen.blit(imgL, (x, y))


flag = False


def player2():
    global side
    global flag
    global x_b
    global y_b
    global bul_timer
    global x_e
    global y_e
    global en_speed
    mouse_en_pr = pygame.mouse.get_pressed()  # Нужно доделать
    mouse_en_pos = pygame.mouse.get_pos()
    keys_en = pygame.key.get_pressed()
    if keys_en[pygame.K_UP]:
        y_e -= en_speed

    if keys_en[pygame.K_RIGHT]:
        x_e += en_speed

    if keys_en[pygame.K_LEFT]:
        x_e -= en_speed

    if keys_en[pygame.K_DOWN]:
        y_e += en_speed

    if keys_en[pygame.K_SPACE]:
        bul()
        flag = True
    else:
        flag = False

    if flag == True:
        if side == 1:
            if x_b < x:
                x_b -= 1
                screen.blit(bullet, (x_b, y_b))
        if side == 0:
            if x_b > x:
                x_b += 1
                screen.blit(bullet, (x_b, y_b))
    else:
        y_b = y
        x_b = x

    screen.blit(img4, (x_e, y_e))


def bul():
    global x_b
    global y_b
    global y_e
    global x_e
    if x_b-150 < x_e < x_b+50 and y_b-150 < y_e < y_b+50:
        spawn()


def touch():
    if x-140 < x_e < x+90 and y-120 < y_e < y+70:
        screen.blit(img5, (x-100, y-100))
        spawn()


def touch_kirp():
    if x-100 < x_k < x+100 and y-150 < y_k < y+150:
        screen.blit(img5, (x, y))


def barrier():
    global x
    global y
    global lev_speed
    if x > screen_width-100:
        x -= lev_speed
    if x < 0:
        x += lev_speed
    if y > screen_height-100:
        y -= lev_speed
    if y < 0:
        y += lev_speed


threadPL = threading.Thread(target=player())
threadPL2 = threading.Thread(target=player2())
threadBUL = threading.Thread(target=bul())

threadBUL.start()
threadPL.start()
threadPL2.start()
pygame.mixer.Sound.play(fon_mus)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.blit(img3, (0, 0))

    text = font.render("Hello", True, (10,200,100))
    screen.blit(text, (600,220))

    text2 = font2.render('Settings', True, (200, 0, 0))
    screen.blit(text2, (100, 60))

    text3 = font2.render('Start Play!', True, (10, 220, 80))
    screen.blit(text3, (600, 350))
    # countTEXT = font2.render(count, True, (0, 220, 0))
    # screen.blit(countTEXT, (700, 0))
    player()
    player2()
    touch()
    barrier()
    pygame.display.update()
