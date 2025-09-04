import json
import pygame
import pygame_gui
from typing import Tuple, List, Dict, Optional, TYPE_CHECKING

from graphics.atlas_manager import AtlasManager
from graphics.animation_manager import AnimationManager
from entities.entity import Entity
from entities.player import Player
from core.groups import AllSprites
from world.world import World
from world.tile import TileAtlas

from scenes.scene import Scene

if TYPE_CHECKING:
    from core.game import Game


class GameScene(Scene):
    def __init__(self, game: "Game"):
        super().__init__(game)

        # Game-related attributes
        self.zoom = 1.0
        self.game_resolution = (800, 600)
        self.game_surface = pygame.Surface(self.game_resolution)

        # Load assets
        self.atlas_manager = AtlasManager()
        self.animation_manager = AnimationManager()

        with open("assets/assets.json", "r") as f:
            data: Dict[str, List[str]] = json.load(f)

            for atlas in data.get("atlases"):
                self.atlas_manager.add(atlas)

            for animation in data.get("animations"):
                self.animation_manager.add(animation)

        self.tile_atlas = TileAtlas()
        self.tile_atlas.initialize(self.atlas_manager, self.animation_manager)

        self.all_sprites = AllSprites()
        self.world = World(self.all_sprites)

        Entity((200, 200), self.animation_manager.get("animal/cow_1/idle/left"), self.all_sprites)
        self.player = Player((400, 300), self.all_sprites)

    def handle_events(self, events: list[pygame.event.Event], delta_time: float) -> None:
        super().handle_events(events, delta_time)

        for event in events:
            if event.type == pygame.QUIT:
                self.game.running = False

            if event.type == pygame.VIDEORESIZE:
                self.game.display_surface = pygame.display.set_mode(event.size, pygame.RESIZABLE)
                self.game.size = event.size
                self.ui_manager.set_window_resolution(event.size)

            if event.type == pygame.MOUSEWHEEL:
                if event.y > 0:
                    self.zoom = min(4.0, self.zoom + 0.5)
                elif event.y < 0:
                    self.zoom = max(1.0, self.zoom - 0.5)

    def update(self, delta_time: float) -> None:
        pygame.display.set_caption(f"Project Atlas - {round(self.game.clock.get_fps(), 2)}")
        self.all_sprites.update(delta_time)
        super().update(delta_time)

    def draw(self, surface: pygame.Surface, delta_time: float) -> None:
        self.game_surface.fill((135, 206, 235))
        self.all_sprites.draw(self.world, self.game_surface, self.player, delta_time)

        aspect_ratio = self.game_resolution[0] / self.game_resolution[1]
        current_width, current_height = surface.get_size()

        if current_width / current_height > aspect_ratio:
            new_height = current_height
            new_width = int(new_height * aspect_ratio)
        else:
            new_width = current_width
            new_height = int(new_width / aspect_ratio)

        zoomed_width = int(new_width * self.zoom)
        zoomed_height = int(new_height * self.zoom)

        zoomed_game_surface = pygame.transform.scale(self.game_surface, (zoomed_width, zoomed_height))
        rect = zoomed_game_surface.get_rect(center=surface.get_rect().center)

        surface.fill((0, 0, 0))
        surface.blit(zoomed_game_surface, rect)

        super().draw(surface, delta_time)