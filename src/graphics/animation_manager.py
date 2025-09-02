from graphics.animation import Animation
from core.singleton import SingletonMeta
from typing import Dict, Any


class AnimationManager(metaclass=SingletonMeta):
    def __init__(self):
        self._animations: Dict[str, Animation] = {}

    def add(self, name: str) -> Animation:
        self._animations[name] = Animation(name)
        return self._animations[name]
    
    def get(self, name: str, default: Any = None) -> Animation:
        return self._animations.get(name, default)
    