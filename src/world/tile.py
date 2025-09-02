from enum import Enum
import pygame
from typing import Dict
from graphics.atlas_manager import AtlasManager
from core.singleton import SingletonMeta


class TileType(Enum):
    GRASS = "grass"
    GRASS_PATTERN_1 = "grass_pattern_1"
    SAND = "sand"
    WATER = "water"


class TileModel:
    def __init__(self, type: TileType, texture: pygame.Surface):
        self.type = type
        self.texture = texture


class TileAtlas(metaclass=SingletonMeta):
    def __init__(self):
        self.tiles: Dict[TileType, TileModel] = {}

    def initialize(self, atlas_manager: AtlasManager):
        self.tiles[TileType.GRASS] = TileModel(TileType.GRASS, atlas_manager.get("tiles/grass/grass_3_middle").get_sprite("grass"))
        self.tiles[TileType.GRASS_PATTERN_1] = TileModel(TileType.GRASS_PATTERN_1, atlas_manager.get("tiles/grass/grass_3").get_sprite("grass_pattern_1"))
        self.tiles[TileType.SAND] = TileModel(TileType.SAND, atlas_manager.get("tiles/beach/beach").get_sprite("sand"))
        self.tiles[TileType.WATER] = TileModel(TileType.WATER, atlas_manager.get("tiles/water/water_middle_1").get_sprite("frame_0"))
