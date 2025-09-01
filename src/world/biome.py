from abc import ABC, abstractmethod
from world.tile import TileType


class Biome(ABC):
    @abstractmethod
    def get_tile(self) -> TileType:
        pass


class PrairieBiome(Biome):
    def get_tile(self) -> TileType:
        return TileType.GRASS
    

class DesertBiome(Biome):
    def get_tile(self) -> TileType:
        return TileType.SAND
    