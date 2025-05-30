# # Imports
# import pygame
# import sys
# from source.game_state import GameState
# from source.units.player import Player
# from source.grid import Grid
# # from button import Button
# # from source.node import Node
# # from animation import rush_animation

# # Set up the display and the variables needed for drawing the screen
# screen = pygame.display.set_mode((800, 800))
# pygame.display.set_caption("My Game")
# range = None
# atk_option = False

# def draw_screen() -> None:
#     grid.draw(screen)

#     # Draw the grid's contents
#     for obj in game_state.obj_in_grid:
#         obj.draw(screen)

#     # Draw the range if there is one
#     # if range:
#     #     if atk_option:
#     #         color = (150, 0, 0, 128)  # Red with 50% transparency
#     #     else:
#     #         color = (0, 0, 150, 128)  # Blue with 50% transparency

#     #     # Create a surface with per-pixel alpha to apply transparency
#     #     surface = pygame.Surface((grid.grid_size, grid.grid_size), pygame.SRCALPHA)
#     #     surface.fill(color)

#     #     for square in range:
#     #         screen.blit(surface, (square.x - grid.grid_center, square.y - grid.grid_center))

#     # Draw the units
#     # for unit in turn_order:
#     #     unit.draw(screen, grid.unit_radius)

#     # Draw dialogue box
#     # draw_dialogue_box(screen)

#     # Update the display
#     pygame.display.flip()

# def handle_input() -> None:
#     for event in pygame.event.get():
#         game_state.controller.handle_input(event)
#     #     elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
#     #         grid_center = grid.get_grid_center(event.pos[0], event.pos[1])
#     #         if attack_button.is_clicked(event) and not disable_attack_action:
#     #             atk_option = True
#     #             range = grid.find_range((turn_order[turn].x, turn_order[turn].y), turn_order[turn].atk_range, atk_option)
#     #         elif move_button.is_clicked(event) and not disable_move_action:
#     #             atk_option = False
#     #             range = grid.find_range((turn_order[turn].x, turn_order[turn].y), turn_order[turn].movement, atk_option)
#     #         elif pass_button.is_clicked(event):
#     #             pass_turn = True
#     #         elif range:
#     #             grid_center = grid.get_grid_center(event.pos[0], event.pos[1])
#     #             selection = Node(grid_center[0], grid_center[1])
#     #             if selection in range:
#     #                 if atk_option:
#     #                     disable_attack_action = attack_action(selection)
#     #                 else:
#     #                     disable_move_action = move_action(selection)
#         # if (disable_move_action and disable_attack_action) or pass_turn:
#     #     disable_move_action = False
#     #     disable_attack_action = False
#     #     range = None
#     #     turn = (turn + 1) % len(turn_order)
#     #     pass_turn = False

# def update_game_state() -> None:
#     for command in game_state.command_queue:
#         command.execute

# # def draw_dialogue_box(screen):
# #     font = pygame.font.Font(None, 24)
# #     text = font.render("Turn: ", True, (255, 255, 255), (0, 0, 0))
# #     screen.blit(text, (615, 715))
# #     pygame.draw.rect(screen, turn_order[turn].color, (660, 715, 15, 15))
# #     attack_button.draw(screen)
# #     move_button.draw(screen)
# #     pass_button.draw(screen)

# # def attack_action(selection):
# #     global turn
# #     global range
# #     range = None
# #     steps = turn_order[turn].attack(selection, grid)
# #     if steps:
# #         for step in steps:
# #             turn_order[turn].move(step[0], step[1])
# #             draw_screen()
# #             pygame.time.delay(70)
# #     turn_order[turn].change_facing(selection.x, selection.y)
# #     dead = grid.objects_in_grid[(selection.x, selection.y)].take_damage(turn_order[turn])
# #     if dead:
# #         turn_order.remove(grid.objects_in_grid[(selection.x, selection.y)])
# #         turn = turn_order.index(turn_order[turn]) % len(turn_order)
# #         del grid.objects_in_grid[(selection.x, selection.y)]
# #     return True

# # def move_action(destination):
# #     global turn
# #     global range
# #     range = None
# #     path = grid.path_find((turn_order[turn].x, turn_order[turn].y), (destination.x, destination.y))
# #     if path:
# #         del grid.objects_in_grid[(turn_order[turn].x, turn_order[turn].y)]
# #         for step in path:
# #             turn_order[turn].move(step[0], step[1])
# #             draw_screen()
# #             pygame.time.delay(120)
# #         # Update the grid with the new position of the unit
# #         grid.objects_in_grid[(destination.x, destination.y)] = turn_order[turn]
# #     return path != None

# # Initializations
# # Initialize Pygame
# pygame.init()

# # Set up the display
# screen = pygame.display.set_mode((800, 800))
# pygame.display.set_caption("My Game")

# # #define units and turn order
# # turn = 0
# # turn_order = []
# # turn_order.append(Unit(grid.sqr_to_pos_center(0, 0), (0, 0, 255), 0, 5, 5, 3, 5, 1, rush_animation))
# # turn_order.append(Unit(grid.sqr_to_pos_center(2, 2), (255, 0, 0), 1, 5, 3, 2, 6, 1, rush_animation))

# # #UI buttons
# # attack_button = Button("Attack", 590, 740, 100, 50, (0, 0, 0), (100, 100, 100))
# # move_button = Button("Move", 695, 740, 100, 50, (0, 0, 0), (100, 100, 100))
# # pass_button = Button("Pass", 485, 740, 100, 50, (0, 0, 0), (100, 100, 100))

# # # Add the units to the grid
# # for unit in turn_order:
# #     grid.objects_in_grid[(unit.x, unit.y)] = unit

# # # Main game loop
# # selection = None
# # disable_attack_action = False
# # disable_move_action = False
# # pass_turn = False

# test_map = [
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
# [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
# [1, 0, 2, 2, 0, 0, 2, 2, 0, 1],
# [1, 0, 2, 2, 0, 0, 2, 2, 0, 1],
# [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
# [1, 0, 0, 0, 3, 3, 0, 0, 0, 1],
# [1, 0, 0, 0, 3, 3, 0, 0, 0, 1],
# [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
# [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# ]

# # Set up the grid/map
# grid: Grid = Grid.from_array(test_map)

# # Set up game state
# game_state = GameState(grid)
# test_unit = Player(60,0)
# game_state.obj_in_grid.append(test_unit)

# while True:
#     handle_input()         # Capture and store input events
#     update_game_state()    # Update all units, tile states, etc.
#     draw_screen()          # Redraw screen using updated data