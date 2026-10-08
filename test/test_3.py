import pytest
from task_3 import words_count

params = (
    ('fewf wegvv gwge', 3),
    ('123', 1),
    ("wef efgqwe  gwe fqw",4),
)
@pytest.mark.parametrize (
 'x,expected',
    params
)
def test_with_params_len(x,expected):
    assert words_count(x) == expected
