import pygame
import random


class Enemy(pygame.sprite.Sprite):
    def __init__(self, displaySurf):
        super().__init__()
        self.screen_width = displaySurf.get_width()
        self.screen_height = displaySurf.get_height()
        #self.image = pygame.image.load("Materials/Enemy.png")
        self.surf = pygame.Surface((50, 90))
        self.surf.fill("red")
        self.rect = self.surf.get_rect(center=((random.randint(30, self.screen_width - 50), 0)))
        self.speed = 2
        self.life = 3

    def shooted(self):
        print("shooted")
        self.life -= 1
        if self.life == 0:
            self.life = 3
            self.rect.top = 0
            self.rect.center = (random.randint(30, 350), 0)
            print("kill")

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.bottom > self.screen_height:
            self.rect.top = 0
            self.rect.center = (random.randint(30, 350), 0)

    #def draw(self, surface):
    #   surface.blit(self.surf, self.rect) #surface do jogo (surface do retangulo, retangulo)
    #   surface.blit(self.image, self.rect)
