import os
import json
import pickle
from pathlib import Path
import shutil
import subprocess
import sys

# === Configuration ===
ASSETS_DIR = Path("assets")              # Dossier source contenant JSON et autres fichiers
BUILD_ASSETS_DIR = Path("build_assets")  # Dossier temporaire pour le build
MAIN_SCRIPT = "src/main.py"                  # Script Python principal
EXE_NAME = "ProjectAtlas.exe"                  # Nom du fichier exe final

# ==================== Fonctions ====================

def convert_json_to_bin(src_dir: Path, dst_dir: Path):
    """
    Convert all .json files in src_dir to .bin files in dst_dir.
    """
    for json_file in src_dir.glob("*.json"):
        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        bin_file = dst_dir / f"{json_file.stem}.bin"
        with open(bin_file, "wb") as f:
            pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)
        print(f"[BUILD] Converted {json_file} -> {bin_file}")

def prepare_build_assets():
    """
    Prépare les assets pour le build :
    - Copie tous les fichiers sauf JSON
    - Convertit JSON en BIN
    """
    if BUILD_ASSETS_DIR.exists():
        shutil.rmtree(BUILD_ASSETS_DIR)
    
    # Copie tous les fichiers du dossier assets sauf JSON
    shutil.copytree(ASSETS_DIR, BUILD_ASSETS_DIR, ignore=shutil.ignore_patterns("*.json"))
    
    # Convertit les JSON en BIN
    convert_json_to_bin(ASSETS_DIR, BUILD_ASSETS_DIR)
    
    print("[BUILD] Assets ready in 'build_assets'.")

def run_pyinstaller():
    """
    Lance PyInstaller pour créer l'exécutable
    """
    # Crée la commande PyInstaller
    # --add-data "build_assets;assets" signifie : inclure le dossier build_assets comme 'assets'
    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--noconfirm",
        "--onefile",
        f"--name={EXE_NAME}",
        f"--add-data={BUILD_ASSETS_DIR};assets",
        MAIN_SCRIPT
    ]
    print(f"[BUILD] Running PyInstaller: {' '.join(cmd)}")
    subprocess.run(cmd, check=True)

def clean_build_assets():
    """
    Supprime le dossier temporaire build_assets après le build
    """
    if BUILD_ASSETS_DIR.exists():
        shutil.rmtree(BUILD_ASSETS_DIR)
        print("[BUILD] Cleaned temporary build assets.")

# ==================== Main ====================
if __name__ == "__main__":
    prepare_build_assets()
    run_pyinstaller()
    clean_build_assets()
    print("[BUILD] Build finished successfully.")
