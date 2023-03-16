'''Written by Elie Nayef Neama and Øyvind H. Ytterstad'''

import pygame
import math
from shipClass import *
from ObstacleClass import *
from BulletClass import *

WIDTH = 1024
HEIGHT = 768
BACKGROUND = "data/grid.png"
SHIP1 = "data/spaceShips_001.png"
SHIP2 = "data/spaceShips_007.png"
BULLET = "spaceMissiles_001.png"
OBSTACLE = "data/spaceBuilding_002.png"
# BULLET_HIT_SOUND = pygame.mixer.Sound("data/Gun+Silencer.mp3")

# HEALTH_FONT = pygame.font.SysFont("comicsans", 40)
# WINNER_FONT = pygame.font.SysFont("comicsans", 40)


class Game():

    def __init__(self, fps, screensize=(WIDTH, HEIGHT)):
        pygame.init()
        self.screen_size = screensize
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("Mayhem Clone")
        self.fps = fps
        self.delta_time = pygame.time.Clock().tick(self.fps) / 1000.0  # TODO fix tick
        self.background_sprite = pygame.image.load(BACKGROUND)
        self.player1 = Spaceship(SHIP1)
        self.player2 = Spaceship(SHIP2)
        self.max_speed = 250
        # self.obstacle = Obstacle((400, 400), OBSTACLE)

    ''' Game loop '''
    def run(self):

        self.start = True
        while self.start:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.start = False

            self.update()
            self.screen.fill([50, 50, 50])
            self.screen.blit(self.background_sprite, (0, 0))

            # Lager en midlertidig sprite som er rotert versjon av spaceship
            player_sprite = pygame.transform.rotate(
                self.player1.image, self.player1.rotation * 180.0 / math.pi)
            self.screen.blit(player_sprite, (self.player1.position.x - player_sprite.get_rect(
            ).center[0], self.player1.position.y - player_sprite.get_rect().center[1]))

            player_sprite = pygame.transform.rotate(
                self.player2.image, self.player2.rotation * 180.0 / math.pi)
            self.screen.blit(player_sprite, (self.player2.position.x - player_sprite.get_rect(
            ).center[0], self.player2.position.y - player_sprite.get_rect().center[1]))

            # pygame.display.update()
            pygame.display.flip()

        pygame.quit()

    ''' Returnerer en liste med booleanske verdier for om knapper på tastaturet blir trykket på. '''

    def keyboard_events(self):
        global inputs
        inputs = pygame.key.get_pressed()

        return inputs

    def update(self):

        # TODO gjør events global
        global events
        events = self.keyboard_events()

        if events[pygame.K_ESCAPE]:
            self.start = False

        # Resetter akselerasjonen
        self.player1.acceleration = pygame.math.Vector2(0, 0)

        self.player1.gravity_vector()
        # Player 1
        if events[pygame.K_a]:
            self.player1.rotation += self.player1.ROTATION_SPEED * self.delta_time

        if events[pygame.K_d]:
            self.player1.rotation -= self.player1.ROTATION_SPEED * self.delta_time

        if events[pygame.K_w]:
            self.player1.rocketOn = True
            self.player1.throttle_vector()
        else:
            self.player1.rocketOn = False

        if events[pygame.K_s]:
            self.player1.shooting = True
            self.player1.shoot()
        else:
            self.player1.shooting = False

        # Player 2
        # Resetter akselerasjonen
        self.player2.acceleration = pygame.math.Vector2(0, 0)
        self.player2.gravity_vector()

        if events[pygame.K_LEFT]:
            self.player2.rotation += self.player2.ROTATION_SPEED * self.delta_time

        if events[pygame.K_RIGHT]:
            self.player2.rotation -= self.player2.ROTATION_SPEED * self.delta_time

        if events[pygame.K_UP]:
            self.player2.rocketOn = True
            self.player2.throttle_vector()
        else:
            self.player2.rocketOn = False

        if events[pygame.K_DOWN]:
            self.player2.shooting = True
            self.player2.shoot()
        else:
            self.player2.shooting = False

        # Må lages for player2
        # Fartsgrense på romskipet
        self.player1.velocity += self.player1.acceleration * self.delta_time
        # 250 er grensa
        if self.player1.velocity.length() > self.max_speed:
            # Normalize bevarer retning og setter lengden på vektoren lik 1
            self.player1.velocity = self.player1.velocity.normalize()
            # Setter hastigheten til fartsgrensa
            self.player1.velocity *= self.max_speed

        self.player1.position += self.player1.velocity*self.delta_time

        # TODO player2 fartsgrense

        self.player2.velocity += self.player2.acceleration * self.delta_time
        if self.player2.velocity.length() > self.max_speed:

            self.player2.velocity.scale_to_length(self.max_speed)

        self.player2.position += self.player2.velocity*self.delta_time

        if self.player1.position.x < 0:
            self.player1.position.x = WIDTH - 10

        if self.player2.position.x < 0:
            self.player2.position.x = WIDTH - 10

        if self.player1.position.x > WIDTH:
            self.player1.position.x = 0 + 10

        if self.player2.position.x > WIDTH:
            self.player2.position.x = 0 + 10

        if self.player1.position.y < 0:
            self.player1.position.y = HEIGHT - 10

        if self.player2.position.y < 0:
            self.player2.position.y = HEIGHT - 10

        if self.player1.position.y > HEIGHT:
            self.player1.position.y = 0 + 10

        if self.player2.position.y > HEIGHT:
            self.player2.position.y = 0 + 10

        # Resetter rotasjonen til [0, 2*pi]
        if self.player1.rotation > 2*math.pi:
            self.player1.rotation -= 2*math.pi
        elif self.player1.rotation < 0:
            self.player1.rotation += 2*math.pi

        # Resetter rotasjonen til [0, 2*pi]
        if self.player1.rotation > 2*math.pi:
            self.player1.rotation -= 2*math.pi
        elif self.player1.rotation < 0:
            self.player1.rotation += 2*math.pi


# WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
if __name__ == "__main__":
    # WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
    game = Game(fps=60)
    game.run()
