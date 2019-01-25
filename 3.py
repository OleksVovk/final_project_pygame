import webbrowser

import pygame
pygame.init()

# MUSIC
pygame.mixer.music.load('sounds/Main_theme.wav')
pygame.mixer.music.play(-1)
arrowSound = pygame.mixer.Sound('sounds/usp2.wav')


display_width = 900     # 1275 - full screen
display_height = 770    # 750 - full screen

win = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption("Liwko's  adventure")

time = pygame.time.Clock()

score = 0

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


# MAIM CHARACTER


class Character(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 6
        self.Jump = False
        self.count = 10
        self.left = False
        self.right = False
        self.walk = 0
        self.stand = True
        self.hitbox = (self.x + 26, self.y, 28, 30)

    def display(self, win):
        if self.walk + 1 >= 25:
            self.walk = 0

        if not self.stand:
            if self.left:
                win.blit(walkLeft[self.walk // 5], (self.x, self.y))
                self.walk += 1

            elif self.right:
                win.blit(walkRight[self.walk // 5], (self.x, self.y))
                self.walk += 1

        else:
            print(self.stand)
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))

        self.hitbox = (self.x + 26, self.y, 28, 80)
        # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

# SHOOTING


class Bullet(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.velocity = 8 * facing

    def display(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

# ENEMY


class Villain(object):
    animationRight = [pygame.image.load('sprites/E1.png'),
                      pygame.image.load('sprites/E2.png'),
                      pygame.image.load('sprites/E3.png'),
                      pygame.image.load('sprites/E4.png'),
                      pygame.image.load('sprites/E5.png'),
                      pygame.image.load('sprites/E6.png'),
                      pygame.image.load('sprites/E7.png'),
                      pygame.image.load('sprites/E8.png'),
                      pygame.image.load('sprites/E9.png'),
                      pygame.image.load('sprites/E10.png')]

    animationLeft = [pygame.image.load('sprites/A1.png'),
                     pygame.image.load('sprites/A2.png'),
                     pygame.image.load('sprites/A3.png'),
                     pygame.image.load('sprites/A4.png'),
                     pygame.image.load('sprites/A5.png'),
                     pygame.image.load('sprites/A6.png'),
                     pygame.image.load('sprites/A7.png'),
                     pygame.image.load('sprites/A8.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.count = 0
        self.velocity = 5
        self.path = [self.x, self.end]
        self.hitbox = (self.x + 20, self.y - 50, 50, 80)
        self.healthbar = 13
        self.visible = True

    def display(self, win):
        self.move()
        if self.visible:
            if self.count + 1 >= 20:
                self.count = 0

            if self.velocity > 0:
                win.blit(self.animationRight[self.count // 4], (self.x, self.y))
                self.count += 1
            else:
                win.blit(self.animationLeft[self.count // 4], (self.x, self.y))
                self.count += 1

            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] + 40, 50, 10))
            pygame.draw.rect(win, (0, 240, 0), (self.hitbox[0], self.hitbox[1] + 40, 50 - (5 * (10 - self.healthbar)), 10))
            self.hitbox = (self.x + 45, self.y - 50, 50, 50)
            # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def move(self):
        if self.velocity > 0:
            if self.x + self.velocity < self.path[1]:
                self.x += self.velocity
            else:
                self.velocity = self.velocity * -1
                self.count = 0
        else:
            if self.x - self.velocity > self.path[0]:
                self.x += self.velocity
            else:
                self.velocity = self.velocity * -1
                self.count = 0

    def hit(self):
        if self.healthbar > 0:
            self.healthbar -= 1
        else:
            self.visible = False
        print('HIT')


def win_update():
    win.blit(bg, (0, 0))
    text = letters.render("You've reached: " + str(score), 1, (255, 255, 255))
    win.blit(text, (590, 10))
    knight.display(win)
    enemy.display(win)
    for i in arrows:
        i.display(win)

    pygame.display.update()


knight = Character(450, 650, 50, 50)
enemy = Villain(10, 680, 50, 50, 800)
letters = pygame.font.SysFont('helvetice', 40, True)
arrows = []
shootRegister = 0
run = True
while run:
    time.tick(25)

    if shootRegister > 0:
        shootRegister += 1
    if shootRegister > 2:
        shootRegister = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(event)
            run = False

    for arrow in arrows:
        if arrow.y - arrow.radius < enemy.hitbox[1] + enemy.hitbox[3] and arrow.y + arrow.radius > enemy.hitbox[1]:
            if arrow.x + arrow.radius > enemy.hitbox[0] and arrow.x - arrow.radius < enemy.hitbox[1] + enemy.hitbox[2]:
                enemy.hit()
                score += 1
                if score == 100:
                    pygame.mixer.music.stop()
                    webbrowser.open("https://youtu.be/-FQIqIiABoU?t=36")
                arrows.pop(arrows.index(arrow))

        if arrow.x < 900 and arrow.x > 0:
            arrow.x += arrow.velocity
        else:
            arrows.pop(arrows.index(arrow))

    keys = pygame.key.get_pressed()

# MOVEMENT

    if keys[pygame.K_SPACE] and shootRegister == 0:
        arrowSound.play()
        if knight.left:
            facing = -1
        else:
            facing = 1

        if len(arrows) < 3:
            arrows.append(Bullet(round(knight.x + knight.width // 2),
                                 round(knight.y + knight.height // 2), 6, (220, 20, 60), facing))

        shootRegister = 1

    if keys[pygame.K_LEFT] and knight.x > knight.velocity:
        knight.x -= knight.velocity
        knight.left = True
        knight.right = False
        knight.stand = False
    elif keys[pygame.K_RIGHT] and knight.x < 900 - knight.width - knight.velocity:
        knight.x += knight.velocity
        knight.right = True
        knight.left = False
        knight.stand = False
    else:
        knight.stand = True
        knight.walk = 0

# JUMPING
    if not knight.Jump:
        if keys[pygame.K_UP]:
            knight.Jump = True
            knight.right = False
            knight.left = False
            knight.walk = 0
    else:
        if knight.count >= -10:
            down = 1
            if knight.count < 0:
                down = -1
            knight.y -= (knight.count ** 2) * 0.3 * down
            knight.count -= 1
        else:
            knight.Jump = False
            knight.count = 10

    win_update()

pygame.quit()
