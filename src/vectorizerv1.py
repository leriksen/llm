from typing import Dict


def encode(tokens: list[str]) -> dict[str, int]:
  return {token:integer for integer,token in enumerate(tokens)}
