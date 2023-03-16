import pygame
import math


class Spaceship(pygame.sprite.Sprite):

    BOOSTER_SPEED = 200.0
    ROTATION_SPEED = 3.0
    GRAVITY_SPEED = 99  # m/s^2

    def __init__(self, img):
        super().__init__()

        self.image = pygame.image.load(img).convert_alpha()
        self.velocity = pygame.math.Vector2(0, 0)
        self.position = pygame.math.Vector2(0, 0)
        self.acceleration = pygame.math.Vector2(0, 0)
        # self.gas = int(1000)
        self.rotation = 0.0  # i radianer
        self.rocketOn = False
        self.shooting = False
        
        # Is standing on ground. No gravity!
        # self.grounded = True

    ''' Returnerer en retningsvektor for hvor skipet peker.'''
    def forward_dir(self):
        direction = pygame.math.Vector2(0, 1)
        direction = direction.rotate_rad(-self.rotation)
        return direction

    ''' Metode som akselererer skipet nedover, som gravitasjon.'''
    def gravity_vector(self):
        self.acceleration += self.GRAVITY_SPEED * pygame.math.Vector2(0, 1)

    ''' Metode for å legge til rakettens vektor.'''
    def throttle_vector(self):
        if self.rocketOn:
            self.acceleration -= self.forward_dir() * self.BOOSTER_SPEED

    def shoot(self):
        if self.shooting:
            # TODO
            pass



    
