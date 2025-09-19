import pygame
class Bullet:
    def __init__(self,player):
        self.center_x = player.center_x + (player.width // 2)
        self.center_y = player.center_y - (player.height - 20)
        self.change_x = 0
        self.change_y = 0
        self.image = "Images\\laserRed.png"
        self.speed = 2
        self.rect = pygame.Rect

    def move(self):
        self.center_y -= self.speed