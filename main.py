# pylint: disable=no-member
import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_event, log_state
from player import Player


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroidsfield = AsteroidField()
    
    dt = 0
    inf = 0
    while inf == 0:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        # player.update(dt)
        # player.draw(screen)
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        #print(dt)


if __name__ == "__main__":
    main()
