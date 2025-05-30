# Imports
import pygame
from source.game_state.game_state import GameState
from source.units.player import Player
from source.grid import Grid

# Set up the display and the variables needed for drawing the screen
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("My Game")
range = None
atk_option = False

def handle_input() -> None:
    for event in pygame.event.get():
        game_state.controller.handle_input(event, game_state)

def enqueue_npc_commands() -> None:
    pass

def route_cmds() -> None:
    for cmd in game_state.command_queue:
        cmd.resolve_target(game_state)
    game_state.command_queue.clear()  

def update_game_state() -> None:
    for obj in game_state.obj_in_grid:
        obj.update_state(game_state)

def draw_screen() -> None:
    grid.draw(screen)

    # Draw the grid's contents
    for obj in game_state.obj_in_grid:
        obj.draw(screen)

    # Update the display
    pygame.display.flip()

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("My Game")

test_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 2, 2, 0, 0, 2, 2, 0, 1],
    [1, 0, 2, 2, 0, 0, 2, 2, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 3, 3, 0, 0, 0, 1],
    [1, 0, 0, 0, 3, 3, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Set up the grid/map
grid: Grid = Grid.from_array(test_map)

# Set up game state
game_state = GameState(grid)
#test_unit = Player(60,0)
#game_state.obj_in_grid.append(test_unit)

# Clock
clock = pygame.time.Clock()

while True:
    dt = clock.tick(60) / 1000  # seconds
    game_state.dt = dt          # provide delta to units for movement pacing

    handle_input()              # Phase 1a: User input → command(s)
    enqueue_npc_commands()      # Phase 1b: AI/NPCs enqueue their own actions
    route_cmds()                # Phase 2a: Assign or enqueue the collected commands
    update_game_state()         # Phase 2b: Execute 1 step of commands + update animations/states
    draw_screen()               # Phase 3: Draw game world based on updated state