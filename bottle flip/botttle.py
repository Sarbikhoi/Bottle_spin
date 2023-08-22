import pygame
import sys
import math
import random

pygame.init()


screen_width = 1500
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bottle Spin Game")


floor_img = pygame.image.load("floor.png")
bottle_img = pygame.image.load("bottle.png")


bottle_img = pygame.transform.scale(bottle_img, (400, 600)) 


font = pygame.font.Font("Pacifico.ttf", 40) 
font_color = (255, 255, 255)

class Bottle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = bottle_img
        self.rect = self.image.get_rect(center=(screen_width // 2, screen_height // 2))
        self.angle = 0
        self.angular_velocity = 0
        self.is_spinning = False
        self.players = ["Player 1", "Player 2", "Player 3", "Player 4", "Player 5"] 
        self.winner = None

    def update(self):
        if self.is_spinning:
            self.angle += self.angular_velocity
            self.angular_velocity *= 0.99 

            if self.angular_velocity < 0.01: 
                self.is_spinning = False
            

        self.image = pygame.transform.rotate(bottle_img, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)



bottle = Bottle()
all_sprites = pygame.sprite.Group()
all_sprites.add(bottle)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not bottle.is_spinning:
                
                bottle.is_spinning = True
                bottle.angular_velocity = random.uniform(10, 20)
                

    all_sprites.update()


    screen.blit(floor_img, (0, 0))
    all_sprites.draw(screen)


    angle_sector = 360 / len(bottle.players)
    radius = 350

    for i, player_name in enumerate(bottle.players):
        angle = math.radians(-90 + angle_sector * i) 
        x = screen_width // 2 + radius * math.cos(angle)
        y = screen_height // 2 + radius * math.sin(angle)
        rotated_text = pygame.transform.rotate(font.render(player_name, True, font_color), -angle_sector * i)
        text_rect = rotated_text.get_rect(center=(x, y))
        screen.blit(rotated_text, text_rect.topleft)


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()