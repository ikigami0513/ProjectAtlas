import pygame
from entities.player import Player
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from world.world import World


class AllSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.offset = pygame.Vector2()

    def draw(self, world: 'World', surface: pygame.Surface, player: Player) -> None:
        self.offset.x = player.rect.centerx - surface.get_width() / 2
        self.offset.y = player.rect.centery - surface.get_height() / 2

        world.update(player.rect.center)
        world.draw(surface, self.offset)
        
        visible_sprites = []

        for sprite in self.sprites():
            chunk_x = int(sprite.rect.centerx // (world.chunk_size * world.tile_size))
            chunk_y = int(sprite.rect.centery // (world.chunk_size * world.tile_size))

            if (chunk_x, chunk_y) in world.visible_chunks:
                visible_sprites.append(sprite)

        for sprite in sorted(visible_sprites, key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            surface.blit(sprite.image, offset_pos)
