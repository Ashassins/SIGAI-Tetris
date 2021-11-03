import pygame
import random
import tetris

pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

size = (400, 500)
screen = pygame.display.set_mode(size)

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
fps = 25
game = tetris(20, 10)
counter = 0

pressing_down = False

while (not done):
    if game.figure is None:
        game.new_figure()

    if counter % (fps // game.level // 2) == 0 or pressing_down:
        if game.state == "start":
            game.go_down()

            

pygame.quit()