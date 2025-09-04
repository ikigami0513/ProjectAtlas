import pygame
import pygame_gui
from scenes.scene import Scene
from scenes.game_scene import GameScene
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.game import Game

class TitleScreenScene(Scene):
    def __init__(self, game: "Game"):
        super().__init__(game)

        # Centered "Play" button
        self.start_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((game.size[0]//2 - 100, game.size[1]//2 - 25), (200, 50)),
            text="Jouer",
            manager=self.ui_manager
        )

    def handle_events(self, events: list[pygame.event.Event], delta_time: float) -> None:
        super().handle_events(events, delta_time)

        for event in events:
            if event.type == pygame.QUIT:
                self.game.running = False

            if event.type == pygame.USEREVENT and event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.start_button:
                    # Switch to the game scene
                    self.game.change_scene(GameScene(self.game))

    def draw(self, surface: pygame.Surface, delta_time: float) -> None:
        surface.fill((0, 0, 0))  # Black background
        # Optionally: draw a title text
        font = pygame.font.SysFont("Arial", 48, bold=True)
        text_surface = font.render("Project Atlas", True, (255, 255, 255))
        surface.blit(text_surface, (self.game.size[0] // 2 - text_surface.get_width() // 2, 150))

        super().draw(surface, delta_time)