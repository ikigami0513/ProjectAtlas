import json
import pygame
import pygame_gui
from typing import Tuple, List, Dict
from graphics.animation import Animation
from graphics.atlas_manager import AtlasManager
from graphics.animation_manager import AnimationManager
from entities.entity import Entity
from entities.player import Player
from core.groups import AllSprites
from world.world import World
from world.tile import TileAtlas


class Game:
    def __init__(self, title: str = "Project Atlas", size: Tuple[int, int] = (800, 600), fps: int = 60):
        pygame.init()

        self.title = title
        self.size = size
        self.fps = fps
        self.zoom = 1.0

        self.display_surface = pygame.display.set_mode(self.size, pygame.RESIZABLE)

        # Use a fixed internal resolution for your game world
        self.game_resolution = (800, 600)  # Fixed resolution
        self.game_surface = pygame.Surface(self.game_resolution)

        pygame.display.set_caption(self.title)

        self.clock = pygame.time.Clock()

        self.running = True

        self.ui_manager = pygame_gui.UIManager(self.size)

        self.atlas_manager = AtlasManager()
        self.animation_manager = AnimationManager()

        with open("assets/assets.json", "r") as f:
            data: Dict[str, List[str]] = json.load(f)

            for atlas in data.get("atlases"):
                self.atlas_manager.add(atlas)

            for animation in data.get("animations"):
                self.animation_manager.add(animation)

        self.tile_atlas = TileAtlas()
        self.tile_atlas.initialize(self.atlas_manager)
        self.all_sprites = AllSprites()
        self.world = World(self.all_sprites)

        Entity((200, 200), self.animation_manager.get("animal/cow_1/idle/left"), self.all_sprites)

        self.player = Player((400, 300), self.all_sprites)

    def handle_events(self, delta_time: float) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.VIDEORESIZE:
                self.display_surface = pygame.display.set_mode(event.size, pygame.RESIZABLE)
                self.size = event.size
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
        # self.atlas_manager.get("fishes").render(self.game_surface, "Clownfish", (150, 150))
        self.all_sprites.draw(self.world, self.game_surface, self.player)

        # Calculate the aspect ratio to avoid stretching
        aspect_ratio = self.game_resolution[0] / self.game_resolution[1]
        current_width, current_height = self.display_surface.get_size()
        
        # Calculate new dimensions while preserving aspect ratio
        if current_width / current_height > aspect_ratio:
            new_height = current_height
            new_width = int(new_height * aspect_ratio)
        else:
            new_width = current_width
            new_height = int(new_width / aspect_ratio)

        # Apply zoom to the new dimensions
        zoomed_width = int(new_width * self.zoom)
        zoomed_height = int(new_height * self.zoom)

        # Scale the game surface
        zoomed_game_surface = pygame.transform.scale(self.game_surface, (zoomed_width, zoomed_height))

        # Center the zoomed surface
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
        