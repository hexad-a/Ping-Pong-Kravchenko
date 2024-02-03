from pygame import *

win_width = 900
win_height = 700
back = (200, 255, 255)
window = display.set_mode((win_width, win_height))
window.fill(back)

clock = time.Clock()
FPS = 60
game = True
speed = 10

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
        if keys[K_s] and self.rect.y < win_height - 80 :
            self.rect.y += self.speed
    def update_r(self) :
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80 :
            self.rect.y += self.speed

racket1 = Player('racket.png', 20, 350, 30, 60, 3)
racket2 = Player('racket.png', 860, 350, 30, 60, 3)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    racket1.update_l()
    racket1.reset()

    racket2.update_r()
    racket2.reset()

    display.update()
    clock.tick(FPS)