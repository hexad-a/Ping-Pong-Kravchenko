from pygame import *
from random import randint

win_width = 900
win_height = 700
back = (200, 255, 255)
window = display.set_mode((win_width, win_height))
window.fill(back)

clock = time.Clock()
FPS = 60
game = True
finish = False
speed = 10
score1 = 0
score2 = 0

speed_x = 3
speed_y = 3

font.init()
font1 = font.SysFont('Arial', 80)
font2 = font.SysFont('Arial', 40)
win1 = font1.render('Переміг гравець 2', True, (28, 133, 4))
win2 = font1.render('Переміг гравець 1', True, (28, 133, 4))

class GameSprite(sprite.Sprite) :
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self) :
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite) :
    def update_l(self) :
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 140 :
            self.rect.y += self.speed
    def update_r(self) :
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 140 :
            self.rect.y += self.speed

rocket1 = Player('racket.png', 20, 280, 50, 150, 5)
rocket2 = Player('racket.png', 830, 280, 50, 150, 5)
ball = GameSprite('tenis_ball.png', 400, 330, 50, 50, 5)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True :

        rocket1.update_l()
        rocket1.reset()

        rocket2.update_r()
        rocket2.reset()

        ball.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(rocket1, ball) or sprite.collide_rect(rocket2, ball) :
            speed_x *= -1
            speed_y *= -1

        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < 0:
            finish = True 
            window.blit(win1, (200, 200))
            score2 = 1

        if ball.rect.x > win_width:
            finish = True 
            window.blit(win2, (200, 200))
            score1 = 1

        text1 = font2.render('Рахунок 1 гравця: ' + str(score1),  1, (255, 0, 0))
        window.blit(text1, (265, 20))

        text2 = font2.render('Рахунок 2 гравця: ' + str(score2),  1, (255, 0, 0))
        window.blit(text2, (265, 630))

    display.update()
    clock.tick(FPS)