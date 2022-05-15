# Importing Libraries
from random import randint
import pygame
import sys


pygame.init()

# Creating display, font and variables
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("HeART of the Sea")
font = pygame.font.Font('font/Pixeltype.ttf', 60)
clock = pygame.time.Clock()
game_active = False
start_time = 0
score = 0

# Function to count score
def count_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time 
    score = font.render(f'Score: {current_time}', False, (64, 64, 100))
    score_rect = score.get_rect(center = (400, 50))
    screen.blit(score, score_rect)
    return current_time

# Collision function
def collisions(obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if pearl_rect.colliderect(obstacle_rect): return False
    return True

# Obstacle movement function
def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 9

            if obstacle_rect.top == 355: screen.blit(kraken, obstacle_rect)
            else: screen.blit(fly, obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        return obstacle_list
    
    else: return []

# Loading images
sea = pygame.image.load('graphics/water.png').convert()
sea_rect = sea.get_rect(topleft = (0,400))
sky = pygame.transform.scale(pygame.image.load('graphics/background.jpg'). convert(), (900, 700))

# Obstacles
kraken = pygame.transform.scale(pygame.image.load('graphics/kraken/kraken.png'), (85,80)).convert_alpha()
fly = pygame.image.load('graphics/fly/fly1.png').convert_alpha()
obstacle_rect_list = []

# Ship
black_pearl = pygame.transform.scale(pygame.image.load('graphics/ship/black_pearl.png').convert_alpha(), (190, 175))
pearl_rect = black_pearl.get_rect(topleft = (0, 240))
ship_gravity = -23

# Treasure
treasure = pygame.image.load('graphics/treasure.png')
treasure = pygame.transform.rotozoom(treasure, 0, 1)
treasure_rect = treasure.get_rect(center = (400, 400))

# Winning text
win_text = font.render("You've found thy hidden treasure!!", False, (111, 196, 189))
win_text_rect = win_text.get_rect(center = (400, 100))

# Play again text
play_again_text = font.render('Press SPACE to play again.', False, (111, 196, 189))
play_again_text_rect = play_again_text.get_rect(center = (400, 175))

# Adding music
bg_music = pygame.mixer.Sound('music/bg_music.mp3')
bg_music.set_volume(0.25)
bg_music.play()

# Intro screen
player = pygame.image.load('graphics/player/player.png')
player = pygame.transform.rotozoom(player, 0, 1.5)
player_rect = player.get_rect(center = (400, 280))

game_name = font.render("HeART Of The Sea", False, (111, 196, 169))
game_name = pygame.transform.scale2x(game_name)
game_name_rect = game_name.get_rect(center = (400, 75))

game_message = font.render("Press SPACE to start.", False, (111, 196, 169))
game_message_rect = game_message.get_rect(center = (400, 550))

# Enemy Spawning
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1650)

# The Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and pearl_rect.bottom >= 420:
                    ship_gravity = -23
            if event.type == obstacle_timer:
                if randint(0,2): obstacle_rect_list.append(kraken.get_rect(topleft = (randint(900, 1200), 355)))
                else: obstacle_rect_list.append(fly.get_rect(topleft = (randint(900, 1200), 175)))
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)

    if score == 15:
        game_active = False

    if game_active:
        # Getting the images on the screen
        screen.blit(sky, (0, 0))
        screen.blit(black_pearl, pearl_rect)
        screen.blit(sea, sea_rect)

        # Jumping of the ship
        ship_gravity += 1
        pearl_rect.y += ship_gravity
        if pearl_rect.bottom > 420: pearl_rect.bottom = 420 

        # check for collision 
        game_active = collisions(obstacle_rect_list)

        obstacle_rect_list = obstacle_movement(obstacle_rect_list)
        score = count_score()

    else:
        if score < 15:
            screen.fill((94, 129, 162))
            screen.blit(player, player_rect)
            screen.blit(game_name, game_name_rect)
            obstacle_rect_list.clear()

            score_message = font.render(f"Your score : {score}", False, (111, 196, 169))
            score_message_rect = score_message.get_rect(center = (400, 525))
            
            if score == 0: screen.blit(game_message, game_message_rect)
            else: screen.blit(score_message, score_message_rect)
        else:
            screen.fill((94, 129, 162))
            screen.blit(treasure, treasure_rect)
            screen.blit(win_text, win_text_rect) 
            screen.blit(play_again_text, play_again_text_rect)           


    pygame.display.update()
    clock.tick(60)


