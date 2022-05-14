from turtle import back
import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Huntin' The Pearl")
font = pygame.font.Font('font/Pixeltype.ttf', 50)
clock = pygame.time.Clock()

sea = pygame.image.load('graphics/water.png').convert()

sky = pygame.transform.scale(pygame.image.load('graphics/background.jpg'). convert(), (900, 700))

text = font.render('Score:', False, (64, 64, 100))

kraken = pygame.transform.scale(pygame.image.load('graphics/kraken/kraken.png'), (85,80)).convert_alpha()
kraken_rect = kraken.get_rect(topleft = (600, 320))

black_pearl = pygame.transform.scale(pygame.image.load('graphics/ship/black_pearl.png').convert_alpha(), (200, 175))
pearl_rect = black_pearl.get_rect(topleft = (0, 240))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(sky, (0, 0))

    screen.blit(black_pearl, pearl_rect)

    screen.blit(sea, (0, 400))

    kraken_rect.x -= 4
    screen.blit(kraken, (kraken_rect.x, 355))
    if kraken_rect.x < -60 : kraken_rect.x = 800

    screen.blit(text, (20, 20))

    pygame.display.update()
    clock.tick(60)