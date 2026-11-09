"""训练场：一个小型库存领域模型。

这个模块故意保留了一个可复现的 bug，供 DSH 训练使用：
`restock` 目前接受零或负数，导致可以通过“补货”减少库存。
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Item:
    """库存条目。"""

    sku: str
    name: str
    quantity: int
    reorder_level: int


class Inventory:
    """内存库存表。"""

    def __init__(self) -> None:
        self._items: Dict[str, Item] = {}

    def add(self, item: Item) -> None:
        """加入一个新条目；SKU 必须唯一，数量不能为负。"""
        if item.sku in self._items:
            raise ValueError(f"duplicate sku: {item.sku}")
        if item.quantity < 0 or item.reorder_level < 0:
            raise ValueError("quantity and reorder_level must be non-negative")
        self._items[item.sku] = item

    def get(self, sku: str) -> Item:
        """按 SKU 取条目；不存在时抛出 KeyError。"""
        try:
            return self._items[sku]
        except KeyError as exc:
            raise KeyError(f"unknown sku: {sku}") from exc

    def restock(self, sku: str, amount: int) -> int:
        """补货并返回新的数量。

        预期：amount 必须是正整数；零或负数应抛出 ValueError。
        当前实现：直接累加，接受任意整数。
        """
        item = self.get(sku)
        item.quantity += amount
        return item.quantity

    def needs_reorder(self) -> List[Item]:
        """返回所有需要补货的条目，按 SKU 排序。"""
        return sorted(
            (item for item in self._items.values() if item.quantity <= item.reorder_level),
            key=lambda item: item.sku,
        )

    def total_units(self) -> int:
        """返回所有条目的数量总和。"""
        return sum(item.quantity for item in self._items.values())
