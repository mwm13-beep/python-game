# tile.py

from abc import ABC, abstractmethod
from source.config import TILE_SIZE

class Tile(ABC):
    def __init__(self, x_index, y_index):
        self.x_index = x_index
        self.y_index = y_index
        self.size = TILE_SIZE
        self.center = (
            x_index * TILE_SIZE + TILE_SIZE // 2,
            y_index * TILE_SIZE + TILE_SIZE // 2
        )
        self.contents = []

    def get_rect(self):
        return (
            self.x_index * self.size,
            self.y_index * self.size,
            self.size,
            self.size
        )

    @abstractmethod
    def draw(self, surface):
        pass
    
    @abstractmethod
    def isPassable(self):
        pass
