import pygame
import pygame_gui

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.game import Game


class Scene:
    """Abstract base class for game scenes."""
    def __init__(self, game: "Game"):
        self.game = game
        self.ui_manager = pygame_gui.UIManager(game.size)

    def handle_events(self, events: list[pygame.event.Event], delta_time: float) -> None:
        """Handle Pygame events (keyboard, mouse, etc.)."""
        for event in events:
            self.ui_manager.process_events(event)

    def update(self, delta_time: float) -> None:
        """Update logic."""
        self.ui_manager.update(delta_time)

    def draw(self, surface: pygame.Surface, delta_time: float) -> None:
        """Draw scene content."""
        self.ui_manager.draw_ui(surface)