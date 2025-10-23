# tests/test_core.py
import pytest
from lotto_game.core import draw_lotto

def test_draw_count_and_range():
    nums = draw_lotto(total_balls=49, pick_count=6)
    assert len(nums) == 6
    assert all(1 <= n <= 49 for n in nums)
    assert nums == sorted(nums)

def test_invalid_pick_count():
    import pytest
    with pytest.raises(ValueError):
        draw_lotto(total_balls=5, pick_count=6)
