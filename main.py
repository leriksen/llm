from src.get_content import get_content
from src.tokenizerv1 import tokenize_file

import pathlib

url = ("https://raw.githubusercontent.com/rasbt/"
       "LLMs-from-scratch/main/ch02/01_main-chapter-code/"
       "the-verdict.txt")
file_path = pathlib.Path("the-verdict.txt")

get_content(url, file_path)

tokens: list[str] = tokenize_file(file_path)