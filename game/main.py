from game.base import *
from process import *

pygame.init()

SCREENWIDTH, SCREENHEIGHT = 640, 360
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT), 0, 32)

clock = pygame.time.Clock()
FPS = 25

bug = Bug(0, SCREENHEIGHT - 40, 40, 40, "game/images/bug.png")

while True:
    #PROCESSES
    process(bug)
    #PROCESSES
    #LOGIC
    bug.motion(SCREENWIDTH, SCREENHEIGHT)
    #LOGIC
    #DRAW
    screen.fill((0, 0, 0))
    BaseClass.allsprites.draw(screen)
    pygame.display.flip()
    #DRAW

    clock.tick(FPS)