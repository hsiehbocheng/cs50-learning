from jar import Jar

def test_init():
    x = Jar()
    assert x.capacity == 12
    assert x.size == 0

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(4)
    assert str(jar) == "🍪"
