from pygame import *
import time as time1

class GameSprite(sprite.Sprite):
    def __init__(self, p_image, speed,x, y, width=65, height=65):
        super().__init__()
        self.image = transform.scale(image.load(p_image), (width, height))
        self.rect = self.image.get_rect()
        self.speed = speed
        self.rect.x = x
        self.rect.y = y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player_l(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        
        if keys_pressed[K_DOWN] and self.rect.y < 300:
            self.rect.y += self.speed
        
class Player_r(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        
        if keys_pressed[K_s] and self.rect.y < 300:
            self.rect.y += self.speed

class Ball(GameSprite):
    speedx = 3
    speedy = 3
    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.y > 445:
            self.speedy -= self.speedy + self.speedy
            global finish, text_r, text_l, gol_l, gol_r, ten, answer
        
        elif self.rect.x > 655:
            self.speedx -= self.speedx + self.speedx
            # text_r = True
            gol_r += 1
            fale.play()

        elif self.rect.x < 0:
            self.speedx -= self.speedx + self.speedx
            # text_l = True
            gol_l +=1
            fale.play()
        
        elif self.rect.y <0:
            self.speedy -= self.speedy + self.speedy
    
        global ball, player_l, player_r
        tolk_l = sprite.collide_rect(player_l, ball)
        tolk_r = sprite.collide_rect(player_r, ball)
        
        if tolk_l:
            self.speedx -= self.speedx + self.speedx
            braek.play()

        if tolk_r:
            self.speedx -= self.speedx + self.speedx
            braek.play()

window = display.set_mode((700, 500))
display.set_caption("Ping Pong")

background = transform.scale(image.load('fantasyforest.png'), (700, 500))

player_r = Player_r("platform_v.png", 7, 20, 200, 20, 200)
player_l = Player_l("platform_v.png", 7, 660, 200, 20, 200)

ball = Ball("football.png", 3, 300, 200, 45, 45)

font.init()
text = font.SysFont("Arial", 20)
text1 = font.SysFont("Arial", 35)

lose_r = text.render("Проиграл правый игрок", True, (225,0,0))
lose_l = text.render("Проиграл левый игрок", True, (225,0,0))

text_l = False
text_r = False

mixer.init()
mixer.music.load('music.ogg')
mixer.music.play()

braek = mixer.Sound('break.wav')
fale = mixer.Sound('fale.wav')

clock = time.Clock()
FPS = 60

start_time = time1.time()
min = 0
ten = 0

gol_l = 0
gol_r = 0

answer = 0


game = True 
finish = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish:
        window.blit(background, (0,0))

        end_time = time1.time()
        total = round(end_time - start_time)
        

        player_r.reset()
        player_l.reset()

        player_r.update()
        player_l.update()

        ball.reset()
        ball.update()

        timer = text1.render(str(min)+":"+str(ten)+str(total), True, (0,0,0))
        window.blit(timer,(300, 10))

        answer1 = text1.render(str(gol_r), True, (0,0,0))
        answer2 = text1.render(str(gol_l), True, (0,0,0))

        window.blit(answer2,(635, 10))
        window.blit(answer1,(35, 10))

        if ten == 6:
            min += 1
            ten = 0

        if total == 10:
            ten += 1
            start_time = time1.time()

        if gol_l == 3:
            lose_r = text.render("Проиграл правый игрок!", True, (225,0,0))
            window.blit(lose_r, (230,450))
            finish = False
        
        if gol_r == 3:
            lose_l = text.render("Проиграл левый игрок!", True, (225,0,0))
            window.blit(lose_l, (230,450))
            finish = False

        # if  ten == 1 and total == 0 or ten == 2 and total == 0 or ten == 3 and total == 0 or ten == 4 and total == 0:
        #     answer = 1

        if min == 1 and ten == 2:
            lose_l = text1.render("Ничья!", True, (225,0,0))
            window.blit(lose_l, (285,450))
            finish = False
        

    clock.tick(FPS)
    display.update()






# #задай фон сцены
# background = transform.scale(image.load('background.png'), (700, 500))
# #создай 2 спрайта и размести их на сцене
# sprite1 = transform.scale(image.load('sprite1.png'), (100, 100))
# sprite2 = transform.scale(image.load('sprite2.png'), (100, 100))
# #обработай событие «клик по кнопке "Закрыть окно"»
# game = True
# clock = time.Clock()
# FPS = 60
# x1 = 100
# y1 = 300
# x2 = 300
# y2 = 300
# while game:
#     window.blit(background, (0,0))

#     window.blit(sprite1, (x1,y1))
#     window.blit(sprite2, (x2,y2))

#     keys_pressed = key.get_pressed()

#     for events in event.get():
#         if events.type == QUIT:
#             game = False

#     if keys_pressed[K_LEFT] and x1 > 5 :
#         x1 -= 10

#     if keys_pressed[K_RIGHT] and x1 <595:
#         x1 += 10

#     if keys_pressed[K_DOWN] and y1 <395:
#         y1 += 10

#     if keys_pressed[K_UP] and y1 >0 :
#         y1 -= 10

#     if keys_pressed[K_a] and x2 >-0:
#         x2 -=10

#     if keys_pressed[K_d]  and x2 <595:
#         x2 += 10

#     if keys_pressed[K_s] and y2 <395:
#         y2 += 10

#     if keys_pressed[K_w] and y2 >-0:
#         y2 -= 10

#     clock.tick(FPS)
#     display.update()
