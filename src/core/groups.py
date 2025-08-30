import pygame
from entities.player import Player


class AllSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.offset = pygame.Vector2()

    def draw(self, surface: pygame.Surface, player: Player) -> None:
        self.offset.x = player.rect.centerx - surface.get_width() / 2
        self.offset.y = player.rect.centery - surface.get_height() / 2

        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            surface.blit(sprite.image, offset_pos)
