import noise
from abc import ABC, abstractmethod
from typing import List, Tuple, Type
from world.tile import TileType
from world.tree import Tree, OakTree, SpruceTree, CactusTree


class Biome(ABC):
    def __init__(self, seed: int = 0, scale: float = 20.0):
        self.seed = seed
        self.scale = scale

    @abstractmethod
    def get_tile(self, x: int, y: int) -> TileType:
        pass

    @abstractmethod
    def get_tree_probabilities(self) -> Tuple[float, List[Tuple[Type[Tree], float]]]:
        pass


class PrairieBiome(Biome):
    def get_tile(self, x: int, y: int) -> TileType:
        value = noise.pnoise2(
            x / self.scale,
            y / self.scale,
            octaves=1,
            persistence=0.5,
            lacunarity=2.0,
            repeatx=999999,
            repeaty=999999,
            base=self.seed,
        )
        
        if value > -0.3:
            return TileType.GRASS
        else:
            return TileType.GRASS_PATTERN_1
    
    def get_tree_probabilities(self) -> Tuple[float, List[Tuple[Type, float]]]:
        return 0.01, [
            (OakTree, 0.7),
            (SpruceTree, 0.3),
        ]
    

class DesertBiome(Biome):
    def get_tile(self, x: int, y: int) -> TileType:
        value = noise.pnoise2(
            x / self.scale,
            y / self.scale,
            octaves=1,
            persistence=0.5,
            lacunarity=2.0,
            repeatx=999999,
            repeaty=999999,
            base=self.seed,
        )
        
        if value > -0.3:
            return TileType.SAND
        else:
            return TileType.SAND_PATTERN
    
    def get_tree_probabilities(self) -> Tuple[float, List[Tuple[Type, float]]]:
        return 0.001, [
            (CactusTree, 1.0)
        ]
    

class BeachBiome(Biome):
    def get_tile(self, x: int, y: int):
        return TileType.SAND
    
    def get_tree_probabilities(self):
        return 0.0, []
    

class OceanBiome(Biome):
    def get_tile(self, x: int, y: int):
        return TileType.WATER
    
    def get_tree_probabilities(self):
        return 0.0, []
