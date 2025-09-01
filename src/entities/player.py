import pygame
from enum import Enum
from entities.entity import Entity
from graphics.animation_manager import AnimationManager
from graphics.animation import Animation
from typing import Tuple, List


class Direction(Enum):
    DOWN = "down"
    UP = "up"
    LEFT = "left"
    RIGHT = "right"


class State(Enum):
    IDLE = "idle"
    WALK = "walk"


class Player(Entity):
    def __init__(self, position: Tuple[float, float], groups: List[pygame.Surface]):
        self.animation_manager = AnimationManager()
        self.direction = Direction.LEFT
        self.state = State.IDLE
        self.speed = 200
        self.is_running = False
        self.velocity = pygame.Vector2()

        super().__init__(position, self.animation_manager.get(f"player/base/{self.state.value}/{self.get_animation_direction().value}"), groups)
        self.shoes = self.animation_manager.get(f"player/shoes/white/{self.state.value}/{self.get_animation_direction().value}")
        self.pants = self.animation_manager.get(f"player/pants/og/blue/{self.state.value}/{self.get_animation_direction().value}")
        self.chest = self.animation_manager.get(f"player/chest/og/black/{self.state.value}/{self.get_animation_direction().value}")
        self.hand = self.animation_manager.get(f"player/hand/hand/{self.state.value}/{self.get_animation_direction().value}")
        self.hair = self.animation_manager.get(f"player/hair/hair_1/grey/{self.state.value}/{self.get_animation_direction().value}")

        self.parts: List[Animation] = [
            self.animation,  # Base
            self.shoes,
            self.pants,
            self.chest,
            self.hand,
            self.hair
        ]

    def get_animation_direction(self) -> Direction:
        if self.direction == Direction.LEFT:
            return Direction.RIGHT
        return self.direction

    def update(self, delta_time: float) -> None:
        self.input()

        if self.velocity.magnitude() > 0:
            self.state = State.WALK
        else:
            self.state = State.IDLE

        self.set_animation()

        speed = self.speed
        if self.is_running:
            speed *= 2
        self.rect.x += self.velocity.x * speed * delta_time
        self.rect.y += self.velocity.y * speed * delta_time

        for animation in self.parts:
            animation.update(delta_time)

        self.image = self.get_image()

    def input(self) -> None:
        keys = pygame.key.get_pressed()
        self.velocity.x = 0
        self.velocity.y = 0

        if keys[pygame.K_z]:
            self.velocity.y = -1
            self.direction = Direction.UP
        elif keys[pygame.K_s]:
            self.velocity.y = 1
            self.direction = Direction.DOWN

        if keys[pygame.K_q]:
            self.velocity.x = -1
            self.direction = Direction.LEFT
        elif keys[pygame.K_d]:
            self.velocity.x = 1
            self.direction = Direction.RIGHT

        self.is_running = keys[pygame.K_LSHIFT] == True

        if self.velocity.magnitude() > 0:
            self.velocity.normalize_ip()

    def get_image(self) -> pygame.Surface:
        base_image = self.animation.current_frame.copy()
        base_image.blit(self.shoes.current_frame.copy(), (0, 0))
        base_image.blit(self.pants.current_frame.copy(), (0, 0))
        base_image.blit(self.chest.current_frame.copy(), (0, 0))
        base_image.blit(self.hand.current_frame.copy(), (0, 0))
        base_image.blit(self.hair.current_frame.copy(), (0, 0))

        if self.direction == Direction.LEFT:
            base_image = pygame.transform.flip(base_image, True, False)

        return base_image
    
    def set_animation(self) -> None:
        self.animation = self.animation_manager.get(f"player/base/{self.state.value}/{self.get_animation_direction().value}")
        self.shoes = self.animation_manager.get(f"player/shoes/white/{self.state.value}/{self.get_animation_direction().value}")
        self.pants = self.animation_manager.get(f"player/pants/og/blue/{self.state.value}/{self.get_animation_direction().value}")
        self.chest = self.animation_manager.get(f"player/chest/og/black/{self.state.value}/{self.get_animation_direction().value}")
        self.hand = self.animation_manager.get(f"player/hand/hand/{self.state.value}/{self.get_animation_direction().value}")
        self.hair = self.animation_manager.get(f"player/hair/hair_1/grey/{self.state.value}/{self.get_animation_direction().value}")

        self.parts = [
            self.animation, 
            self.shoes,
            self.pants,
            self.chest,
            self.hand,
            self.hair
        ]
