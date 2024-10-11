from src.vectorizerv1 import encode

def test_encode():
  result = encode(['here', 'they', 'be'])

  assert result == {
    'here': 0,
    'they': 1,
    'be': 2
  }