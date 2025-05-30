from source.tiles.grass_tile import GrassTile
from source.tiles.water_tile import WaterTile
from source.tiles.wall_tile import WallTile
from source.tiles.stone_tile import StoneTile

TILE_TYPES = {
    0: GrassTile,
    1: WallTile,
    2: WaterTile,
    3: StoneTile,
}