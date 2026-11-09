import pytest
from src.inventory import Inventory


def test_add_stock():
    inventory = Inventory()
    inventory.add_stock("pen", 5)
    assert inventory.stock["pen"] == 5


def test_remove_stock():
    inventory = Inventory()
    inventory.add_stock("pen", 5)
    inventory.remove_stock("pen", 2)
    assert inventory.stock["pen"] == 3


def test_removing_too_much_raises_error():
    inventory = Inventory()
    inventory.add_stock("pen", 2)

    with pytest.raises(ValueError):
        inventory.remove_stock("pen", 3)