import pygame
import sys
import heapq

# Define the Node class to assist with A* path finding
class Node:
    def __init__(self, x, y, parent=None):
        self.x = x
        self.y = y
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __lt__(self, other):
        return self.f < other.f

class Unit:
    def __init__(self, x, y, color, id = 0):
        self.x = x
        self.y = y
        self.color = color
        self.id = id

    def move(self, dx, dy):
        self.x = dx
        self.y = dy

    def draw(self, screen, radius):
        pygame.draw.circle(screen, self.color, (self.x, self.y), radius)

    # A* path finding algorithm
    def path_find(self, target, grid_size, objects_in_grid):
        # Check if the target position is occupied
        if target in [(obj.x, obj.y) for obj in objects_in_grid]:
            return None
        start_node = Node(self.x, self.y)
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
            for new_position in [(0, -grid_size), (0, grid_size), (-grid_size, 0), (grid_size, 0)]:
                node_position = (current_node.x + new_position[0], current_node.y + new_position[1])
                new_node = Node(node_position[0], node_position[1], current_node)
                
                # Skip nodes that are occupied by objects
                if (new_node.x, new_node.y) in [(obj.x, obj.y) for obj in objects_in_grid]:
                    continue
                
                children.append(new_node)

            # Loop through the children
            for child in children:
                if child in closed_list:
                    continue

                # Calculate the g, h, and f values
                child.g = current_node.g + grid_size
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

def draw_screen(screen, grid_size):
    # Fill the screen with a color (RGB)
    screen.fill((0, 0, 0))

    #Draw the grid
    for x in range(0, screen.get_width(), grid_size):
        pygame.draw.line(screen, (255, 255, 255), (x, 0), (x, screen.get_height()))
    for y in range(0, screen.get_height(), grid_size):
        pygame.draw.line(screen, (255, 255, 255), (0, y), (screen.get_width(), y))

    # Draw the unit
    for unit in turn_order:
        unit.draw(screen, unit_radius)

    # Update the display
    pygame.display.flip()

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Game")

#Define the grid size
grid_size = 50
grid_center = grid_size // 2
unit_radius = (grid_size - 10) // 2
objects_in_grid = []

#define units
blue_unit = Unit(0 + grid_center, 0 + grid_center, (0, 0, 255), 0)
red_unit = Unit(100 + grid_center, 100 + grid_center, (255, 0, 0), 1)

#turn tracking
number_of_units = 2
turn = 0
turn_order = [blue_unit, red_unit]

# add objects to the grid
for unit in turn_order:
    objects_in_grid.append(unit)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            target = (event.pos[0] // grid_size * grid_size + grid_center, event.pos[1] // grid_size * grid_size + grid_center)
            if target in [(obj.x, obj.y) for obj in objects_in_grid]:
                continue
            path = turn_order[turn].path_find(target, grid_size, objects_in_grid)
            if path:
                for step in path:
                    turn_order[turn].move(step[0], step[1])
                    draw_screen(screen, grid_size)
                    pygame.time.delay(120)
            turn = (turn + 1) % number_of_units

    draw_screen(screen, grid_size)