# water_tile.py

import pygame
from source.tiles.base_tile import BaseTile

class WaterTile(BaseTile):
    def draw(self, surface):
        pygame.draw.rect(surface, (0, 0, 255), self.get_rect())

    def isPassable(self):
        return False
