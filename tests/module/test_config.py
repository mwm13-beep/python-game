import pytest
from source.config import TILE_SIZE, TILE_CENTER

def test_tile_size_is_numeric():
    assert isinstance(TILE_SIZE, (int, float)), "TILE_SIZE must be a number"

def test_tile_center_is_numeric():
    assert isinstance(TILE_CENTER, (int, float)), "TILE_CENTER must be a number"

def test_tile_center_is_half_tile_size():
    assert TILE_CENTER == TILE_SIZE / 2, "TILE_CENTER should be half of TILE_SIZE"
