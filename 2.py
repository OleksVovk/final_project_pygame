from random import randint

import pygame
pygame.init()

# MUSIC
# pygame.mixer.music.load('sounds/Main_theme.wav')
# pygame.mixer.music.play(-1)

display_width = 900     # 1275
display_height = 790    # 750

win = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption("Vanishing of Hao Melnik")

time = pygame.time.Clock()

walkRight = [pygame.image.load('sprites/R1.png'),
             pygame.image.load('sprites/R2.png'),
             pygame.image.load('sprites/R3.png'),
             pygame.image.load('sprites/R4.png'),
             pygame.image.load('sprites/R5.png'),
             pygame.image.load('sprites/R6.png')]

walkLeft = [pygame.image.load('sprites/L1.png'),
            pygame.image.load('sprites/L2.png'),
            pygame.image.load('sprites/L3.png'),
            pygame.image.load('sprites/L4.png'),
            pygame.image.load('sprites/L5.png'),
            pygame.image.load('sprites/L6.png')]

bg = pygame.image.load('sprites/Background.png')

char = [pygame.image.load('sprites/standing1.png'),
        pygame.image.load('sprites/standing2.png'),
        pygame.image.load('sprites/standing3.png'),
        pygame.image.load('sprites/standing4.png')]


x = 700
y = 680
width = 50
height = 50
velocity = 10
Jump = False
count = 10
left = False
right = False
still = False
walk = 0
stand = 1


def win_update():
    global walk
    global stand
    win.blit(bg, (0, 0))

    if walk + 1 >= 25:
        walk = 0

    if left:
        win.blit(walkLeft[walk//6], (x, y))
        walk += 1
    elif right:
        win.blit(walkRight[walk//6], (x, y))
        walk += 1
    else:
        print(stand)
        win.blit(char[stand // 2], (x, y))
        if stand == 6:
            stand = 0
        else:
            stand += 1

    pygame.display.update()


run = True
while run:
    time.tick(25)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(event)
            run = False

    keys = pygame.key.get_pressed()

# MOVEMENT
    if keys[pygame.K_LEFT] and x > velocity:
        x -= velocity
        left = True
        right = False

    elif keys[pygame.K_RIGHT] and x < 900 - width - velocity:
        x += velocity
        right = True
        left = False

    else:
        right = False
        left = False
        walk = 0

# JUMPING
    if not Jump:
        if keys[pygame.K_SPACE]:
            Jump = True
            right = False
            left = False
            walk = 0
    else:
        if count >= -10:
            des = 1
            if count < 0:
                des = -1
            y -= (count ** 2) * 0.2 * des
            count -= 1
        else:
            Jump = False
            count = 10

    win_update()

pygame.quit()
