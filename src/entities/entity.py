import pygame
from graphics.animation import Animation
from typing import List, Tuple
from copy import deepcopy

class Entity(pygame.sprite.Sprite):
    def __init__(self, position: Tuple[float, float], animation: Animation, groups: List[pygame.sprite.Group]):
        super().__init__(groups)
        self.animation = deepcopy(animation)
        self.image = self.animation.current_frame
        self.rect = self.image.get_frect(center=position)

    def update(self, delta_time: float) -> None:
        self.animation.update(delta_time)
        self.image = self.animation.current_frame
