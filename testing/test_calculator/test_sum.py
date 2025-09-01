from calculator.sum import sum


def test_sum():
    assert sum(5, 6) == 11

def test_sum1():
    assert sum(5, 4) == 9

def test_sum2():
    assert sum(5, 1) == 6
