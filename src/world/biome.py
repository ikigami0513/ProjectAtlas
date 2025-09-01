from abc import ABC, abstractmethod
from typing import List, Tuple, Type
from world.tile import TileType
from world.tree import Tree, OakTree, SpruceTree, CactusTree


class Biome(ABC):
    @abstractmethod
    def get_tile(self) -> TileType:
        pass

    @abstractmethod
    def get_tree_probabilities(self) -> Tuple[float, List[Tuple[Type[Tree], float]]]:
        pass


class PrairieBiome(Biome):
    def get_tile(self) -> TileType:
        return TileType.GRASS
    
    def get_tree_probabilities(self) -> Tuple[float, List[Tuple[Type, float]]]:
        return 0.01, [
            (OakTree, 0.7),
            (SpruceTree, 0.3),
        ]
    

class DesertBiome(Biome):
    def get_tile(self) -> TileType:
        return TileType.SAND
    
    def get_tree_probabilities(self) -> Tuple[float, List[Tuple[Type, float]]]:
        return 0.001, [
            (CactusTree, 1.0)
        ]
    