# src/lotto_game/core.py
import random
import json
from typing import List

def draw_lotto(total_balls: int = 49, pick_count: int = 6) -> List[int]:
    """Return sorted list of unique drawn numbers."""
    if pick_count > total_balls or pick_count <= 0:
        raise ValueError("Invalid pick_count")
    nums = random.sample(range(1, total_balls + 1), pick_count)
    return sorted(nums)

def save_history(path: str, history: List[List[int]]):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(history, f)

def load_history(path: str) -> List[List[int]]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
