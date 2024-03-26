import pygame

class Spaceship:
    def __init__(self, window):
        self.window = window
        self.speed = 2.5

    def setImage(self, imageName, width, height, x=275, y=500):
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        self.rocket = pygame.image.load("./Assets/"+imageName)
        self.rocket = pygame.transform.scale(self.rocket, (width,height))
        self.hitbox = self.rocket.get_rect()
        self.hitbox.width = width-10    # Maak hitbox kleiner voor collision met grote asteroid
        self.hitbox.height = height-15

    def print(self):
        self.window.blit(self.rocket, (self.x, self.y))

    def move(self,keyPressed):
        if (keyPressed[pygame.K_RIGHT] or keyPressed[pygame.K_d]) and self.x < (self.window.get_width() - self.width):
            self.x += self.speed
            self.rocket = pygame.image.load("./Assets/rocketflames.png")
        elif (keyPressed[pygame.K_LEFT] or keyPressed[pygame.K_q]) and self.x > 0:
            self.x -= self.speed
            self.rocket = pygame.image.load("./Assets/rocketflames.png")
        if (keyPressed[pygame.K_UP] or keyPressed[pygame.K_z]) and self.y > 0:
            self.y -= self.speed
            self.rocket = pygame.image.load("./Assets/rocketflames.png")
        elif (keyPressed[pygame.K_DOWN] or keyPressed[pygame.K_s]) and self.y < (self.window.get_height() - self.height):
            self.y += self.speed
            self.rocket = pygame.image.load("./Assets/rocket.png")
        else:
            self.rocket = pygame.image.load("./Assets/rocketflamesmall.png")

        self.rocket = pygame.transform.scale(self.rocket, (self.width, self.height))
        self.hitbox.x = self.x + 5  # Verplaats kleinere hitbox naar het midde van het schip
        self.hitbox.y = self.y + 5