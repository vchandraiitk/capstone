import subprocess
import os
import shutil

def create_mar():
    os.makedirs("model-store", exist_ok=True)
    if not os.path.exists("pipeline/handler.py"):
        raise FileNotFoundError("Missing handler.py")
    shutil.copy("pipeline/handler.py", "./handler.py")  # required by archiver
    subprocess.run([
        "torch-model-archiver",
        "--model-name", "simple-v1",
        "--version", "1.0",
        "--serialized-file", "model.pt",
        "--handler", "handler.py",
        "--export-path", "model-store"
    ], check=True)
    print("✅ Created .mar file")
