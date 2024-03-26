import pygame

class Star:
    def __init__(self, window, x, y=-48):
        self.window = window
        self.speed = 4.5
        self.x = x
        self.y = y
        self.star = pygame.image.load("./Assets/star.png")
        self.hitbox = self.star.get_rect()

    def print(self):
        self.window.blit(self.star, (self.x, self.y))

    def fall(self):
        self.y += self.speed
        self.hitbox.x = self.x
        self.hitbox.y = self.y