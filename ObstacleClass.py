import pygame

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, position, image):
        super().__init__()
        self.position = pygame.Vector2(position)
        self.image = image
        self.rect = self.image.get_rect(position)
        