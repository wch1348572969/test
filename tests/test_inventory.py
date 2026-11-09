from __future__ import annotations

import unittest

from src.inventory import Inventory, Item


class InventoryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.inventory = Inventory()
        self.inventory.add(Item("A-001", "键盘", 5, 3))
        self.inventory.add(Item("B-002", "鼠标", 2, 4))

    def test_add_duplicate_sku_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            self.inventory.add(Item("A-001", "另一个键盘", 1, 1))

    def test_restock_updates_quantity(self) -> None:
        self.assertEqual(self.inventory.restock("A-001", 4), 9)

    def test_restock_rejects_non_positive(self) -> None:
        with self.assertRaises(ValueError):
            self.inventory.restock("A-001", 0)
        with self.assertRaises(ValueError):
            self.inventory.restock("A-001", -3)

    def test_needs_reorder_returns_sorted_items(self) -> None:
        self.assertEqual([item.sku for item in self.inventory.needs_reorder()], ["B-002"])

    def test_total_units(self) -> None:
        self.assertEqual(self.inventory.total_units(), 7)


if __name__ == "__main__":
    unittest.main()
