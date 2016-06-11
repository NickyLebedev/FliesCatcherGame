import pygame

class BaseClass(pygame.sprite.Sprite):

    allsprites = pygame.sprite.Group()

    def __init__(self, x, y, width, height, image_string):

        pygame.sprite.Sprite.__init__(self)
        BaseClass.allsprites.add(self)

        self.image = pygame.image.load(image_string)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.width = width
        self.height = height

class Bug(BaseClass):

    list = pygame.sprite.Group()

    def __init__(self, x, y, width, height, image_string):
        BaseClass.__init__(self, x, y, width, height, image_string)
        Bug.list.add(self)
        self.step, self.up = 0, 5
        self.jumping, self.go_down = False, False

    def motion(self, SCREENWIDTH, SCREENHEIGHT):

        location = self.rect.x + self.step
        if location < 0:
            self.step = 0
        elif location + self.width > SCREENWIDTH:
            self.step = 0


        self.rect.x += self.step

        max_jump = 75

        if self.jumping:
            if self.rect.y < max_jump:
                self.go_down = True

            if self.go_down:
                self.rect.y += self.up
            else:
                self.rect.y -= self.up
