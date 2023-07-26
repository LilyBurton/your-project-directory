from lib.counter import *
def test_counting():
    counter = Counter()
    assert counter.report() == "Counted to 0 so far."

def test_counting_with_a_number():
    counter = Counter()
    counter.add(13)
    result = counter.report()
    assert result == "Counted to 13 so far."

def test_counting_with_multiple_numbers():
    counter = Counter()
    counter.add(5)
    counter.add(3)
    assert counter.report() == "Counted to 8 so far."

# def test_counting_with_negative_numbers():
#     counter = Counter()
#     counter.add(8)
#     assert counter.report() == "Counted to 8 so far."