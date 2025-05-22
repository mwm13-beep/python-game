# grass_tile.py

import pygame
from source.tiles.tile import Tile

class GrassTile(Tile):
    def draw(self, surface):
        pygame.draw.rect(surface, (0, 255, 0), self.get_rect())

    def isPassable(self):
        return True
