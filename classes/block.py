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

    def generate_model(self):
        image = pygame.image.load(os.path.join("resources", f"{self.type}.png")).convert_alpha()
        self.image = image
        self.rect = image.get_rect()

    def __init__(self, surface: pygame.surface, type: str, x: int, y: int):
        self.x = x
        self.y = y
        self.surface = surface
        self.type = type
        self.generate_model()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        self.surface.blit(self.image, self.rect)

    def is_breakable(self) -> bool:
        return self.type 

    def destroy(self):
        self.type = "sky"
        self.generate_model()