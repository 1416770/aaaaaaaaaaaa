import pygame
import os

temp_floor = 320

class Player:
    surface: pygame.surface
    rect: pygame.Rect
    x: int
    y: int
    gravity = 0.4
    speed = 0.5
    jump_power = 5
    last_mined = 0
    mining_cooldown = 2

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

    def is_grounded(self) -> bool:
        return self.rect.y >= temp_floor

    def process(self, delta_time: float):
        if not self.is_grounded():
            self.rect.y += self.gravity * delta_time

    def draw(self):
        self.surface.blit(self.image, self.rect)

    def jump(self, delta_time: float):
        if self.is_grounded():
            self.rect.y -= self.jump_power * delta_time

    def move_left(self, delta_time: float):
        self.rect.x -= self.speed * delta_time

    def move_right(self, delta_time: float):
        self.rect.x += self.speed * delta_time

    def mine(self, elapsed: float):
        if (elapsed - self.last_mined) >= self.mining_cooldown:
            self.last_mined = elapsed

            
        print("mine")