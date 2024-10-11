def encode(tokens: list[str]) -> dict[int, str]:
  return {token:integer for integer,token in enumerate(tokens)}
