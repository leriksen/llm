from unittest.mock import patch, mock_open, Mock

from pathlib import Path

from src.get_content import get_content

# noinspection PyArgumentList
@patch('src.get_content.requests.get', return_value=Mock(text='content'))
def test_get_data(mock_get):
  path = Path('here')

  with patch('src.get_content.open', mock_open()) as mocked_file:
    get_content('https://google.com', path)

    mocked_file.assert_called_once_with(path, 'w', encoding='utf-8')
    mocked_file().write.assert_called_once_with('content')
    mock_get.assert_called_once_with('https://google.com')
