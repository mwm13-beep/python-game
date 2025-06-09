# stone_tile.py

import pygame
from source.tiles.base_tile import BaseTile

class StoneTile(BaseTile):
    def draw(self, surface):
        pygame.draw.rect(surface, (128, 128, 128), self.get_rect())

    def isPassable(self):
        return False
