import pygame


class GameObject:

    def __init__(self, x, y, width, height, img_path, scale):
        image = pygame.image.load(img_path)
        self.x = x
        self.y = y

        if scale is None:
            self.width = width
            self.height = height
            self.image = pygame.transform.scale(image, (width, height))
        else:
            self.width = width * scale[0]
            self.height = height * scale[1]
            self.image = pygame.transform.scale(image, (width * scale[0], height * scale[1]))
