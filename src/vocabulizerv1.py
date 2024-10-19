from typing import Dict, List

import re
from src.tokenizerv1 import tokenize_text

class Vocabulizerv1:
  def __init__(self, vocab: list[str]):
    self.str_to_int = {}
    self.int_to_str = {}

    # symbols to handle document boundries, and text not found in training set
    vocab.extend(["<|endoftext|>", "<|unk|>"])

    for integer, token in enumerate(vocab):
      self.str_to_int[token] = integer
      self.int_to_str[integer] = token

  def encode(self, text: str) -> list[int]:
    tokens = tokenize_text(text)

    return [self.str_to_int[s] if s in self.str_to_int else self.str_to_int["<|unk|>"] for s in tokens]

  def decode(self, ids: list[int]) -> str:
    text = " ".join([self.int_to_str[id] for id in ids])

    # text will have spaces before punctuations, strip these
    return re.sub(r'\s+([,.:;?!"()\'])', r'\1', text)