import pytest
from task_1_1 import solution,discriminant

def test_solution_neganive_d():
    assert solution(1,1,1) == 'корней нет'

params = (
    (1, 8, 15,(-3.0, -5.0)),
    (1, -13, 12,(12.0, 1.0)),
    (-4, 28, -49,3.5),
)

@pytest.mark.parametrize(
    'x,y,z,expected',
    params
)
def test_with_params(x, y,z, expected):
    assert solution(x, y,z) == expected
