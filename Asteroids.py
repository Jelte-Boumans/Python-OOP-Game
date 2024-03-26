import pygame
import random

class Asteroids:
    def __init__(self, window, x, y=0):
        self.window = window
        self.normalSpeed = 1
        self.randomSpeed = random.uniform(0.5,2.5)
        self.x = x
        self.y = y

    def print(self):
        self.window.blit(self.asteroid, (self.x, self.y))

    def fall(self, difficulty):
        if difficulty == 1:
            self.y += self.normalSpeed
        elif difficulty == 2:
            self.y += self.randomSpeed
        self.hitbox.x = self.x
        self.hitbox.y = self.y

class smallAsteroid(Asteroids):
    def __init__(self, window, x, y=-18):
        super().__init__(window, x, y)
        self.asteroid = pygame.image.load("./Assets/smallasteroid.png")
        self.width = self.asteroid.get_width()
        self.height = self.asteroid.get_height()
        self.hitbox = self.asteroid.get_rect()

class mediumAsteroid(Asteroids):
    def __init__(self, window, x, y=-31):
        super().__init__(window, x, y)
        self.asteroid = pygame.image.load("./Assets/mediumasteroid.png")
        self.width = self.asteroid.get_width()
        self.height = self.asteroid.get_height()
        self.hitbox = self.asteroid.get_rect()

class bigAsteroid(Asteroids):
    def __init__(self, window, x, y=-61):
        super().__init__(window, x, y)
        self.asteroid = pygame.image.load("./Assets/bigasteroid.png")
        self.width = self.asteroid.get_width()
        self.height = self.asteroid.get_height()
        self.hitbox = self.asteroid.get_rect()