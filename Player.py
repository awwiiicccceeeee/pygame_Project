import pygame, sys
from pygame.locals import *
#from Assignment6.Config import SPEED, playerimg, deathsound
import Config
pygame.init()


class Player:
    def __init__(self):
        self.speed = Config.SPEED
        self.sprite = Config.playerimg
        self.rect = self.sprite.get_rect(bottomleft=(200-(self.sprite.get_width()/2),Config.resolution[2]))
        self.alive = True
        self.health = 10
        self.deadSound = pygame.mixer.Sound(Config.deathsound)
        self.shootSprite = Config.shootImg
        self.shootSound = pygame.mixer.Sound(Config.shootSound)
        self.shootRect = self.shootSprite.get_rect(bottomleft=)
        self.shootSpeed = [20, 0]
        


    def move(self, keys):
        if keys[pygame.K_a]:
            if self.rect.left < 0:
                self.rect = self.rect.move(0)
            else:
                self.rect = self.rect.move(-self.speed, 0)
        if keys[pygame.K_d]:
            if self.rect.right > 480:
                self.rect = self.rect.move(0)
            else:
                self.rect = self.rect.move(self.speed, 0)
    def shoot(self, keys):
        if keys[pygame.K_w]:
            self.shootRect = self.rect.move(0, self.shootSpeed)
    def draw_shoot(self, surface):
        surface.blit(self.shootSprite, self.shootRect)

    def draw(self, surface):
        surface.blit(self.sprite, self.rect)


