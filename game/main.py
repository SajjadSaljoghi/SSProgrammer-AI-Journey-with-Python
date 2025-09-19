import random
import pygame
from player import Player
from enemy import Enemy

class Main():
    def __init__(self):
        self.width = 800
        self.height = 600
        self.fps = 60
        self.caption = "Interstaller Game"
        self.bg = "Images\\backgroundColor.png"
        self.bg_speed_line = "Images\\speedLine.png"
        self.bg_star_big = "Images\\starBig.png"
        self.player = Player(self)
        self.enemies = []
        self.life_location = 0
        self.change_time = 0

    def run(self):
        pygame.init()
        pygame.mixer.init()
        screen = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption(self.caption)
        clock = pygame.time.Clock()
        bg = pygame.image.load(self.bg)
        scale_bg = pygame.transform.scale(bg,(self.width,self.height))

        bg_s_l = pygame.image.load(self.bg_speed_line)
        bg_star_big = pygame.image.load(self.bg_star_big)

        pygame.mixer.music.load("Sounds\\SkyFire.ogg")
        pygame.mixer.music.play(-1)

        explosion_sound = pygame.mixer.Sound("Sounds\\explosion.wav")
        laser_sound = pygame.mixer.Sound("Sounds\\laser.wav")

        player_image = pygame.image.load(self.player.image).convert_alpha()
        scale_player = pygame.transform.scale(player_image,(self.player.width,self.player.height))
        

        self.player.create_lifes()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.player.change_x = -1
                    elif event.key == pygame.K_RIGHT:
                        self.player.change_x = 1
                    elif event.key == pygame.K_SPACE:
                        self.player.fire()
                        laser_sound.play()

                if event.type == pygame.KEYUP:
                    self.player.change_x = 0
            screen.blit(scale_bg,(0,0))
            screen.blit(bg_s_l,(random.randint(0,self.width),random.randint(0,self.height)))
            screen.blit(bg_star_big,(500,random.randint(0,self.height)))
            screen.blit(bg_star_big,(400,random.randint(0,self.height)))
            screen.blit(bg_star_big,(300,random.randint(0,self.height)))
            screen.blit(bg_star_big,(200,random.randint(0,self.height)))
            screen.blit(bg_star_big,(100,random.randint(0,self.height)))
            screen.blit(bg_star_big,(600,random.randint(0,self.height)))
            screen.blit(bg_star_big,(700,random.randint(0,self.height)))
            screen.blit(scale_player,(self.player.center_x,self.player.center_y))
            screen.blit(scale_player,(self.player.center_x,self.player.center_y))
            

            self.player.move()
            self.player.rect = scale_player.get_rect(topleft=(self.player.center_x,self.player.center_y))
            
            
            if len(self.enemies) <= 1000 and random.randint(1,150) == 6:
                self.enemy = Enemy(self)
                self.enemies.append(self.enemy)
            
            for l in self.player.lifes:
                life_image = pygame.image.load(l.image).convert_alpha()
                scale_life = pygame.transform.scale(life_image,(l.width,l.height))
                screen.blit(scale_life,(l.center_x,l.center_y))

            for e in self.enemies:
                enemy_image = pygame.image.load(e.image).convert_alpha()
                scale_enemy = pygame.transform.scale(enemy_image,(e.width,e.height))
                screen.blit(scale_enemy,(e.center_x,e.center_y))
                e.rect = scale_enemy.get_rect(topleft=(e.center_x,e.center_y))
                e.move()

                if self.player.rect.colliderect(e.rect):
                    player_image = pygame.image.load(self.player.damaged).convert_alpha()
                    scale_player = pygame.transform.scale(player_image,(self.player.width,self.player.height))
                    self.change_time = pygame.time.get_ticks()
                    explosion_sound.play()
                    if not self.player.life_remove:
                        self.player.hit()
                
                if e.remove(self):
                    self.enemies.remove(e)
                    self.player.hit()

            for b in self.player.bullet_list:
                bullet_image = pygame.image.load(b.image).convert_alpha()
                screen.blit(bullet_image,(b.center_x,b.center_y))
                b.move()
                b.rect = bullet_image.get_rect(topleft=(b.center_x,b.center_y))
                for e in self.enemies:
                    if b.rect.colliderect(e.rect):
                        explosion_sound.play()
                        self.enemies.remove(e)
                        self.player.bullet_list.remove(b)


            
            if pygame.time.get_ticks() - self.change_time >= 3000:       
                player_image = pygame.image.load(self.player.image).convert_alpha()
                scale_player = pygame.transform.scale(player_image,(self.player.width,self.player.height))
                self.change_time = 0
                self.player.life_remove = False

            pygame.display.flip()
            clock.tick(60)
        pygame.quit()


game = Main()
game.run()
