import pygame
from bullet import Bullet
from life import Life

class Player:
    def __init__(self,main):
        self.center_x = main.width // 2
        self.center_y = main.height - 100
        self.change_x = 0
        self.change_y = 0
        self.width = 50
        self.height = 50
        self.image = "Images\\player.png"
        self.damaged = "Images\\playerDamaged.png"
        self.speed = 5
        self.main_width = main.width
        self.rect = pygame.Rect
        self.bullet_list = []
        self.lifes = []
        self.life_remove = False

    def move(self):
        if self.change_x == -1 and self.center_x > 5:
            self.center_x -= self.speed
        elif self.change_x == 1 and self.center_x < self.main_width - self.width - 5:
            self.center_x += self.speed


    def fire(self):
        new_Bullet = Bullet(self)
        self.bullet_list.append(new_Bullet)

    def hit(self):
        if len(self.lifes) != 0:
            self.lifes.pop()
            self.life_remove = True

    def create_lifes(self):
        for i in range(3):
            self.life = Life()
            if i != 0:
                self.life_location += self.life.width + 5
            else:
                self.life_location = self.life.center_x
            self.life.center_x = self.life_location
            self.lifes.append(self.life)