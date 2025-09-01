import noise
import random
from core.groups import AllSprites
from world.tree import Tree
from world.biome import Biome
from typing import Optional


class TreeGenerator:
    def __init__(self, all_sprites: AllSprites, seed: int, scale: float = 30.0):
        self.all_sprites = all_sprites
        self.seed = seed
        self.scale = scale

    def generate_tree(self, x: int, y: int, biome: Biome) -> Optional[Tree]:
        tree_density, tree_probs = biome.get_tree_probabilities()

        if tree_density <= 0.0:
            return None

        # Valeur de bruit → influence la densité locale
        noise_value = noise.pnoise2(
            x / self.scale,
            y / self.scale,
            base=self.seed
        )
        noise_value = (noise_value + 1) / 2  # [0,1]

        local_density = noise_value * tree_density

        # Tirage pseudo-aléatoire mais déterministe (en fonction de seed + coord)
        rng = random.Random(hash((x, y, self.seed)))
        if rng.random() > local_density:
            return None

        # Sélectionner l’arbre selon les poids
        total_weight = sum(weight for _, weight in tree_probs)
        threshold = rng.random() * total_weight
        cumulative = 0
        for tree_class, weight in tree_probs:
            cumulative += weight
            if threshold <= cumulative:
                return tree_class((x, y), [self.all_sprites])
    