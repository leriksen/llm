from src.vocabulizerv1 import Vocabulizerv1

def test_ctor():
  result = Vocabulizerv1(['here', 'they', 'be'])

  assert result.str_to_int == {
    'here': 0,
    'they': 1,
    'be': 2,
  }

  assert result.int_to_str == {
    0: 'here',
    1: 'they',
    2: 'be',
  }

def test_encode():
  vocab = Vocabulizerv1(['here', 'they', 'be'])

  assert vocab.encode("be they") == [2, 1]

def test_decode():
  vocab = Vocabulizerv1(['here', 'they', 'be'])

  assert vocab.decode([2, 1]) == "be they"