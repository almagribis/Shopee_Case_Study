import sqlite3
from typing import Dict, Any, List
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DB_PATH = BASE_DIR / "data" / "food_receipts.db"


def get_db_path() -> Path:
    return DB_PATH


def get_connection() -> sqlite3.Connection:
    return sqlite3.connect(DB_PATH)

def to_int_or_none(value: Any):
    """
    Convert string like "34500" or "" to int / None.
    """
    if value is None:
        return None
    if isinstance(value, (int, float)):
        return int(value)
    value = str(value).strip()
    if not value:
        return None
    value = value.replace(",", "").replace(".", "")
    if value.isdigit():
        return int(value)
    return None

def insert_receipt(data: Dict[str, Any], db_path: str):
    """
    data: dict JSON hasil ekstraksi, format:
    {
      "order_id": "...",
      "order_time": "2025-09-22T13:35:00",
      "payment_method": "ovo",
      "merchant_name": "...",
      "platform": "grabfood",
      "total_initial_price": "34500",
      "total_discount": "6000",
      "total_paid": "28500",
      "items": [
        {"item_name": "...", "item_qty": "1"}
      ]
    }
    """
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    order_id = data.get("order_id", "")

    cur.execute("""
        INSERT INTO orders (
            order_id,
            order_time,
            payment_method,
            merchant_name,
            platform,
            total_initial_price,
            total_discount,
            total_paid
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        order_id or "",
        data.get("order_time", "") or "",
        data.get("payment_method", "") or "",
        data.get("merchant_name", "") or "",
        data.get("platform", "") or "",
        to_int_or_none(data.get("total_initial_price")),
        to_int_or_none(data.get("total_discount")),
        to_int_or_none(data.get("total_paid"))
    ))

    items: List[Dict[str, Any]] = data.get("items", []) or []
    for item in items:
        item_name = (item.get("item_name") or "").strip()
        item_qty_raw = item.get("item_qty", "1")
        try:
            item_qty = int(str(item_qty_raw).strip() or "1")
        except ValueError:
            item_qty = 1

        if not item_name:
            continue

        cur.execute("""
            INSERT INTO order_items (
                order_id,
                item_name,
                item_qty
            )
            VALUES (?, ?, ?)
        """, (
            order_id or "",
            item_name,
            item_qty
        ))

    conn.commit()
    conn.close()