import pygame
import os

class Block:
    surface: pygame.surface
    type: str
    rect: pygame.Rect
    x: int
    y: int

    def __init__(self, surface: pygame.surface, type: str, x: int, y: int):
        self.x = x
        self.y = y
        self.surface = surface

        image = pygame.image.load(os.path.join("resources", f"{type}.png")).convert_alpha()
        self.image = image

        rect = image.get_rect()
        rect.x = x
        rect.y = y
        self.rect = rect

    def draw(self):
        self.surface.blit(self.image, self.rect)