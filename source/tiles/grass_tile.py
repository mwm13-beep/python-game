# grass_tile.py

import pygame
from source.tiles.base_tile import BaseTile

class GrassTile(BaseTile):
    def draw(self, surface):
        pygame.draw.rect(surface, (0, 255, 0), self.get_rect())

    def isPassable(self):
        return True
