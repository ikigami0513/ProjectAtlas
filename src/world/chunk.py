import pygame
from typing import List
from world.tile import TileAtlas, Tile, AnimatedTile
from world.biome_manager import BiomeManager
from world.tree_generator import TreeGenerator
from world.tree import Tree
from core.settings import Settings


class Chunk:
    def __init__(self, chunk_x: int, chunk_y: int, chunk_size: int, tile_size: int, biome_manager: BiomeManager, tree_generator: TreeGenerator):
        self.chunk_x = chunk_x
        self.chunk_y = chunk_y
        self.chunk_size = chunk_size
        self.tile_size = tile_size
        
        self.tiles = pygame.sprite.Group()
        self.tile_atlas = TileAtlas()
        self.biome_manager = biome_manager

        self.tree_generator = tree_generator
        self.trees: List[Tree] = []

        self.generate_tiles()

    def generate_tiles(self) -> None:
        world_x = self.chunk_x * self.chunk_size * self.tile_size
        world_y = self.chunk_y * self.chunk_size * self.tile_size

        for row in range(self.chunk_size):
            for col in range(self.chunk_size):
                tile_world_x = world_x + col * self.tile_size
                tile_world_y = world_y + row * self.tile_size

                biome = self.biome_manager.get_biome(tile_world_x, tile_world_y)
                tile_model = TileAtlas().tiles[biome.get_tile(tile_world_x, tile_world_y)]
                if tile_model.type == "static":
                    Tile(tile_model, (tile_world_x, tile_world_y), self.tiles)
                elif tile_model.type == "animated":
                    AnimatedTile(tile_model, (tile_world_x, tile_world_y), self.tiles)

                tree = self.tree_generator.generate_tree(tile_world_x, tile_world_y, biome)
                if tree:
                    self.trees.append(tree)

    def update(self, delta_time: float):
        self.tiles.update(delta_time)
                
    def draw(self, surface: pygame.Surface, offset: pygame.Vector2) -> None:
        world_x = self.chunk_x * self.chunk_size * self.tile_size
        world_y = self.chunk_y * self.chunk_size * self.tile_size

        for tile in self.tiles:
            screen_pos = tile.rect.topleft - offset
            surface.blit(tile.image, screen_pos)

        if Settings.DEBUG:
            chunk_rect = pygame.Rect(
                world_x - offset.x, 
                world_y - offset.y, 
                self.chunk_size * self.tile_size, 
                self.chunk_size * self.tile_size
            )
            pygame.draw.rect(surface, (0, 0, 0), chunk_rect, 1)
