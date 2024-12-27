import pygame
import math
from direction import Direction

def rush_animation(unit_pos, target, direction, grid):
    path = []
    back_steps = 4
    back_up_value = 0.1
    rush_steps = 3

    # Back the unit up slowly
    for i in range(1, back_steps + 1):
        if direction == Direction.UP or direction == Direction.DOWN:
            path.append((unit_pos[0], unit_pos[1] + grid.sqr_to_pos_no_center(-direction.value[1] * back_up_value * i)))
        else:
            path.append((unit_pos[0] + grid.sqr_to_pos_no_center(-direction.value[0] * back_up_value * i), unit_pos[1]))
    
    # Calculate the total distance and step size
    pos_after_backup = path[-1]
    if direction == Direction.UP or direction == Direction.DOWN:
        rush_distance = abs(target[1] - pos_after_backup[1])
    else:
        rush_distance = abs(target[0] - pos_after_backup[0])
    step_size = rush_distance / rush_steps

    # Rush forward
    if direction == Direction.UP or direction == Direction.DOWN:
        for i in range(1, rush_steps + 1):
            path.append((pos_after_backup[0], pos_after_backup[1] + (direction.value[1] * step_size * i)))
    else:
        for i in range(1, rush_steps + 1):
            path.append((pos_after_backup[0] + (direction.value[0] * step_size * i), pos_after_backup[1]))
    
    # Leap back to original position
    pos_after_rush = path[-1]

    if direction == Direction.UP or direction == Direction.DOWN:
        # Parabolic arc for vertical leap back
        if direction == Direction.UP:
            peak_height = -50  # Adjust the peak height for the leap
        else:
            peak_height = 50
        num_steps = 5
        for i in range(1, num_steps + 1):
            t = i / num_steps
            x = unit_pos[0]
            y = (1 - t) * pos_after_rush[1] + t * unit_pos[1] - peak_height * (4 * t * (1 - t))
            path.append((x, y))
    else:
        # Half-circle arc for horizontal leap back
        center_x = (unit_pos[0] + pos_after_rush[0]) / 2
        center_y = (unit_pos[1] + pos_after_rush[1]) / 2
        leap_back_circ_radius = math.sqrt((unit_pos[0] - pos_after_rush[0]) ** 2 + (unit_pos[1] - pos_after_rush[1]) ** 2) / 2
        hori_point_one = 180
        hori_point_two = 360
        step_size = 20
        
        if direction == Direction.LEFT:
            angle_start, angle_end, step_size = hori_point_one, hori_point_two, step_size
        else:  # Direction.RIGHT
            angle_start, angle_end, step_size = hori_point_two, hori_point_one, -step_size
       
        for angle in range(angle_start, angle_end, step_size):  # Adjust the step for smoother animation
            rad = math.radians(angle)
            x = center_x + leap_back_circ_radius * math.cos(rad)
            y = center_y + leap_back_circ_radius * math.sin(rad)
            path.append((x, y))
    path.append(unit_pos)
    return path
