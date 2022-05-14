# Importing Libraries
from itertools import count
from turtle import back
import pygame
import sys

pygame.init()

# Creating display and font
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Huntin' The Pearl")
font = pygame.font.Font('font/Pixeltype.ttf', 50)
clock = pygame.time.Clock()

# Function to count score
def count_score():
    current_time = pygame.time.get_ticks() // 1000
    score = font.render(f'Score: {current_time}', False, (64, 64, 100))
    score_rect = score.get_rect(center = (400, 50))
    screen.blit(score, score_rect)

# Loading images
sea = pygame.image.load('graphics/water.png').convert()

sky = pygame.transform.scale(pygame.image.load('graphics/background.jpg'). convert(), (900, 700))

kraken = pygame.transform.scale(pygame.image.load('graphics/kraken/kraken.png'), (85,80)).convert_alpha()
kraken_rect = kraken.get_rect(topleft = (600, 320))

black_pearl = pygame.transform.scale(pygame.image.load('graphics/ship/black_pearl.png').convert_alpha(), (200, 175))
pearl_rect = black_pearl.get_rect(topleft = (0, 240))

# The Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Getting the images on the screen
    screen.blit(sky, (0, 0))

    screen.blit(black_pearl, pearl_rect)

    screen.blit(sea, (0, 400))

    kraken_rect.x -= 4
    screen.blit(kraken, (kraken_rect.x, 355))
    if kraken_rect.x < -60 : kraken_rect.x = 800

    count_score()

    pygame.display.update()
    clock.tick(60)