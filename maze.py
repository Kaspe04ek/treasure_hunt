import pygame
from time import sleep

 
pygame.init()
class GameSprite(pygame.sprite.Sprite):
    # Конструктор
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(player_image), (65,65))
        self.speed = player_speed
        # Создаем свойство Rect (координаты и размер нашего спрайта)
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    # Метод, для отрисовки спрайта
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[pygame.K_d] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[pygame.K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.y <= 270:
            self.direction = 'right'
        if self.rect.y >= 420:
            self.direction = 'left'

        if self.direction == 'left':
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed

class Wall(pygame.sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y,width,height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = width
        self.height = height
        self.image = pygame.Surface((self.width , self.height))
        self.image.fill((color_1 , color_2 , color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        window.blit(self.image , (self.rect.x , self.rect.y))

 
# Игровая сцена
win_width = 700
win_height = 500
window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Лабиринт")
background = pygame.transform.scale(pygame.image.load('background.jpg'), (win_width, win_height))
 
# Спрайты игры
W1 = Wall(0 , 255 , 0 , 70 , 0 , 10 , 380)
W2 = Wall(0 , 255 , 0 , 200 , 0 , 10 ,210)
W3 = Wall(0 , 255 , 0 , 200 , 290 ,10 ,300)
W4 = Wall(0 , 255 , 0 , 200 , 290 , 150 , 10 )
W5 = Wall(0 , 255 , 0 , 200 , 210 , 270 ,10)
W6 = Wall(0 , 255 , 0 , 460 , 210 , 10 ,180)
W7 = Wall(0 , 255 , 0 , 310 , 380 , 250 , 10)
W8 = Wall(0 , 255 , 0 , 200 , 210 , 150 ,10)
W9 = Wall(0 , 255 , 0 , 210 , 460 , 350 ,10)


player = Player('hero.png', 5, win_height - 80, 4)
monster = Enemy('cyborg.png', win_width - 200, 280, 2)
final = GameSprite('treasure.png', win_width - 120, win_height - 80, 0)

 
game = True
finish = False
clock = pygame.time.Clock()
FPS = 60
 
# музыка
pygame.mixer.init()
pygame.mixer.music.load('jungles.ogg')
pygame.mixer.music.play()
 
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    if finish != True:
        window.blit(background, (0 , 0))
        player.update()
        monster.update()
        final.update()
        W1.update()
        W2.update()
        W3.update()
        W4.update()
        W6.update()
        W7.update()
        W8.update()
        W9.update()


        if pygame.sprite.collide_rect(player, final):
            window.blit(win , (200 , 200))
            finish = True

        window.blit(background, (0, 0))
        player.reset()
        monster.reset()
        final.reset()
        W1.draw_wall()
        W2.draw_wall()
        W3.draw_wall()
        W4.draw_wall()
        W5.draw_wall()
        W6.draw_wall()
        W7.draw_wall()
        W8.draw_wall()
        W9.draw_wall()

        
    
    if pygame.sprite.collide_rect(player, monster):
        game = False

        
    if pygame.sprite.collide_rect(player, W1 ):
        player.rect.x = 5
        player.rect.y = 420
    if pygame.sprite.collide_rect(player, W2 ):
        player.rect.x = 5
        player.rect.y = 420
    if pygame.sprite.collide_rect(player, W3 ):
        player.rect.x = 5
        player.rect.y = 420
    if pygame.sprite.collide_rect(player, W4 ):
        player.rect.x = 5
        player.rect.y = 420
    if pygame.sprite.collide_rect(player, W5 ):
        player.rect.x = 5
        player.rect.y = 420
    if pygame.sprite.collide_rect(player, W6 ):
        player.rect.x = 5
        player.rect.y = 420
    if pygame.sprite.collide_rect(player, W7 ):
        player.rect.x = 5
        player.rect.y = 420
    if pygame.sprite.collide_rect(player, W8 ):
        player.rect.x = 5
        player.rect.y = 420
    if pygame.sprite.collide_rect(player, W9):
        player.rect.x = 5
        player.rect.y = 420
    

       

 
    pygame.display.update()
    clock.tick(FPS)

pygame.display.update()





