import pygame
import random
import tetris
from tetris import Tetris
import piece

pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

size = (400, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("SIGAI Tetris")
# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
fps = 25
print("marker")
game = Tetris(20, 10)
counter = 0

pressing_down = False

screen.fill(WHITE)

while (not done):
    if game.piece is None:
        game.newPiece()

    counter += 1
    if counter > 100000:
        counter = 0
    if counter % (game.level // 2) == 0 or pressing_down:
        if game.state == "start":
            game.move_down()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                game.rotateClockwise()
            if event.key == pygame.K_DOWN:
                pressing_down = True
            if event.key == pygame.K_LEFT:
                game.move_sideways(-1)
            if event.key == pygame.K_RIGHT:
                game.move_sideways(1)
            if event.key == pygame.K_SPACE:
                game.go_space()
            if event.key == pygame.K_ESCAPE:
                game.__init__(20, 10)

    if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                pressing_down = False

    screen.fill(WHITE)

    for i in range(game.height):
        for j in range(game.width):
            pygame.draw.rect(screen, GRAY, [game.x + game.zoom * j, game.y + game.zoom * i, game.zoom, game.zoom], 1)
            if game.field[i][j] > 0:
                pygame.draw.rect(screen, colors[game.field[i][j]],
                                 [game.x + game.zoom * j + 1, game.y + game.zoom * i + 1, game.zoom - 2, game.zoom - 1])

    if game.piece is not None:
        print("game Figure not none")
        print(game.piece.image())
        for i in range(4):
            for j in range(4):
                print("piece num ") # + j + "x" + i)
                if game.piece.image()[i][j] > 0:
                    print("draw piece")
                    pygame.draw.rect(screen, game.piece.color,
                                    [game.x + game.zoom * (j + game.piece.x) + 1,
                                    game.y + game.zoom * (i + game.piece.y) + 1,
                                    game.zoom - 2, game.zoom - 2])

    font = pygame.font.SysFont('Calibri', 25, True, False)
    font1 = pygame.font.SysFont('Calibri', 65, True, False)
    text = font.render("Score: " + str(game.score), True, BLACK)
    text_game_over = font1.render("Game Over", True, (255, 125, 0))
    text_game_over1 = font1.render("Press ESC", True, (255, 215, 0))

    screen.blit(text, [0, 0])
    if game.state == "gameover":
        screen.blit(text_game_over, [20, 200])
        screen.blit(text_game_over1, [25, 265])

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()