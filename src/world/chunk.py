import pygame
import noise
from typing import List
from world.tile import TileAtlas, TileType


class Chunk:
    def __init__(self, chunk_x: int, chunk_y: int, chunk_size: int, tile_size: int):
        self.chunk_x = chunk_x
        self.chunk_y = chunk_y
        self.chunk_size = chunk_size
        self.tile_size = tile_size
        
        self.tiles: List[List[TileType]] = []
        self.tile_atlas = TileAtlas()

        self.generate_tiles()

    def generate_tiles(self) -> None:
        for row in range(self.chunk_size):
            self.tiles.append([])
            for col in range(self.chunk_size):
                self.tiles[row].append(TileType.GRASS)
                
    def draw(self, surface: pygame.Surface, offset: pygame.Vector2) -> None:
        world_x = self.chunk_x * self.chunk_size * self.tile_size
        world_y = self.chunk_y * self.chunk_size * self.tile_size

        for row_index, row in enumerate(self.tiles):
            for col_index, tile_type in enumerate(row):
                tile_world_x = world_x + col_index * self.tile_size
                tile_world_y = world_y + row_index * self.tile_size

                screen_x = tile_world_x - offset.x
                screen_y = tile_world_y - offset.y

                tile = self.tile_atlas.tiles[tile_type]
                surface.blit(tile.texture, (screen_x, screen_y))

        chunk_rect = pygame.Rect(
            world_x - offset.x, 
            world_y - offset.y, 
            self.chunk_size * self.tile_size, 
            self.chunk_size * self.tile_size
        )
        pygame.draw.rect(surface, (0, 0, 0), chunk_rect, 1)
