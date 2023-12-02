import pygame

pygame.init()

screen_width = 1500
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))

font2 = pygame.font.SysFont('Algerian', 70)
font = pygame.font.SysFont("Algerian", 110)

img = pygame.image.load('pct/levushka.jpg')
img2 = pygame.image.load('pct/Без названия.jpg')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    text = font.render("Hello", True, (10,200,100))
    screen.blit(text, (600,220))

    text2 = font2.render('Settings', True, (200, 0, 0))
    screen.blit(text2, (100, 60))

    text3 = font2.render('Start Play!', True, (10, 220, 80))
    screen.blit(text3, (600, 350))

    screen.blit(img, (100, 200))
    screen.blit(img2, (1200, 100))
    pygame.display.update()