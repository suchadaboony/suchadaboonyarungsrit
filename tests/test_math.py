import pytest

@pytest.mark.math
def test_one_plus_one(): 
    assert 1+1 == 2 

@pytest.mark.math
def test_one_plus_two(): 
    a = 1 
    b = 2 
    c = 3
    assert a + b == c

@pytest.mark.math
def test_devide_by_zero(): 

    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0

    assert 'division by zero' in str(e.value)


products = [
    (2,3,6),
    (1,99,99),
    (0,99,0)
]

@pytest.mark.math
@pytest.mark.parametrize('a,b,product', products)
def test_multiplication(a,b, product): 
    assert a * b == product

