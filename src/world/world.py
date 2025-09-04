import pygame
from typing import Dict, Tuple
from world.chunk import Chunk
from world.biome_manager import BiomeManager
from world.tree_generator import TreeGenerator
from core.groups import AllSprites


class World:
    def __init__(self, all_sprites: AllSprites, chunk_size: int = 16, tile_size: int = 16, seed: int = 12):
        self.all_sprites = all_sprites
        self.chunk_size = chunk_size
        self.tile_size = tile_size
        self.chunks: Dict[Tuple[int, int], Chunk] = {}
        self.visible_chunks: Dict[Tuple[int, int], Chunk] = {}
        self.biome_manager = BiomeManager(seed=seed, scale=1000.0, continent_scale=1000.0)
        self.tree_generator = TreeGenerator(self.all_sprites, seed=seed, scale=100)

    def get_chunk(self, chunk_x: int, chunk_y: int) -> Chunk:
        chunk_key = (chunk_x, chunk_y)
        if chunk_key not in self.chunks:
            # Si le chunk n'existe pas, on le génère
            self.chunks[chunk_key] = Chunk(chunk_x, chunk_y, self.chunk_size, self.tile_size, self.biome_manager, self.tree_generator)

        return self.chunks[chunk_key]
    
    def update(self, delta_time: float, player_position: Tuple[int, int], render_distance: int = 2) -> None:
        current_chunk_x = int(player_position[0] // (self.chunk_size * self.tile_size))
        current_chunk_y = int(player_position[1] // (self.chunk_size * self.tile_size))

        new_visible_chunks = {}
        for dx in range(-render_distance, render_distance + 1):
            for dy in range(-render_distance, render_distance + 1):
                chunk_x = current_chunk_x + dx
                chunk_y = current_chunk_y + dy
                chunk = self.get_chunk(chunk_x, chunk_y)
                new_visible_chunks[(chunk_x, chunk_y)] = chunk

        self.visible_chunks = new_visible_chunks

        for chunk in self.visible_chunks.values():
            chunk.update(delta_time)

    def draw(self, surface: pygame.Surface, offset: pygame.Vector2) -> None:
        for chunk_pos, chunk in self.visible_chunks.items():
            chunk.draw(surface, offset)
