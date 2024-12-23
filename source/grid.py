import pygame
import heapq
from node import Node

class Grid:
    def __init__(self, grid_size = 50):
        self.grid_size = grid_size
        self.grid_center = self.grid_size // 2
        self.unit_radius = (self.grid_size - 10) // 2
        self.objects_in_grid = []

    def draw_grid(self, screen):
        for x in range(0, screen.get_width(), self.grid_size):
            pygame.draw.line(screen, (255, 255, 255), (x, 0), (x, screen.get_height()))
        for y in range(0, screen.get_height(), self.grid_size):
            pygame.draw.line(screen, (255, 255, 255), (0, y), (screen.get_width(), y))

    # Convert grid coordinates to screen coordinates
    def sqr_to_pos(self, x, y):
        return (x * self.grid_size + self.grid_center, y * self.grid_size + self.grid_center)
    
    def get_grid_center(self, x, y):
        return (x // self.grid_size * self.grid_size + self.grid_center, y // self.grid_size * self.grid_size + self.grid_center)
    
       # A* path finding algorithm
    def path_find(self, start, target):

        # Check if the target position is occupied
        if target in [(obj.x, obj.y) for obj in self.objects_in_grid]:
            return None
        start_node = Node(start[0], start[1])
        target_node = Node(target[0], target[1])
        open_list = []
        closed_list = []
        heapq.heappush(open_list, (start_node.f, start_node))

        while open_list:
            current_node = heapq.heappop(open_list)[1]
            closed_list.append(current_node)

            # If we have reached the target node, return the path
            if current_node == target_node:
                path = []
                while current_node:
                    path.append((current_node.x, current_node.y))
                    current_node = current_node.parent
                return path[::-1]

            # Get neighboring nodes' positions
            children = []
            for new_position in [(0, -self.grid_size), (0, self.grid_size), (-self.grid_size, 0), (self.grid_size, 0)]:
                node_position = (current_node.x + new_position[0], current_node.y + new_position[1])
                new_node = Node(node_position[0], node_position[1], current_node)
                
                # Skip nodes that are occupied by objects
                if (new_node.x, new_node.y) in [(obj.x, obj.y) for obj in self.objects_in_grid]:
                    continue
                
                children.append(new_node)

            # Loop through the children
            for child in children:
                if child in closed_list:
                    continue

                # Calculate the g, h, and f values
                child.g = current_node.g + self.grid_size
                child.h = ((child.x - target_node.x) ** 2) + ((child.y - target_node.y) ** 2)
                child.f = child.g + child.h

                # Check if the child is in the open list with a higher g value
                in_open_list = False
                for open_node in open_list:
                    if open_node[1] == child:
                        in_open_list = True
                        if child.g < open_node[1].g:
                            open_list.remove((child.f, child))
                            heapq.heapify(open_list)
                            heapq.heappush(open_list, (child.f, child))
                        break

                # If the child is not in the open list, add it
                if not in_open_list:
                    heapq.heappush(open_list, (child.f, child))
        return None
    
    def movement_range_find(self, start, movement):
        start_node = Node(start[0], start[1])
        open_list = []
        closed_list = []
        heapq.heappush(open_list, (start_node.f, start_node))

        while open_list:
            current_node = heapq.heappop(open_list)[1]
            closed_list.append(current_node)

            # If we have reached a square beyond the specified movement range then do not process it
            if current_node.g > movement * self.grid_size:
                continue

            # Get neighboring nodes' positions
            children = []
            for new_position in [(0, -self.grid_size), (0, self.grid_size), (-self.grid_size, 0), (self.grid_size, 0)]:
                node_position = (current_node.x + new_position[0], current_node.y + new_position[1])
                new_node = Node(node_position[0], node_position[1], current_node)
                
                # Skip nodes that are occupied by objects
                if (new_node.x, new_node.y) in [(obj.x, obj.y) for obj in self.objects_in_grid]:
                    continue
                
                children.append(new_node)

            # Loop through the children
            for child in children:
                if child in closed_list:
                    continue

                # Check if the child is in the open list
                in_open_list = False
                for open_node in open_list:
                    if open_node[1] == child:
                        in_open_list = True
                        break

                # If the child is not in the open list then calculate its g, h, and f values 
                # and add it to the list
                if not in_open_list:
                    child.g = current_node.g + self.grid_size
                    child.h = 0
                    child.f = child.g + child.h
                    heapq.heappush(open_list, (child.f, child))
        return closed_list