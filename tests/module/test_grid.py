import pytest
from source.grid import Grid
from source.config import TILE_SIZE, TILE_CENTER
from source.tiles.tile_types import TILE_TYPES

class MockTile:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.draw_called = False
        self.draw_arg = None

    def draw(self, surface):
        self.draw_called = True
        self.draw_arg = surface

def test_grid_draw_calls_tile_draw():
    mock_surface = object()  # we don't care what this is, just pass it through

    # Create a 2x2 grid of mock tiles
    tile_rows = [
        [MockTile(0, 0), MockTile(1, 0)],
        [MockTile(0, 1), MockTile(1, 1)]
    ]
    grid = Grid(tile_rows)

    grid.draw(mock_surface)

    for row in tile_rows:
        for tile in row:
            assert tile.draw_called
            assert tile.draw_arg == mock_surface

@pytest.fixture
def simple_array():
    return [
        [0, 1],
        [1, 0]
    ]

def test_grid_initialization_from_array(simple_array):
    grid = Grid.from_array(simple_array)
    assert isinstance(grid, Grid)
    assert grid.rows == 2
    assert grid.cols == 2
    assert len(grid.tiles) == 2
    assert all(len(row) == 2 for row in grid.tiles)

def test_grid_tile_types_are_correct(simple_array):
    grid = Grid.from_array(simple_array)
    for y, row in enumerate(simple_array):
        for x, code in enumerate(row):
            expected_cls = TILE_TYPES.get(code)
            assert isinstance(grid.tiles[y][x], expected_cls)

def assert_tuple_of_type(value, expected_type):
    assert isinstance(value, tuple), f"Expected tuple, got {type(value)}"
    assert all(isinstance(v, expected_type) for v in value), \
        f"Expected all elements to be {expected_type}, got {[type(v) for v in value]}"

def test_grid_to_screen_coor():
    g = Grid([])
    result = g.grid_coor_to_screen_coor(2, 3)
    assert_tuple_of_type(result, float)
    assert result == (2 * TILE_SIZE, 3 * TILE_SIZE)

def test_grid_to_screen_coor_center():
    g = Grid([])
    x, y = 2, 3
    expected = (x * TILE_SIZE + TILE_CENTER, y * TILE_SIZE + TILE_CENTER)
    result = g.grid_coor_to_screen_coor_center(x, y)
    assert_tuple_of_type(result, float)
    assert result == expected

def test_screen_to_grid_index():
    g = Grid([])
    result = g.screen_to_grid_index(64, 128)
    assert_tuple_of_type(result, int)
    assert result == (64 // TILE_SIZE, 128 // TILE_SIZE)

def test_screen_to_grid_fuzzy():
    g = Grid([])
    import math
    result = g.screen_to_grid_fuzzy(65, 129)
    assert_tuple_of_type(result, int)
    assert result == (
        math.ceil(65 / TILE_SIZE), math.ceil(129 / TILE_SIZE)
    )

def test_screen_to_grid_center():
    g = Grid([])
    x, y = 128.0, 128.0
    expected = (
        x // TILE_SIZE * TILE_SIZE + TILE_CENTER,
        y // TILE_SIZE * TILE_SIZE + TILE_CENTER
    )
    result = g.screen_to_grid_center(x, y)
    assert_tuple_of_type(result, float)
    assert result == expected
