import pygame
import os

immune_block_types = [
    "cloud",
    "sky",
    "player"
]

class Block:
    surface: pygame.surface
    type: str
    rect: pygame.Rect
    x: int
    y: int

    def set_type(self, type: str, x = 0, y = 0):
        self.type = type

        image = pygame.image.load(os.path.join("resources", f"{type}.png")).convert_alpha()
        self.image = image

        rect = image.get_rect()
        rect.x = x
        rect.y = y
        self.rect = rect

    def __init__(self, surface: pygame.surface, type: str, x: int, y: int):
        self.x = x
        self.y = y
        self.surface = surface
        self.set_type(type, x, y)

    def draw(self):
        self.surface.blit(self.image, self.rect)

    def is_breakable(self) -> bool:
        return self.type not in immune_block_types

    def destroy(self):
        self.type = "sky"
        self.generate_model()