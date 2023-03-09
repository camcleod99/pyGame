import pygame

from gameObject import GameObject


class Enemy(GameObject):
    def __init__(self, x, y, width, height, img_path, scale, speed, direction, direction_face, level):
        super().__init__(x, y, width, height, img_path, scale)
        self.speed = speed
        self.direction = direction
        self.direction_face = direction_face
        self.level = level

    def move(self, max_width):
        if (self.x <= 0) or (self.x >= max_width - self.width):
            self.direction = self.direction * -1

        self.x += (self.direction * self.speed)
