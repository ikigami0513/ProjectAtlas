import noise
from typing import Type
from world.biome import Biome, PrairieBiome, DesertBiome, BeachBiome, OceanBiome

class BiomeManager:
    def __init__(self, seed: int = 0, scale: float = 50.0, continent_scale: float = 1000.0, continent_seed: int = 1):
        """
        :param seed: graine aléatoire pour le bruit de Perlin des biomes
        :param scale: échelle du bruit de Perlin pour les biomes (plus petit = biomes plus grands)
        :param continent_scale: échelle du bruit de Perlin pour les continents et océans (beaucoup plus grand = continents plus grands)
        :param continent_seed: graine aléatoire pour le bruit de Perlin des continents
        """
        self.seed = seed
        self.scale = scale
        self.continent_scale = continent_scale
        self.continent_seed = continent_seed

    def get_biome(self, x: int, y: int) -> Biome:
        # Bruit de Perlin pour la génération des continents
        continent_value = noise.pnoise2(
            x / self.continent_scale,
            y / self.continent_scale,
            octaves=4,
            persistence=0.5,
            lacunarity=2.0,
            repeatx=999999,
            repeaty=999999,
            base=self.continent_seed
        )

        # Bruit de Perlin pour la génération des biomes terrestres
        biome_value = noise.pnoise2(
            x / self.scale,
            y / self.scale,
            octaves=4,
            persistence=0.5,
            lacunarity=2.0,
            repeatx=999999,
            repeaty=999999,
            base=self.seed
        )

        # Logique pour déterminer le biome
        if continent_value < -0.2:
            return OceanBiome(self.seed)
        elif continent_value < -0.1:
            return BeachBiome(self.seed)
        else: # On est sur la terre, on utilise la valeur des biomes
            if biome_value < 0.3:
                return PrairieBiome(self.seed)
            else:
                return DesertBiome(self.seed)