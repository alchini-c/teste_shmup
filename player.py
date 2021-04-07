import pygame
from pygame.locals import *
from bullet import Bullet


class Player(pygame.sprite.Sprite):
    def __init__(self, displaySurf):
        super().__init__()
        self.width = displaySurf.get_width()
        self.height = displaySurf.get_height()
        #self.image = pygame.image.load("Materials/Player.png")
        self.surf = pygame.Surface((50, 90))
        self.surf.fill("blueviolet")
        self.rect = self.surf.get_rect(center = (self.width / 2, self.height / 1.2))
        self.speed = 5

    def move(self):
        #print("right:", self.rect.right)
        pressed_keys = pygame.key.get_pressed()
        if self.rect.top > 0:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -self.speed)
        if self.rect.bottom < self.height:
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, self.speed)
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-self.speed, 0)
        if self.rect.right < self.width:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(self.speed, 0)


    #def draw(self, surface):
        #surface.blit(self.surf, self.rect)
        #surface.blit(self.image, self.rect)
