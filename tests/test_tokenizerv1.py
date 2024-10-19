from unittest.mock import patch, mock_open

from pathlib import Path

from src.tokenizerv1 import tokenize_text, tokenize_file

def test_tokenize_text():
  assert tokenize_text() == []
  assert tokenize_text("") == []
  assert tokenize_text("here there") == ["here", "there"]

def test_tokenize_file():
  path = Path('here')

  with patch('src.tokenizerv1.open'.format(__name__), new=mock_open(read_data='ooo')) as mocked_file:
    tokenize_file(path)

    mocked_file.assert_called_once_with(path, 'r', encoding='utf-8')
    # mocked_file().read.assert_called_once_with('content')
    # mock_get.assert_called_once_with('https://google.com')
