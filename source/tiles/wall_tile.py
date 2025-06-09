# wall_tile.py

import pygame
from source.tiles.base_tile import BaseTile

class WallTile(BaseTile):
    def draw(self, surface):
        pygame.draw.rect(surface, (150, 75, 0), self.get_rect())

    def isPassable(self):
        return False
