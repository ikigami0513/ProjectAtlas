import noise
from typing import Type
from world.biome import Biome, PrairieBiome, DesertBiome


class BiomeManager:
    def __init__(self, seed: int = 0, scale: float = 50.0):
        """
        :param seed: random seed for noise
        :param scale: scale of noise, lower = bigger biomes, higher = smaller biomes
        """
        self.seed = seed
        self.scale = scale

    def get_biome(self, x: int, y: int) -> Biome:
        noise_value = noise.pnoise2(
            x / self.scale,
            y / self.scale,
            octaves=2,
            persistence=0.5,
            lacunarity=2.0,
            repeatx=999999,
            repeaty=999999,
            base=self.seed
        )

        if noise_value < 0:
            return DesertBiome()
        else:
            return PrairieBiome()
        