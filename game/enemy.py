import random
import pygame


class Enemy:
    def __init__(self,main):
        self.center_x = random.randint(50,main.width - 50)
        self.center_y = -50
        self.width = 40
        self.height = 40
        self.angle = 0
        self.image = "Images\\enemyShip.png"
        self.speed = 1.5
        self.rect = pygame.Rect

    def move(self):
        self.center_y += self.speed
    
    def remove(self,main):
        if self.center_y >= main.height:
            return True
