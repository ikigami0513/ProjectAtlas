import pygame
from entities.player import Player
from world.world import World


class AllSprites(pygame.sprite.Group):
    def __init__(self, world: World):
        super().__init__()
        self.offset = pygame.Vector2()
        self.world = world

    def draw(self, surface: pygame.Surface, player: Player) -> None:
        self.offset.x = player.rect.centerx - surface.get_width() / 2
        self.offset.y = player.rect.centery - surface.get_height() / 2

        self.world.update(player.rect.center)
        self.world.draw(surface, self.offset)
        
        visible_sprites = []

        for sprite in self.sprites():
            chunk_x = int(sprite.rect.centerx // (self.world.chunk_size * self.world.tile_size))
            chunk_y = int(sprite.rect.centery // (self.world.chunk_size * self.world.tile_size))

            if (chunk_x, chunk_y) in self.world.visible_chunks:
                visible_sprites.append(sprite)

        for sprite in sorted(visible_sprites, key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            surface.blit(sprite.image, offset_pos)
