import pytest

from stuff.accum import Accumulator

@pytest.mark.accumulator
def test_accumulator_init(accum): 
    assert accum.count == 0 

@pytest.mark.accumulator
def test_accumulator_add_one(accum): 
    accum.add()
    assert accum.count == 1

@pytest.mark.accumulator
def test_accumulator_add_three(): 
    accum = Accumulator()
    accum.add(3)
    assert accum.count == 3

@pytest.mark.accumulator
def test_accumulator_add_twice(): 
    accum = Accumulator()
    accum.add()
    accum.add()
    assert accum.count == 2

@pytest.mark.accumulator
def test_accumulator_cannot_set_count_directly(): 
    accum = Accumulator()
    with pytest.raises(AttributeError) as e:
        accum.count = 10         

