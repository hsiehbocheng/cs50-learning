from seasons import cal

def main():
    test_1()
    test_2()


def test_1():
    assert cal(1999, 5, 17) == "Ten million, fifty-eight thousand, four hundred minutes"
    assert cal(2000, 2, 1) == "Eleven million, seven hundred eighty-seven thousand, eight hundred forty minutes"

def test_2():
    assert cal(23, 1, 20000) == "Invalid Date"
