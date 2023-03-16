import pygame
import math


class Bullet(pygame.sprite.Sprite):
    def __init__(self, position, image):
        super().__init__()
        self.image = image 
        self.position = pygame.math.Vector2(position)
        self.rect = pygame.rect.Rect(0, 0, self.image.get_width(), self.image.get_height())
        self.speed = 4


    def draw_bullet(self):
        self.position += self.velocity
        self.rect.center = self.position