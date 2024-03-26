import pygame
import time
import random
from Star import Star
from Asteroids import smallAsteroid,mediumAsteroid,bigAsteroid

class Game:
    def __init__(self, window):
        self.window = window
        self.score = 0
        self.startTime = time.time()
        self.asteroids = []
        self.stars = []



    # Background methods
    def setBackground(self,background):
        self.background = pygame.image.load("./Assets/"+background)

    def printBackground(self):
        self.window.blit(self.background, (0, 0))



    # Score methods
    def calcScore(self):
        currentTime = time.time()
        if currentTime - self.startTime >= 1:
            self.score += 1
            str(self.score)
            self.startTime = time.time()

    def printScore(self, x, y):
        fontScore = pygame.font.Font("./Assets/scoreFont.ttf", 40)
        score = fontScore.render("Score: " + str(self.score), 1, (255, 255, 255))
        self.window.blit(score, (x, y))



    # Theme methods
    def setTheme(self, theme):
        self.theme = pygame.mixer.Sound("./Assets/"+theme)

    def playTheme(self):
        self.theme.play(-1)
        self.theme.set_volume(0.5)

    def stopTheme(self):
        self.theme.stop()



    # Asteroid methods
    def spawnAsteroid(self):
        if len(self.asteroids) < 20:
            if random.randint(0, 300) in [6, 59, 47]:
                self.asteroids.append(bigAsteroid(self.window, random.randint(0, 538)))
            if random.randint(0, 300) in [8, 75, 98, 24]:
                self.asteroids.append(mediumAsteroid(self.window, random.randint(0, 569)))
            if random.randint(0, 300) in [85, 37, 18, 65, 26]:
                self.asteroids.append(smallAsteroid(self.window, random.randint(0, 582)))

    def cleanAsteroid(self):
        for asteroid in self.asteroids:
            if asteroid.y >= 600:
                self.asteroids.remove(asteroid)

    def clearAsteroids(self):
        self.asteroids = []



    # Leaderboard methods
    def setLeaderboard(self, leaderboard):
        self.leaderboard = "./Assets/" + leaderboard

    def readLeaderboard(self):
        leaderboardFile = open(self.leaderboard, "r")
        self.leaderboardList = leaderboardFile.read().split(",")
        i = 0
        for score in self.leaderboardList:
            self.leaderboardList[i] = int(score)
            i += 1
        i = 0

        self.leaderboardList.append(self.score)
        self.leaderboardList.sort(reverse=True)
        self.leaderboardList.pop()
        leaderboardFile.close()

    def writeLeaderboard(self):
        leaderboardFile = open('./Assets/Leaderboard.txt', "w")
        i = 0
        for score in self.leaderboardList:
            if i != 4:
                leaderboardFile.write(str(score) + ",")
            else:
                leaderboardFile.write(str(score))
            i += 1
        i = 0
        leaderboardFile.close()

    def printLeaderboard(self):
        fontTitle = pygame.font.Font("./Assets/mainmenuFont.TTF", 60)
        fontScore = pygame.font.Font("./Assets/scoreFont.ttf", 40)
        fontMenu = pygame.font.Font("./Assets/scoreFont.ttf", 20)
        title1 = fontTitle.render("Game Over", 1, (255, 255, 255))
        title2 = fontTitle.render("Leaderboard", 1, (255, 255, 255))
        clickStart = fontMenu.render("→Click anywhere to restart←", 1, (255, 255, 255))
        self.window.blit(title1, (70, 100))
        self.window.blit(title2, (30, 180))
        self.window.blit(clickStart, (135,550))
        i = 1
        for score in self.leaderboardList:
            scoreText = fontScore.render(f"{i}. {score}" , 1, (255, 255, 255))
            self.window.blit(scoreText, (250,(40*i)+270))
            i += 1
        i = 1



    # Star methods
    def spawnStar(self):
        if len(self.stars) < 1:
            if random.randint(0, 2000) == 111:
                self.stars.append(Star(self.window, random.randint(0, 552)))

    def clearStar(self):
        self.stars = []