import pygame
from tkinter import *
from tkinter import messagebox
import random
Tk().wm_withdraw()
pygame.display.set_caption("Типа арканоид")
pygame.mixer.init()
pygame.mixer.music.load("rickroll.mp3")

PADDLE_HEIGHT = 20
PADDLE_WIDTH = 100
x_paddle = 205
y_paddle = 370
x1_paddle = 5

class Paddle(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PADDLE_WIDTH, PADDLE_HEIGHT))
        self.image.fill((0, 255, 0))
        pygame.draw.rect(self.image, (0, 255, 0), ((x_paddle, y_paddle), (PADDLE_WIDTH, PADDLE_HEIGHT)))
        self.rect = self.image.get_rect()
        self.rect.x = x_paddle
        self.rect.y = y_paddle
        self.direction = 0
        self.speed = x1_paddle

    def update(self):
        global timer
        global timer3
        global bonus_active
        global anti_active

        self.rect.x += self.direction * self.speed
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > WIDTH - PADDLE_WIDTH:
            self.rect.x = WIDTH - PADDLE_WIDTH

        if bonus_active:
            if timer != -1 and pygame.time.get_ticks() - timer <= 3000:
                self.image = pygame.Surface((PADDLE_WIDTH * 2, PADDLE_HEIGHT))
                self.image.fill((0, 255, 0))
                pygame.draw.rect(self.image, (0, 255, 0), ((x_paddle, y_paddle), (PADDLE_WIDTH * 2, PADDLE_HEIGHT)))
            else:
                timer = -1
                bonus_active = False
                self.image = pygame.Surface((PADDLE_WIDTH, PADDLE_HEIGHT))
                self.image.fill((0, 255, 0))
                pygame.draw.rect(self.image, (0, 255, 0), ((x_paddle, y_paddle), (PADDLE_WIDTH, PADDLE_HEIGHT)))
        else:
            if timer3 != -1 and pygame.time.get_ticks() - timer3 <= 3000:
                self.image = pygame.Surface((PADDLE_WIDTH / 2, PADDLE_HEIGHT))
                self.image.fill((0, 255, 0))
                pygame.draw.rect(self.image, (0, 255, 0), ((x_paddle, y_paddle), (PADDLE_WIDTH / 2, PADDLE_HEIGHT)))
            else:
                timer3 = -1
                anti_active = False
                self.image = pygame.Surface((PADDLE_WIDTH, PADDLE_HEIGHT))
                self.image.fill((0, 255, 0))
                pygame.draw.rect(self.image, (0, 255, 0), ((x_paddle, y_paddle), (PADDLE_WIDTH, PADDLE_HEIGHT)))





RADIUS = 10
x_ball = 200
y_ball = 200
x1_ball = 5
y1_ball = 2

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((RADIUS * 2, RADIUS * 2))
        self.image.fill((0, 0, 255))
        pygame.draw.circle(self.image, (0, 0, 255), (RADIUS, RADIUS), RADIUS)
        self.rect = self.image.get_rect()
        self.rect.x = x_ball
        self.rect.y = y_ball
        self.speed_x = x1_ball
        self.speed_y = y1_ball

    def update(self):
        global timer2
        global timer4
        global changed
        global bonus_active
        global anti_active
        global anti_changed

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.x < 0 or self.rect.x > WIDTH - RADIUS * 2:
            self.speed_x *= -1
        if self.rect.y < 0:
            self.speed_y *= -1

        if timer2 != -1:
            if pygame.time.get_ticks() - timer2 <= 3000:
                if not changed:
                    try:
                        self.speed_y = (self.speed_y / abs(self.speed_y)) * (abs(self.speed_y) - 1)
                        self.speed_x = (self.speed_x / abs(self.speed_x)) * (abs(self.speed_x) - 3)
                    except ZeroDivisionError:
                        self.speed_y = (self.speed_y / (abs(self.speed_y) + 1)) * (abs(self.speed_y) - 1)
                        self.speed_x = (self.speed_x / (abs(self.speed_x) + 1)) * (abs(self.speed_x) - 3)
                    changed = True
                else:
                    pass
            else:
                timer2 = -1
        elif timer2 == -1 and changed:
            try:
                self.speed_y = (self.speed_y / abs(self.speed_y)) * (abs(self.speed_y) + 1)
                self.speed_x = (self.speed_x / abs(self.speed_x)) * (abs(self.speed_x) + 3)
            except ZeroDivisionError:
                self.speed_y = (self.speed_y / (abs(self.speed_y) + 1)) * (abs(self.speed_y) + 1)
                self.speed_x = (self.speed_x / (abs(self.speed_x) + 1)) * (abs(self.speed_x) + 3)
            changed = False
            bonus_active = False

        if timer4 != -1:
            if pygame.time.get_ticks() - timer4 <= 3000:
                if not anti_changed:
                    try:
                        self.speed_y = (self.speed_y / abs(self.speed_y)) * (abs(self.speed_y) + 4)
                        self.speed_x = (self.speed_x / abs(self.speed_x)) * (abs(self.speed_x) + 3)
                    except ZeroDivisionError:
                        self.speed_y = (self.speed_y / (abs(self.speed_y) + 1)) * (abs(self.speed_y) + 4)
                        self.speed_x = (self.speed_x / (abs(self.speed_x) + 1)) * (abs(self.speed_x) + 3)
                    anti_changed = True
                else:
                    pass
            else:
                timer4 = -1
        elif timer4 == -1 and anti_changed:
            try:
                self.speed_y = (self.speed_y / abs(self.speed_y)) * (abs(self.speed_y) - 4)
                self.speed_x = (self.speed_x / abs(self.speed_x)) * (abs(self.speed_x) - 3)
            except ZeroDivisionError:
                self.speed_y = (self.speed_y / (abs(self.speed_y) + 1)) * (abs(self.speed_y) - 4)
                self.speed_x = (self.speed_x / (abs(self.speed_x) + 1)) * (abs(self.speed_x) - 3)
            anti_changed = False
            anti_active = False





