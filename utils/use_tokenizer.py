from pathlib import Path

from src.tokenizerv1 import tokenize_file

tokens: list[str] = tokenize_file(Path('./the-verdict.txt'))

print( tokens)

