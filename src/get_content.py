import requests

from pathlib import Path

def get_content(url: str, save_path: Path):
  response = requests.get(url)
  with open(save_path, "w") as f:
    f.write(response.text)
