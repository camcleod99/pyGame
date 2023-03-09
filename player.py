import pygame

from gameObject import GameObject


class Player(GameObject):
    def __init__(self, x, y, width, height, img_path, scale, speed, direction, direction_face):
        super().__init__(x, y, width, height, img_path, scale)
        self.speed = speed
        self.direction = direction
        self.direction_face = direction_face

    def setDirection(self, key):
        match key:
            case pygame.K_UP:
                self.direction = -1
            case pygame.K_DOWN:
                self.direction = 1

    def resetDirection(self):
        self.direction = 0

    def move(self, max_height):
        if (self.y >= max_height - self.height and self.direction > 0) or (self.y <= 0 and self.direction < 0):
            return

        self.y += (self.direction * self.speed)
