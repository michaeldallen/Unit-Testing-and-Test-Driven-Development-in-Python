import pytest
from Checkout import Checkout

@pytest.fixture()
def checkout():
    checkout = Checkout()
    return checkout


def test_CannAddItemPrice(checkout):
    checkout.addItemPrice("a", 1)


def test_CanAddItem(checkout):
    checkout.addItem("a")
