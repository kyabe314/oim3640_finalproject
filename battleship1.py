from engine import Player, Game


# setting up pygame
import pygame
pygame.init()
pygame.font.init()
pygame.display.set_caption("Battleship")
game_font = pygame.font.SysFont('fresansttf', 100)

# global variables
SQ_SIZE = 45
H_MARGIN = SQ_SIZE * 4
V_MARGIN = SQ_SIZE
WIDTH = SQ_SIZE * 10 * 2 + H_MARGIN
HEIGHT = SQ_SIZE * 10 * 2 + V_MARGIN
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
INDENT = 10
HUMAN1 = True
HUMAN2 = True

# colors
GREY = (40, 50, 60)
WHITE = (255, 250, 250)
GREEN = (50, 250, 200)
BLUE = (50, 150, 200)
RED = (250, 50, 100)
ORANGE = (250, 140, 20)
COLORS = {"U": GREY, "M": BLUE, "H": ORANGE, "S": RED}

# function to draw a grid
def draw_grid(player, left=0, top=0, search=False):
    for i in range(100):
        x = left + i % 10 * SQ_SIZE
        y = top + i // 10 * SQ_SIZE
        square = pygame.Rect(x, y, SQ_SIZE, SQ_SIZE)
        pygame.draw.rect(SCREEN, WHITE, square, width = 3)
        if search:
            x += SQ_SIZE // 2
            y += SQ_SIZE // 2
            pygame.draw.circle(SCREEN, COLORS[player.search[i]], (x, y), radius=SQ_SIZE//4)

# function to draw ships onto the position grids
def draw_ships(player, left=0, top=0):
    for ship in player.ships:
        x = left + ship.col * SQ_SIZE + INDENT
        y = top + ship.row * SQ_SIZE + INDENT
        if ship.orientation == 'h':
            width = ship.size * SQ_SIZE - 2*INDENT
            height = SQ_SIZE - 2*INDENT
        else:
            width = SQ_SIZE - 2*INDENT
            height = ship.size * SQ_SIZE - 2*INDENT
        rectangle = pygame.Rect(x, y, width, height)
        pygame.draw.rect(SCREEN, GREEN, rectangle, border_radius=10)

game = Game()

# pygame loop
animating = True
pausing = False
while animating:

    # track user interaction
    for event in pygame.event.get():

        # user closes the pygame window
        if event.type == pygame.QUIT:
            animating = False

        # use clicks on mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if not game.over and game.player1_turn and x < SQ_SIZE * 10 and y < SQ_SIZE * 10:
                row = y // SQ_SIZE
                col = x // SQ_SIZE
                index = row * 10 + col
                game.make_move(index)
            elif not game.over and not game.player1_turn and x > WIDTH - SQ_SIZE*10 and y > SQ_SIZE*10 + V_MARGIN:
                row = (y - SQ_SIZE*10 - V_MARGIN) // SQ_SIZE
                col = (x - SQ_SIZE*10 - H_MARGIN) // SQ_SIZE
                index = row * 10 + col
                game.make_move(index)

        # user presses key on keyboard
        if event.type == pygame.KEYDOWN:
            
            # escape key to close the animation
            if event.key == pygame.K_ESCAPE:
                animating = False

            # space bar to pause and unpause the animation
            if event.key == pygame.K_SPACE:
                pausing = not pausing

            # return key to restart the game
            if event.key == pygame.K_RETURN:
                game = Game()

    # execution
    if not pausing:

        # draw background
        SCREEN.fill(GREY)

        # draw search grids
        draw_grid(game.player1, search=True)
        draw_grid(game.player2, search=True, left=(WIDTH-H_MARGIN)//2 + H_MARGIN, top=(HEIGHT-V_MARGIN)//2 + V_MARGIN)

        # draw position grids
        draw_grid(game.player1, top=(HEIGHT-V_MARGIN)//2 + V_MARGIN)
        draw_grid(game.player2, left=(WIDTH-H_MARGIN)//2 + H_MARGIN)

        # draw ships onto position grids
        draw_ships(game.player1, top=(HEIGHT-V_MARGIN)//2 + V_MARGIN)
        draw_ships(game.player2, left=(WIDTH-H_MARGIN)//2 + H_MARGIN)

        # game over message
        if game.over:
            text = f'Player {str(game.result)} wins!'
            textbox = game_font.render(text, False, GREY, WHITE)
            SCREEN.blit(textbox, (WIDTH//2 - 240, HEIGHT//2 - 50))

        # update screen
        pygame.display.flip()