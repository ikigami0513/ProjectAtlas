import pygame
from entities.entity import Entity
from graphics.animation_manager import AnimationManager
from graphics.animation import Animation
from typing import Tuple, List


class Player(Entity):
    def __init__(self, position: Tuple[float, float], groups: List[pygame.Surface]):
        self.animation_manager = AnimationManager()
        super().__init__(position, self.animation_manager.get("player/base/idle/down"), groups)
        self.shoes = self.animation_manager.get("player/shoes/white/idle/down")
        self.pants = self.animation_manager.get("player/pants/og/blue/idle/down")
        self.chest = self.animation_manager.get("player/chest/og/black/idle/down")
        self.hand = self.animation_manager.get("player/hand/hand/idle/down")
        self.hair = self.animation_manager.get("player/hair/hair_1/grey/idle/down")

        self.parts: List[Animation] = [
            self.animation,  # Base
            self.shoes,
            self.pants,
            self.chest,
            self.hand,
            self.hair
        ]

    def update(self, delta_time: float) -> None:
        self.input()

        for animation in self.parts:
            animation.update(delta_time)

        self.image = self.get_image()

    def input(self) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_z]:
            print("up")
        elif keys[pygame.K_s]:
            print("down")

        if keys[pygame.K_q]:
            print("left")
        elif keys[pygame.K_d]:
            print("right")

    def get_image(self) -> pygame.Surface:
        base_image = self.animation.current_frame.copy()
        base_image.blit(self.shoes.current_frame.copy(), (0, 0))
        base_image.blit(self.pants.current_frame.copy(), (0, 0))
        base_image.blit(self.chest.current_frame.copy(), (0, 0))
        base_image.blit(self.hand.current_frame.copy(), (0, 0))
        base_image.blit(self.hair.current_frame.copy(), (0, 0))

        return base_image
