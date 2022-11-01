import Lab2 as Lab2


def test_calc_average():
    sample = [1, 8, 3, 47, 3, 2, 8, 2, 123, 24]
    expected = 22.1

    result = Lab2.calc_average_temperature(sample)

    assert (expected == result)
