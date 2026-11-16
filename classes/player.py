import pygame
import os

class Player:
    surface: pygame.surface
    rect: pygame.Rect
    x: int
    y: int
    gravity = 300
    speed = 1
    jump_power = 1

    def __init__(self, surface: pygame.surface, x: int, y: int):
        self.x = x
        self.y = y
        self.surface = surface

        image = pygame.image.load(os.path.join("resources", "player.png")).convert_alpha()
        self.image = image

        rect = image.get_rect()
        rect.x = x
        rect.y = y
        self.rect = rect

    def process(self, delta_time: float):
        temp_floor = 320
        if self.rect.y < temp_floor:
            self.rect.y += self.gravity * delta_time

    def draw(self):
        self.surface.blit(self.image, self.rect)

    def jump(self, delta_time: float):
        self.rect.y -= self.jump_power * delta_time

    def move_left(self, delta_time: float):
        self.rect.x -= self.speed * delta_time

    def move_right(self, delta_time: float):
        self.rect.x += self.speed * delta_time