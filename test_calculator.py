from calculator import Calculator

def test_add():
    calc = Calculator()
    result = calc.add(3, 2)
    assert result == 5

def test_subtract():
    calc = Calculator()
    result = calc.subtract(3, 2)
    assert result == 1

def test_multiply():
    calc = Calculator()
    result = calc.multiply(3, 2)
    assert result == 6

def test_divide():
    calc = Calculator()
    result = calc.divide(6, 3)
    assert result == 2
# You can add similar tests for subtract, multiply and divide
