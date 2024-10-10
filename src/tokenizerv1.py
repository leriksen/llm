import re
from pathlib import Path

def tokenize_file(path: Path):
  with open(path, 'r', encoding='utf-8') as f:
    return [
      item.strip() for item in  re.split(r'([,.?_!"()\']|--|\s)', f.read()) if item.strip()
    ]

def tokenize_text(text: str =""):
  return [
    item.strip() for item in re.split(r'([,.?_!"()\']|--|\s)', text) if item.strip()
  ]
