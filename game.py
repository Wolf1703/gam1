import pygame

pygame.init()

screen_hight = 800
screen_widht = 1200

screen = pygame.display.set_mode((screen_widht, screen_hight))

font = pygame.font.SysFont("Algerian", 60)

# spo = {'Аня', "Ваня"}

text = font.render("Boronnikov Timofei Evgenevich", True, (10,200,100))
# text2 = font.render(spo, True, (0, 100, 200))

img_k = pygame.image.load('images/kot.jpg')
img_c = pygame.image.load("images/cobaka.jpg")

img_c = pygame.transform.scale(img_c, (300, 300))

us_inp = input()


def cob():
    if us_inp == 'Собака':
        screen.blit(img_c, (20, 20))


def kot():
     if us_inp == 'Кот':
        screen.blit(img_k, (20, 20))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.blit(text, (0, 0))

    cob()
    kot()
    pygame.display.update()
