import pygame
import random
from Spaceship import Spaceship
from Game import Game
from Asteroids import smallAsteroid,mediumAsteroid,bigAsteroid
from Star import Star

pygame.init()
pygame.font.init()
pygame.mixer.init()

window = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()

pygame.display.set_caption("Asteroid Adventure")

game = Game(window)
game.setBackground("background.png")
game.setLeaderboard("Leaderboard.txt")

rocket = Spaceship(window)

game.setTheme("theme.mp3")

def main():
    mainMenu()
    gameLoop()
    leaderboard()

def mainMenu():
    run = True
    fontTitle = pygame.font.Font("./Assets/mainmenuFont.TTF", 60)
    fontMenu = pygame.font.Font("./Assets/scoreFont.ttf", 20)
    title1 = fontTitle.render("Asteroid", 1, (255, 255, 255))
    title2 = fontTitle.render("Adventure", 1, (255, 255, 255))
    clickStart = fontMenu.render("→Click anywhere to start←", 1, (255,255,255))
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False

        game.printBackground()
        window.blit(title1, (120, 100))
        window.blit(title2, (80, 160))
        window.blit(clickStart, (140,340))
        pygame.display.update()

def gameLoop():
    run = True
    game.playTheme()
    game.score = 0
    rocket.setImage("rocket.png", 50, 77)
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        game.printBackground()
        keyPressed = pygame.key.get_pressed()

        game.spawnAsteroid()
        for asteroid in game.asteroids:
            if game.score < 50: asteroid.fall(1)
            else: asteroid.fall(2)
            asteroid.print()
            if rocket.hitbox.colliderect(asteroid.hitbox):
                game.readLeaderboard()
                game.writeLeaderboard()
                run = False

        game.spawnStar()
        for star in game.stars:
            star.print()
            star.fall()
            if rocket.hitbox.colliderect(star.hitbox):
                game.score += 10
                game.clearStar()
            if star.y >= 600:
                game.clearStar()

        rocket.move(keyPressed)
        rocket.print()

        game.calcScore()
        game.printScore(10,10)
        game.cleanAsteroid()
        pygame.display.update()

def leaderboard():
    game.stopTheme()
    game.clearAsteroids()
    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                gameLoop()
                game.stopTheme()
                game.clearAsteroids()

        game.printBackground()
        game.printLeaderboard()
        pygame.display.update()


if __name__ == "__main__":
    main()