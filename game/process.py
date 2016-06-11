import pygame, sys

def process(bug):
    #PROCESSES
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        bug.image = pygame.image.load("game/images/Bugflipped.png")
        bug.step = -5
    elif keys[pygame.K_d]:
        bug.image = pygame.image.load("game/images/bug.png")
        bug.step = 5
    else:
        bug.step = 0

    if keys[pygame.K_w]:
        bug.jumping = True

    #PROCESSES