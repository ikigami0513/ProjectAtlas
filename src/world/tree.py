import pygame
from graphics.atlas_manager import AtlasManager
from typing import Tuple, List


class Tree(pygame.sprite.Sprite):
    def __init__(self, position: Tuple[int, int], groups: List[pygame.sprite.Group]):
        super().__init__(groups)
        self.atlas_manager = AtlasManager()

class OakTree(Tree):
    def __init__(self, position: Tuple[int, int], groups: List[pygame.sprite.Group]):
        super().__init__(position, groups)
        self.image = self.atlas_manager.get("trees/big_oak").get_sprite("big_oak")
        self.rect = self.image.get_rect(center=position)

class SpruceTree(Tree):
    def __init__(self, position: Tuple[int, int], groups: List[pygame.sprite.Group]):
        super().__init__(position, groups)
        self.image = self.atlas_manager.get("trees/big_spruce").get_sprite("big_spruce")
        self.rect = self.image.get_rect(center=position)


class CactusTree(Tree):
    def __init__(self, position: Tuple[int, int], groups: List[pygame.sprite.Group]):
        super().__init__(position, groups)
        self.image = self.atlas_manager.get("trees/cactus").get_sprite("cactus_1")
        self.rect = self.image.get_rect(center=position)
