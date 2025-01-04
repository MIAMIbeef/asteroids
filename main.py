import pygame
from constants import *
from circleshape import *
from player import *

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

    player = Player((SCREEN_WIDTH /2), (SCREEN_HEIGHT / 2))
    
    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        player.update(dt)
        player.draw(screen)     
        pygame.display.flip()
        tick = clock.tick(60)
        dt = tick/1000

if __name__ == "__main__":
    main()
