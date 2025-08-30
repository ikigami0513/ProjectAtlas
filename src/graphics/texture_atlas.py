import os
import sys
import json
import pickle
import pygame
from pathlib import Path
from typing import Dict, Any, Tuple


class TextureAtlas:
    def __init__(self, name: str):
        frozen = hasattr(sys, "_MEIPASS")

        base_dir = Path(getattr(sys, "_MEIPASS", ".")) / "assets" / "textures_atlas" if frozen else Path("assets", "textures_atlas")
        file_ext = ".bin" if frozen else ".json"
        self.file_path = base_dir / f"{name}{file_ext}"

        if self.file_path.suffix == ".bin":
            with open(self.file_path, "rb") as f:
                self.data: Dict[str, Any] = pickle.load(f)
        else:
            with open(self.file_path, "r", encoding="utf-8") as f:
                self.data: Dict[str, Any] = json.load(f)

        self.texture_path = base_dir / self.data.get("texture")
        self.texture = pygame.image.load(str(self.texture_path)).convert_alpha()
        self.sprites = {s["name"]: s for s in self.data.get("sprites", [])}

    def get_sprite(self, sprite_name, scale: float = 1.0) -> pygame.Surface:
        sprite = self.sprites.get(sprite_name)
        if not sprite:
            raise ValueError(f"Sprite '{sprite_name}' not found in atlas.")
        
        x, y = sprite["position"]
        w, h = sprite["size"]

        sub_surface = self.texture.subsurface(pygame.Rect(x, y, w, h))

        if scale != 1.0:
            new_size = (int(w * scale), int(h * scale))
            sub_surface = pygame.transform.scale(sub_surface, new_size)

        return sub_surface

    def render(self, surface: pygame.Surface, sprite_name: str, position: Tuple[int, int], scale: float = 1.0) -> None:
        sprite = self.sprites.get(sprite_name)
        if not sprite:
            raise ValueError(f"Sprite '{sprite_name}' not found in atlas.")
        
        x, y = sprite["position"]
        w, h = sprite["size"]

        sub_surface = self.texture.subsurface(pygame.Rect(x, y, w, h))

        if scale != 1.0:
            new_size = (int(w * scale), int(h * scale))
            sub_surface = pygame.transform.scale(sub_surface, new_size)

        surface.blit(sub_surface, position)
