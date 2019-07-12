import pytest
import json
from Prices import Prices

def test_openPrices():
    prices = Prices("section5/prices.json")
