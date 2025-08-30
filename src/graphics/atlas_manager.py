from core.singleton import SingletonMeta
from graphics.texture_atlas import TextureAtlas
from typing import Dict, Any


class AtlasManager(metaclass=SingletonMeta):
    def __init__(self):
        self._atlases: Dict[str, TextureAtlas] = {}

    def add(self, name: str) -> TextureAtlas:
        self._atlases[name] = TextureAtlas(name)
        return self._atlases[name]
    
    def get(self, name: str, default: Any = None) -> TextureAtlas:
        return self._atlases.get(name, default)
    