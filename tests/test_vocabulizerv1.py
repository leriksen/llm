from src.vocabulizerv1 import Vocabulizerv1

def test_ctor():
  result = Vocabulizerv1(['here', 'they', 'be'])

  assert result.str_to_int == {
    'here': 0,
    'they': 1,
    'be': 2,
    '<|endoftext|>': 3,
    '<|unk|>': 4,
  }

  assert result.int_to_str == {
    0: 'here',
    1: 'they',
    2: 'be',
    3: '<|endoftext|>',
    4: '<|unk|>',
  }

def test_encode():
  vocab = Vocabulizerv1(['here', 'they', 'be'])

  assert vocab.encode("be they") == [2, 1]

def test_decode():
  vocab = Vocabulizerv1(['here', 'they', 'be'])

  assert vocab.decode([2, 1]) == "be they"

def test_encode_unknown():
  vocab = Vocabulizerv1(['here', 'they', 'be'])

  assert vocab.encode("be they aware") == [2, 1, 4]

def test_decode_unknown():
  vocab = Vocabulizerv1(['here', 'they', 'be'])

  assert vocab.decode([2, 1, 4]) == "be they <|unk|>"

def test_encode_doc_boundaries():
  text1 = "be they"
  text2 = "aware"
  text = " <|endoftext|> ".join((text1, text2))

  vocab = Vocabulizerv1(['here', 'they', 'be'])

  assert vocab.encode(text) == [2, 1, 3, 4]

def test_decode_doc_boundaries():
  vocab = Vocabulizerv1(['here', 'they', 'be'])

  assert vocab.decode([2, 1, 3, 4]) == "be they <|endoftext|> <|unk|>"
