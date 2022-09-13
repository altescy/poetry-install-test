import numpy


def test_numpy() -> None:
    x = numpy.arange(10)
    assert len(x) == 10
    assert x[0] == 0
    assert x[-1] == 9
