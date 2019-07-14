from Prices import Prices
from unittest.mock import MagicMock
import json
import pytest

def test_openPrices(monkeypatch):


    prices1 = Prices("prices.json")
    
    mock_json_load = MagicMock(return_value = json.loads('{"a": 1, "b": 2, "c": 4}'))
    monkeypatch.setattr("json.load", mock_json_load)




    #print(str(mock_json_load.load()))

    #mock_open = MagicMock(return_value = mock_json)
    #monkeypatch.setattr("builtins.open", mock_open)
    prices2 = Prices("prices.json")

