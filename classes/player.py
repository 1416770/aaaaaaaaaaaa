import pygame
import os
from classes.block import Block

class Player:
    surface: pygame.surface
    rect: pygame.Rect
    gravity = 0.4
    speed = 0.5
    jump_power = 5
    last_mined = 0
    mining_cooldown = 1000

    def __init__(self, surface: pygame.surface, x: int, y: int):
        self.surface = surface

        image = pygame.image.load(os.path.join("resources", "player.png")).convert_alpha()
        self.image = image

        rect = image.get_rect()
        rect.x = x
        rect.y = y
        self.rect = rect

    def get_nearest_block(self, blocks: list[Block]) -> Block:
        player_position = pygame.Vector2(self.rect.x, self.rect.y)
        nearest_block = None
        nearest_distance = 10000

        for block in blocks:
            if block.is_breakable():
                block_position = pygame.Vector2(block.rect.x, block.rect.y)

                distance = player_position.distance_to(block_position)
                if distance < nearest_distance:
                    nearest_distance = distance
                    nearest_block = block

        return nearest_block, nearest_distance

    def is_grounded(self) -> bool:
        nearest_block = self.get_nearest_block()
        
        return self.rect.y >= nearest_block.rect.y

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

    def mine(self, blocks: list[Block]):
        ticks = pygame.time.get_ticks()
        if (ticks - self.last_mined) >= self.mining_cooldown:
            self.last_mined = ticks

            nearest_block, nearest_distance = self.get_nearest_block(blocks)
            if nearest_block and nearest_distance <= 70:
                nearest_block.destroy()