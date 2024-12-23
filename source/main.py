# Imports
import pygame
import sys
from unit import Unit
from grid import Grid
from button import Button
from node import Node

# Functions
# Function for drawing the screen
def draw_screen(screen, movement_range = None):
    # Fill the screen with black (RGB)
    screen.fill((0, 0, 0))

    # Draw the grid
    grid.draw_grid(screen)

    # Draw the movement range if there is one
    if movement_range:
        for square in movement_range:
            pygame.draw.rect(screen, (0, 255, 0), (square.x - grid.grid_center, square.y - grid.grid_center, grid.grid_size, grid.grid_size))

    # Draw the unit
    for unit in turn_order:
        unit.draw(screen, grid.unit_radius)

    # Draw dialogue box
    draw_dialogue_box(screen)

    # Update the display
    pygame.display.flip()

def draw_dialogue_box(screen):
    font = pygame.font.Font(None, 24)
    text = font.render("Turn: ", True, (255, 255, 255), (0, 0, 0))
    screen.blit(text, (615, 715))
    pygame.draw.rect(screen, turn_order[turn].color, (660, 715, 15, 15))
    for button in buttons:
        button.draw(screen)

def attack_action():
    print("Attack")

def move_action(event):
    global turn
    movement_range = grid.movement_range_find((turn_order[turn].x, turn_order[turn].y), turn_order[turn].movement)
    selection = None
    while selection is None or selection not in movement_range:
        draw_screen(screen, movement_range)
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            grid_center = grid.get_grid_center(event.pos[0], event.pos[1])
            selection = Node(grid_center[0], grid_center[1])
    path = grid.path_find((turn_order[turn].x, turn_order[turn].y), (selection.x, selection.y))
    if path:
        for step in path:
            turn_order[turn].move(step[0], step[1])
            draw_screen(screen)
            pygame.time.delay(120)
    turn = (turn + 1) % len(turn_order)

# Initializations
# Initialize Pygame
pygame.init()

# Set up the grid/map
grid = Grid()

# Set up the display
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("My Game")

#define units and turn order
turn = 0
turn_order = []
turn_order.append(Unit(grid.sqr_to_pos(0, 0), (0, 0, 255), 0, 15, 5, 3, 5))
turn_order.append(Unit(grid.sqr_to_pos(2, 2), (255, 0, 0), 1, 20, 3, 2, 6))

#UI buttons
buttons = []
buttons.append(Button("Attack", 590, 740, 100, 50, (0, 0, 0), (100, 100, 100), attack_action))
buttons.append(Button("Move", 695, 740, 100, 50, (0, 0, 0), (100, 100, 100), move_action))

# add objects to the grid
for unit in turn_order:
    grid.objects_in_grid.append(unit)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for button in buttons:
                if button.is_clicked(event):
                    break
    draw_screen(screen)