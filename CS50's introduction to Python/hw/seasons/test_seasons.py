from seasons import cal

def main():
    test_1()
    test_2()


def test_1():
    assert cal(1999, 5, 7) == "Twelve million, six hundred ninety-two thousand, one hundred sixty minutes"

def test_2():
    assert cal(23, 1, 20000) == "Invalid Date"
