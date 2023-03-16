import pygame 

class Bullet(pygame.sprite.Sprite):
    def __init__(self, position, rotation, image):
        super().__init__()
        self.image = image 
        self.position = position
        self.rect = pygame.rect.Rect(0, 0, self.image.get_width(), self.image.get_height())
        self.speed = 4
        self.rotation = rotation
        