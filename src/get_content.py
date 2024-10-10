import requests

from pathlib import Path

def get_content(url: str, save_path: Path):
  response = requests.get(url)
  with open(save_path, 'w', encoding='utf-8') as f:
    f.write(response.text)
