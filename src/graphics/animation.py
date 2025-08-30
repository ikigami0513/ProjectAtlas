import pygame
from graphics.texture_atlas import TextureAtlas
from typing import List, Tuple


class Animation:
    def __init__(self, texture_atlas: TextureAtlas, frames: List[str], loop: bool = True, animation_speed: int = 20, scale: float = 1.0):
        self.texture_atlas = texture_atlas
        self.frames = frames
        self.loop = loop
        self.finish = False
        self.animation_speed = animation_speed
        self.scale = scale
        self.frame = 0.0

        self.current_frame = self.texture_atlas.get_sprite(self.frames[int(self.frame)], self.scale)

    def update(self, delta_time: float) -> None:
        self.frame = (self.frame + self.animation_speed * delta_time) % len(self.frames)
        self.current_frame = self.texture_atlas.get_sprite(self.frames[int(self.frame)], self.scale)
