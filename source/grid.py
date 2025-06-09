from typing import List, Tuple
# import heapq
import math

import pygame
from source.tiles.base_tile import BaseTile
from source.tiles.tile_types import TILE_TYPES
from source.config import TILE_SIZE, TILE_CENTER

class Grid:
    def __init__(self, tile_rows: List[List[BaseTile]]) -> None:
        self.tiles = tile_rows
        self.rows = len(tile_rows)
        self.cols = len(tile_rows[0]) if self.rows > 0 else 0

    def draw(self, surface: pygame.Surface) -> None:
        for row in self.tiles:
            for tile in row:
                tile.draw(surface)

    @classmethod
    def from_array(cls, array2d: List[List[int]]) -> "Grid":
        tile_rows = []
        for y, row in enumerate(array2d):
            tile_row = []
            for x, tile_code in enumerate(row):
                tile_cls = TILE_TYPES.get(tile_code, TILE_TYPES[0])  # default fallback is grass
                tile = tile_cls(x, y)
                tile_row.append(tile)
            tile_rows.append(tile_row)
        return cls(tile_rows)

    # Convert grid coordinates to screen coordinates
    @classmethod
    def grid_coor_to_screen_coor(self, x: int, y: int) -> Tuple[float, float]:
        return (x * TILE_SIZE, y * TILE_SIZE)

    @classmethod
    def grid_coor_to_screen_coor_center(self, x: int, y: int) -> Tuple[float, float]:
        return (x * TILE_SIZE + TILE_CENTER, y * TILE_SIZE + TILE_CENTER)
    
    # Convert screen coordinates to grid coordinates
    @classmethod
    def screen_to_grid_index(self, x: float, y: float) -> Tuple[int, int]:
        return int(x // TILE_SIZE), int(y // TILE_SIZE)
    
    @classmethod
    def screen_to_grid_fuzzy(self, x: float, y: float) -> Tuple[int, int]:
        return (math.ceil(x / TILE_SIZE), math.ceil(y / TILE_SIZE))
    
    @classmethod
    def screen_to_grid_center(self, x: float, y: float) -> Tuple[float, float]:
        return (x // TILE_SIZE * TILE_SIZE + TILE_CENTER, y // TILE_SIZE * TILE_SIZE + TILE_CENTER)
    
    # # A* path finding algorithm
    # def path_find(self, start, target):
    #     # Check if the target position is occupied
    #     if target in self.objects_in_grid:
    #         return None
    #     start_node = Node(start[0], start[1])
    #     target_node = Node(target[0], target[1])
    #     open_list = []
    #     closed_list = []
    #     heapq.heappush(open_list, (start_node.f, start_node))

    #     while open_list:
    #         current_node = heapq.heappop(open_list)[1]
    #         closed_list.append(current_node)

    #         # If we have reached the target node, return the path
    #         if current_node == target_node:
    #             path = []
    #             while current_node:
    #                 path.append((current_node.x, current_node.y))
    #                 current_node = current_node.parent
    #             return path[::-1]

    #         # Get neighboring nodes' positions
    #         children = []
    #         for new_position in [(0, -TILE_SIZE), (0, TILE_SIZE), (-TILE_SIZE, 0), (TILE_SIZE, 0)]:
    #             node_position = (current_node.x + new_position[0], current_node.y + new_position[1])
    #             new_node = Node(node_position[0], node_position[1], current_node)
                
    #             # Skip nodes that are occupied by objects
    #             if (new_node.x, new_node.y) in self.objects_in_grid:
    #                 continue
                
    #             children.append(new_node)

    #         # Loop through the children
    #         for child in children:
    #             if child in closed_list:
    #                 continue

    #             # Calculate the g, h, and f values
    #             child.g = current_node.g + TILE_SIZE
    #             child.h = ((child.x - target_node.x) ** 2) + ((child.y - target_node.y) ** 2)
    #             child.f = child.g + child.h

    #             # Check if the child is in the open list with a higher g value
    #             in_open_list = False
    #             for open_node in open_list:
    #                 if open_node[1] == child:
    #                     in_open_list = True
    #                     if child.g < open_node[1].g:
    #                         open_list.remove((child.f, child))
    #                         heapq.heapify(open_list)
    #                         heapq.heappush(open_list, (child.f, child))
    #                     break

    #             # If the child is not in the open list, add it
    #             if not in_open_list:
    #                 heapq.heappush(open_list, (child.f, child))
    #     return None
    
    # def find_range(self, start, range, atk_option):
    #     start_node = Node(start[0], start[1])
    #     open_list = []
    #     closed_list = []
    #     heapq.heappush(open_list, (start_node.f, start_node))

    #     while open_list:
    #         current_node = heapq.heappop(open_list)[1]
    #         closed_list.append(current_node)

    #         # If we have reached a square at or beyond the specified range then do not process it
    #         if current_node.g >= range * TILE_SIZE:
    #             continue

    #         # Get neighboring nodes' positions
    #         children = []
    #         for new_position in [(0, -TILE_SIZE), (0, TILE_SIZE), (-TILE_SIZE, 0), (TILE_SIZE, 0)]:
    #             node_position = (current_node.x + new_position[0], current_node.y + new_position[1])
    #             new_node = Node(node_position[0], node_position[1], current_node)
                
    #             # Skip nodes that are occupied by objects
    #             if not atk_option:
    #                 if (new_node.x, new_node.y) in self.objects_in_grid:
    #                     continue
                
    #             children.append(new_node)

    #         # Loop through the children
    #         for child in children:
    #             if child in closed_list:
    #                 continue

    #             # Check if the child is in the open list
    #             in_open_list = False
    #             for open_node in open_list:
    #                 if open_node[1] == child:
    #                     in_open_list = True
    #                     break

    #             # If the child is not in the open list then calculate its g, h, and f values 
    #             # and add it to the list
    #             if not in_open_list:
    #                 child.g = current_node.g + TILE_SIZE
    #                 child.h = 0
    #                 child.f = child.g + child.h
    #                 heapq.heappush(open_list, (child.f, child))
        
    #     # By default, units cannot target their own square
    #     closed_list.remove(start_node)
    #     return closed_list