BLOCK_WIDTH, BLOCK_HEIGHT = 50, 20
BLOCK_ROWS = 5
BLOCK_COLS = 7
BLOCK_MARGIN = 6
class Block(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([BLOCK_WIDTH, BLOCK_HEIGHT])
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

def create_blocks():
    block_list = pygame.sprite.Group()
    for row in range(1, BLOCK_ROWS):
        for col in range(BLOCK_COLS):
            block = Block(col * (BLOCK_WIDTH + BLOCK_MARGIN) + BLOCK_MARGIN,
            row * (BLOCK_HEIGHT + BLOCK_MARGIN) + BLOCK_MARGIN)
            block_list.add(block)

    return block_list

class Bonus(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((15, 15))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_y = 3

    def update(self):
        global timer2
        self.rect.y += self.speed_y
        if self.rect.y > HEIGHT:
            self.kill()

class Antibonus(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((15, 15))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_y = 3

    def update(self):
        global timer2
        self.rect.y += self.speed_y
        if self.rect.y > HEIGHT:
            self.kill()

def display(screen, lives):
    font = pygame.font.Font(None, 30)
    text = font.render(f'Жизни: {lives}                         Счет: {28 - len(blocks)}/28', True, (255, 255, 255))
    screen.blit(text, (10, 10))

# Настройки окна
HEIGHT = 400
WIDTH = 400
lives = 3

# Бонусы
bonus_active = False
timer = -1
timer2 = -1
bonus_counter = -1
changed = False

# АнтиБонусы
anti_active = False
timer3 = -1
timer4 = -1
antibonus_counter = -1
anti_changed = False

pygame.init()
screen = pygame.display.set_mode((HEIGHT, WIDTH))
done = False
clock = pygame.time.Clock()

paddle = Paddle()
ball = Ball()
blocks = create_blocks()
sprites = pygame.sprite.Group()


sprites.add(paddle)
sprites.add(ball)
sprites.add(blocks)


while not done:
    clock.tick(60)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                paddle.direction = -1
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                paddle.direction = 1
        else:
            paddle.direction = 0

    sprites.update()

    if lives <= 0:
        messagebox.showinfo('Конец игры', 'Жизни кончились')
        done = False
        exit()

    if len(blocks) == 0 :
        messagebox.showinfo('Конец игры', 'Вы выиграли!')
        done = False
        exit()


    if pygame.sprite.spritecollide(ball, blocks, dokill=True):
        ball.speed_y *= -1
        if random.randint(0, 1):
            sprite = Bonus(ball.rect.x, ball.rect.y)
        else:
            sprite = Antibonus(ball.rect.x, ball.rect.y)
        sprites.add(sprite)


    if pygame.sprite.collide_rect(ball, paddle):
        ball.speed_y *= -1

    for sprite in sprites:
        if isinstance(sprite, Bonus):
            if pygame.sprite.collide_rect(paddle, sprite):
                sprite.kill()
                if not bonus_active:
                    bonus_counter += 1
                    if bonus_counter % 4 == 2:
                        lives += 1
                    elif bonus_counter % 4 == 1:
                        timer2 = pygame.time.get_ticks()
                    elif bonus_active % 4 == 0:
                        timer = pygame.time.get_ticks()
                        pygame.mixer.music.play()
                    else:
                        pygame.mixer.music.play()

                    bonus_active = True

        elif isinstance(sprite, Antibonus):
            if pygame.sprite.collide_rect(paddle, sprite):
                sprite.kill()
                if not anti_active:
                    antibonus_counter += 1
                    if antibonus_counter % 3 == 2:
                        lives -= 1
                    elif antibonus_counter % 3 == 1:
                        timer4 = pygame.time.get_ticks()
                    else:
                        timer3 = pygame.time.get_ticks()
                    anti_active = True


    if ball.rect.y > HEIGHT:
        ball.rect.y = y_ball
        ball.rect.x = x_ball
        lives -= 1
        ball.speed_x += 2
        ball.speed_y += 2


    screen.fill((255, 137, 3))
    sprites.draw(screen)
    display(screen, lives)
    pygame.display.flip()