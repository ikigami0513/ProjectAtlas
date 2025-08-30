import pygame
import pygame_gui
from typing import Tuple
from graphics.animation import Animation
from graphics.atlas_manager import AtlasManager
from graphics.animation_manager import AnimationManager
from entities.entity import Entity
from entities.player import Player


class Game:
    def __init__(self, title: str = "Project Atlas", size: Tuple[int, int] = (800, 600), fps: int = 60):
        pygame.init()

        self.title = title
        self.size = size
        self.fps = fps
        self.zoom = 1.0

        self.display_surface = pygame.display.set_mode(self.size)

        self.game_resolution = self.size
        self.game_surface = pygame.Surface(self.game_resolution)

        pygame.display.set_caption(self.title)

        self.clock = pygame.time.Clock()

        self.all_sprites = pygame.sprite.Group()

        self.running = True

        self.ui_manager = pygame_gui.UIManager(self.size)

        self.atlas_manager = AtlasManager()
        self.animation_manager = AnimationManager()
        self.atlas_manager.add("fishes")
        self.atlas_manager.add("cow_1")
        self.atlas_manager.add("player/base")
        self.atlas_manager.add("player/shoes/white")
        self.atlas_manager.add("player/pants/og/blue")
        self.atlas_manager.add("player/chest/og/black")
        self.atlas_manager.add("player/hand/hand")
        self.atlas_manager.add("player/hair/hair_1/grey")

        self.animation_manager.add("player/base/idle/down", Animation(self.atlas_manager.get("player/base"), [f"idle_down_{i}" for i in range(6)]))
        self.animation_manager.add("player/base/idle/right", Animation(self.atlas_manager.get("player/base"), [f"idle_right_{i}" for i in range(6)]))
        self.animation_manager.add("player/base/idle/up", Animation(self.atlas_manager.get("player/base"), [f"idle_up_{i}" for i in range(6)]))

        self.animation_manager.add("player/base/walk/down", Animation(self.atlas_manager.get("player/base"), [f"walk_down_{i}" for i in range(6)]))
        self.animation_manager.add("player/base/walk/right", Animation(self.atlas_manager.get("player/base"), [f"walk_right_{i}" for i in range(6)]))
        self.animation_manager.add("player/base/walk/up", Animation(self.atlas_manager.get("player/base"), [f"walk_up_{i}" for i in range(6)]))

        self.animation_manager.add("player/shoes/white/idle/down", Animation(self.atlas_manager.get("player/shoes/white"), [f"idle_down_{i}" for i in range(6)]))
        self.animation_manager.add("player/shoes/white/idle/right", Animation(self.atlas_manager.get("player/shoes/white"), [f"idle_right_{i}" for i in range(6)]))
        self.animation_manager.add("player/shoes/white/idle/up", Animation(self.atlas_manager.get("player/shoes/white"), [f"idle_up_{i}" for i in range(6)]))

        self.animation_manager.add("player/shoes/white/walk/down", Animation(self.atlas_manager.get("player/shoes/white"), [f"walk_down_{i}" for i in range(6)]))
        self.animation_manager.add("player/shoes/white/walk/right", Animation(self.atlas_manager.get("player/shoes/white"), [f"walk_right_{i}" for i in range(6)]))
        self.animation_manager.add("player/shoes/white/walk/up", Animation(self.atlas_manager.get("player/shoes/white"), [f"walk_up_{i}" for i in range(6)]))

        self.animation_manager.add("player/pants/og/blue/idle/down", Animation(self.atlas_manager.get("player/pants/og/blue"), [f"idle_down_{i}" for i in range(6)]))
        self.animation_manager.add("player/pants/og/blue/idle/right", Animation(self.atlas_manager.get("player/pants/og/blue"), [f"idle_right_{i}" for i in range(6)]))
        self.animation_manager.add("player/pants/og/blue/idle/up", Animation(self.atlas_manager.get("player/pants/og/blue"), [f"idle_up_{i}" for i in range(6)]))

        self.animation_manager.add("player/pants/og/blue/walk/down", Animation(self.atlas_manager.get("player/pants/og/blue"), [f"walk_down_{i}" for i in range(6)]))
        self.animation_manager.add("player/pants/og/blue/walk/right", Animation(self.atlas_manager.get("player/pants/og/blue"), [f"walk_right_{i}" for i in range(6)]))
        self.animation_manager.add("player/pants/og/blue/walk/up", Animation(self.atlas_manager.get("player/pants/og/blue"), [f"walk_up_{i}" for i in range(6)]))

        self.animation_manager.add("player/chest/og/black/idle/down", Animation(self.atlas_manager.get("player/chest/og/black"), [f"idle_down_{i}" for i in range(6)]))
        self.animation_manager.add("player/chest/og/black/idle/right", Animation(self.atlas_manager.get("player/chest/og/black"), [f"idle_right_{i}" for i in range(6)]))
        self.animation_manager.add("player/chest/og/black/idle/up", Animation(self.atlas_manager.get("player/chest/og/black"), [f"idle_up_{i}" for i in range(6)]))

        self.animation_manager.add("player/chest/og/black/walk/down", Animation(self.atlas_manager.get("player/chest/og/black"), [f"walk_down_{i}" for i in range(6)]))
        self.animation_manager.add("player/chest/og/black/walk/right", Animation(self.atlas_manager.get("player/chest/og/black"), [f"walk_right_{i}" for i in range(6)]))
        self.animation_manager.add("player/chest/og/black/walk/up", Animation(self.atlas_manager.get("player/chest/og/black"), [f"walk_up_{i}" for i in range(6)]))

        self.animation_manager.add("player/hand/hand/idle/down", Animation(self.atlas_manager.get("player/hand/hand"), [f"idle_down_{i}" for i in range(6)]))
        self.animation_manager.add("player/hand/hand/idle/right", Animation(self.atlas_manager.get("player/hand/hand"), [f"idle_right_{i}" for i in range(6)]))
        self.animation_manager.add("player/hand/hand/idle/up", Animation(self.atlas_manager.get("player/hand/hand"), [f"idle_up_{i}" for i in range(6)]))

        self.animation_manager.add("player/hand/hand/walk/down", Animation(self.atlas_manager.get("player/hand/hand"), [f"walk_down_{i}" for i in range(6)]))
        self.animation_manager.add("player/hand/hand/walk/right", Animation(self.atlas_manager.get("player/hand/hand"), [f"walk_right_{i}" for i in range(6)]))
        self.animation_manager.add("player/hand/hand/walk/up", Animation(self.atlas_manager.get("player/hand/hand"), [f"walk_up_{i}" for i in range(6)]))

        self.animation_manager.add("player/hair/hair_1/grey/idle/down", Animation(self.atlas_manager.get("player/hair/hair_1/grey"), [f"idle_down_{i}" for i in range(6)]))
        self.animation_manager.add("player/hair/hair_1/grey/idle/right", Animation(self.atlas_manager.get("player/hair/hair_1/grey"), [f"idle_right_{i}" for i in range(6)]))
        self.animation_manager.add("player/hair/hair_1/grey/idle/up", Animation(self.atlas_manager.get("player/hair/hair_1/grey"), [f"idle_up_{i}" for i in range(6)]))

        self.animation_manager.add("player/hair/hair_1/grey/walk/down", Animation(self.atlas_manager.get("player/hair/hair_1/grey"), [f"walk_down_{i}" for i in range(6)]))
        self.animation_manager.add("player/hair/hair_1/grey/walk/right", Animation(self.atlas_manager.get("player/hair/hair_1/grey"), [f"walk_right_{i}" for i in range(6)]))
        self.animation_manager.add("player/hair/hair_1/grey/walk/up", Animation(self.atlas_manager.get("player/hair/hair_1/grey"), [f"walk_up_{i}" for i in range(6)]))

        self.animation_manager.add("cow_1_idle_left", Animation(self.atlas_manager.get("cow_1"), ["idle_left_0", "idle_left_1"]))
        self.animation_manager.add("cow_1_idle_down", Animation(self.atlas_manager.get("cow_1"), ["idle_down_0", "idle_down_1"]))
        self.animation_manager.add("cow_1_idle_up", Animation(self.atlas_manager.get("cow_1"), ["idle_up_0", "idle_up_1"]))

        self.animation_manager.add("cow_1_walk_left", Animation(self.atlas_manager.get("cow_1"), [f"walk_left_{i}" for i in range(8)]))
        self.animation_manager.add("cow_1_walk_down", Animation(self.atlas_manager.get("cow_1"), [f"walk_down_{i}" for i in range(8)]))
        self.animation_manager.add("cow_1_walk_up", Animation(self.atlas_manager.get("cow_1"), [f"walk_up_{i}" for i in range(8)]))

        Entity((200, 200), self.animation_manager.get("cow_1_walk_left"), self.all_sprites)

        self.player = Player((400, 300), self.all_sprites)

    def handle_events(self, delta_time: float) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.VIDEORESIZE:
                self.ui_manager.set_window_resolution(event.size)

            if event.type == pygame.MOUSEWHEEL:
                if event.y > 0:  # Molette vers le haut
                    self.zoom = min(4.0, self.zoom + 0.5)  # Augmente le zoom, limite à 4.0
                elif event.y < 0:  # Molette vers le bas
                    self.zoom = max(1.0, self.zoom - 0.5)  # Diminue le zoom, limite à 0.5

            self.ui_manager.process_events(event)

    def update(self, delta_time: float) -> None:
        self.all_sprites.update(delta_time)
        self.ui_manager.update(delta_time)

    def draw(self) -> None:
        self.game_surface.fill((135, 206, 235))
        self.atlas_manager.get("fishes").render(self.game_surface, "Clownfish", (150, 150))
        self.all_sprites.draw(self.game_surface)

        zoomed_width = int(self.game_resolution[0] * self.zoom)
        zoomed_height = int(self.game_resolution[1] * self.zoom)

        zoomed_game_surface = pygame.transform.scale(self.game_surface, (zoomed_width, zoomed_height))

        # Centrer la surface zoomée sur l'écran
        rect = zoomed_game_surface.get_rect(center=self.display_surface.get_rect().center)

        self.display_surface.fill((0, 0, 0))
        self.display_surface.blit(zoomed_game_surface, rect)

        self.ui_manager.draw_ui(self.display_surface)
        pygame.display.flip()

    def run(self) -> None:
        while self.running:
            delta_time = self.clock.tick(self.fps) / 1000.0
            self.handle_events(delta_time)
            self.update(delta_time)
            self.draw()
            self.clock.tick(self.fps)

        pygame.quit()
