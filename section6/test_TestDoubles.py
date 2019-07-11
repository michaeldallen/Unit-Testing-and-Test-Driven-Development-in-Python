import pytest
from unittest.mock import MagicMock

from LineReader import readFromFile

    
def test_returnsCorrectString(monkeypatch):
    mock_file = MagicMock()
    mock_file.readline = MagicMock(return_value="bar")
    mock_open = MagicMock(return_value=mock_file)
    monkeypatch.setattr("builtins.open", mock_open)
    result = readFromFile("foo")
    mock_open.assert_called_once_with("foo", "r")
    assert result == "bar"

    
