import sys
import json
import pickle
from graphics.atlas_manager import AtlasManager
from typing import Dict, Any
from pathlib import Path


class Animation:
    def __init__(self, name):
        frozen = hasattr(sys, "_MEIPASS")

        base_dir = Path(getattr(sys, "_MEIPASS", ".")) / "assets" / "animations" if frozen else Path("assets", "animations")
        file_ext = ".bin" if frozen else ".json"
        self.file_path = base_dir / f"{name}{file_ext}"

        if self.file_path.suffix == ".bin":
            with open(self.file_path, "rb") as f:
                self.data: Dict[str, Any] = pickle.load(f)
        else:
            with open(self.file_path, "r", encoding="utf-8") as f:
                self.data: Dict[str, Any] = json.load(f)
        
        self.texture_atlas = AtlasManager().get(self.data.get("atlas"))
        self.frames = self.data.get("frames")
        self.loop = self.data.get("loop", True)
        self.finish = False
        self.animation_speed = self.data.get("speed", 20)
        self.scale = self.data.get("scale", 1.0)
        self.frame = 0.0

        self.current_frame = self.texture_atlas.get_sprite(self.frames[int(self.frame)], self.scale)

    def update(self, delta_time: float) -> None:
        self.frame = (self.frame + self.animation_speed * delta_time) % len(self.frames)
        self.current_frame = self.texture_atlas.get_sprite(self.frames[int(self.frame)], self.scale)
