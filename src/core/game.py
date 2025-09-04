import pygame
from typing import Tuple

from scenes.scene import Scene
from scenes.title_screen_scene import TitleScreenScene
from scenes.game_scene import GameScene

class Game:
    def __init__(self, title: str = "Project Atlas", size: Tuple[int, int] = (800, 600), fps: int = 60):
        pygame.init()
        self.title = title
        self.size = size
        self.fps = fps

        self.display_surface = pygame.display.set_mode(self.size, pygame.RESIZABLE)
        pygame.display.set_caption(self.title)

        self.clock = pygame.time.Clock()
        self.running = True

        # Start with the title screen
        self.scene: Scene = TitleScreenScene(self)

    def change_scene(self, new_scene: Scene) -> None:
        """Switch to a new scene."""
        self.scene = new_scene

    def run(self) -> None:
        while self.running:
            delta_time = self.clock.tick(self.fps) / 1000.0
            events = pygame.event.get()

            self.scene.handle_events(events, delta_time)
            self.scene.update(delta_time)
            self.scene.draw(self.display_surface, delta_time)

            pygame.display.flip()

        pygame.quit()
