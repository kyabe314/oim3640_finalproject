# setting up pygame
import pygame
pygame.init()
pygame.display.set_caption("Battleship")

# global variables
SQ_SIZE = 45
H_MARGIN = SQ_SIZE * 4
V_MARGIN = SQ_SIZE
WIDTH = SQ_SIZE * 10 * 2 + H_MARGIN
HEIGHT = SQ_SIZE * 10 * 2 + V_MARGIN
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

# colors
GREY = (40, 50, 60)
WHITE = (255, 250, 250)

# function to draw a grid
def draw_grid(left=0, top=0):
    for i in range(100):
        x = left + i % 10* SQ_SIZE
        y = top + i // 10 * SQ_SIZE
        square = pygame.Rect(x, y, SQ_SIZE, SQ_SIZE)
        pygame.draw.rect(SCREEN, WHITE, square, width = 3)


# pygame loop
animating = True
pausing = False
while animating:

    # track user interaction
    for event in pygame.event.get():

        # user closes the pygame window
        if event.type == pygame.QUIT:
            animating = False

        # user presses key on keyboard
        if event.type == pygame.KEYDOWN:
            
            # escape key to close the animation
            if event.key == pygame.K_ESCAPE:
                animating = False

            # space bar to pause and unpause the animation
            if event.key == pygame.K_SPACE:
                pausing = not pausing

    # execution
    if not pausing:

        # draw background
        SCREEN.fill(GREY)

        # draw search grids
        draw_grid()
        draw_grid(left=(WIDTH-H_MARGIN)//2 + H_MARGIN, top=(HEIGHT-V_MARGIN)//2 + V_MARGIN)

        # draw position grids
        draw_grid(left=(WIDTH-H_MARGIN)//2 + H_MARGIN)
        draw_grid(top=(HEIGHT-V_MARGIN)//2 + V_MARGIN)

        # update screen
        pygame.display.flip()