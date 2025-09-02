import noise
from typing import Type
from world.biome import Biome, PrairieBiome, DesertBiome, BeachBiome, OceanBiome


class BiomeManager:
    def __init__(self, seed: int = 0, scale: float = 50.0):
        """
        :param seed: random seed for noise
        :param scale: scale of noise, lower = bigger biomes, higher = smaller biomes
        """
        self.seed = seed
        self.scale = scale

    def get_biome(self, x: int, y: int) -> Biome:
        height = noise.pnoise2(
            x / self.scale,
            y / self.scale,
            octaves=4,
            persistence=0.5,
            lacunarity=2.0,
            repeatx=999999,
            repeaty=999999,
            base=self.seed
        )

        if height < -0.2:
            return OceanBiome(self.seed)
        elif height < -0.1:
            return BeachBiome(self.seed)
        elif height < 0.3:
            return PrairieBiome(self.seed)
        else:
            return DesertBiome(self.seed)
        