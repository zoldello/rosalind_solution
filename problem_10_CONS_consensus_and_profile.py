import pytest
import problem_10_CONS_consensus_and_profile as sut


@pytest.mark.parametrize('n, k, expected',[
(5, 3, 15),
(0, 2, 2),
(0, 3, 3),
(7, 0, 0),
])
def test_fibonacci(n, k, expected):
    target = sut.fibonacci(n, k)
    assert target == expected


@pytest.mark.parametrize('n, k, exception',[
    ('1', 1, TypeError),
    (1, '2', TypeError),
    ('3', '1', TypeError),
    (-1, 1, ValueError),
    (-3, 2, ValueError),
    (-5, -6, ValueError),
])
def test_fibonacci_exception_raising(n, k, exception):
    with pytest.raises(exception):
        sut.fibonacci(n, k)
