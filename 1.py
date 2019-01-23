
import pygame

pygame.init()

# MUSIC
# pygame.mixer.music.load('Main_theme.wav')
# pygame.mixer.music.play(-1)

display_width = 1275
display_height = 750

black = (0, 0, 0)

win = pygame.display.set_mode((display_width, display_height))
# full screen: ((1275, 750))

pygame.display.set_caption("Vanishing of Hao Melnik")

introImg = pygame.image.load('pygame-badge-SMA.png')

# INTRO SCREEN


def intro(x, y):
    win.blit(introImg, (x, y))


x = (display_width * 0.18)
y = (display_height * 0.15)

win.fill(black)
intro(x, y)

died = False

while not died:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            died = True

    if event.type == pygame.K_SPACE:
        intro()

    pygame.display.update()
pygame.quit()
quit()


# ScreenWidth = 500
#
# x = 50
# y = 425
# width = 50
# height = 50
# vel = 5
#
# isJump = True
# jumpCount = 10
# run = True
#
# while run:
#     pygame.time.delay(1)
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#
#     keys = pygame.key.get_pressed()
#
#     if keys[pygame.K_LEFT] and x > vel:
#         x -= vel
#     if keys[pygame.K_RIGHT] and x < ScreenWidth - width - vel:
#         x += vel
#     if not isJump:
#         if keys[pygame.K_UP] and y > vel:
#             y -= vel
#         if keys[pygame.K_DOWN] and y < ScreenWidth - height - vel:
#             y += vel
#         if keys[pygame.K_SPACE]:
#             isJump = True
#     else:
#         if jumpCount >= -10:
#             neg = 1
#             if jumpCount < 0:
#                 y -= (jumpCount ** 2) / 2 * neg
#             jumpCount -= 1
#         else:
#             isJump = False
#             jumpCount = 20
#
#     win.fill((0, 0, 0))
#     pygame.draw.rect(win, (45, 50, 45), (x, y, width, height))
#     pygame.display.update()
#
# pygame.quit()
