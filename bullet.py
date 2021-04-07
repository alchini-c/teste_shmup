import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.surf = pygame.Surface((5, 10))
        self.surf.fill("white")
        self.rect = self.surf.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speed = -10

    def move(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()

