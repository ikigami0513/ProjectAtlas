import os
import json
import pygame
from typing import Dict, List, Tuple, Union
from graphics.atlas_manager import AtlasManager
from graphics.animation_manager import AnimationManager
from graphics.animation import Animation
from core.singleton import SingletonMeta


class TileModel:
    def __init__(self, type: str, texture: pygame.Surface):
        self.type = type
        self.texture = texture


class AnimatedTileModel:
    def __init__(self, type: str, animation: Animation):
        self.type = type
        self.animation = animation


class TileAtlas(metaclass=SingletonMeta):
    def __init__(self):
        self.tiles: Dict[str, Union[TileModel, AnimatedTileModel]] = {}

    def initialize(self, atlas_manager: AtlasManager, animation_manager: AnimationManager):
        with open(os.path.join("assets", "tiles.json"), "r") as f:
            tiles = json.load(f)

        for tile in tiles:
            if tile["type"] == "static":
                self.tiles[tile["name"]] = TileModel(tile["type"], atlas_manager.get(tile["atlas"]).get_sprite(tile["sprite"]))
            elif tile["type"] == "animated":
                self.tiles[tile["name"]] = AnimatedTileModel(tile["type"], animation=animation_manager.get(tile["animation"]))

        print(self.tiles)

class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_model: TileModel, pos: Tuple[int, int], groups: List[pygame.sprite.Group]):
        super().__init__(groups)
        self.image = tile_model.texture
        self.rect = self.image.get_rect(center=pos)


class AnimatedTile(pygame.sprite.Sprite):
    def __init__(self, tile_model: AnimatedTileModel, pos: Tuple[int, int], groups: List[pygame.sprite.Group]):
        super().__init__(groups)
        self.animation = tile_model.animation
        self.image = self.animation.current_frame
        self.rect = self.image.get_rect(center=pos)

    def update(self, delta_time: float):
        self.animation.update(delta_time)
        self.image = self.animation.current_frame
