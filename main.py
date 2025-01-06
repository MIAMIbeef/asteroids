import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
import sys

def main():
    pygame.init()

    # welcome message and screen width and height
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # define FPS
    clock = pygame.time.Clock()
    # delta time
    dt = 0

  
    # groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    AsteroidField.containers = updatable
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (updatable, drawable)

    player = Player((SCREEN_WIDTH /2), (SCREEN_HEIGHT / 2))
    ast_field = AsteroidField()

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        for obj in updatable:
            obj.update(dt)
        for obj in drawable:
            obj.draw(screen)      
        for obj in asteroids:
            if obj.collision(player):
                sys.exit("Game Over!")
        
        pygame.display.flip()
        tick = clock.tick(60)
        dt = tick/1000
        player.timer -= dt

if __name__ == "__main__":
    main()
