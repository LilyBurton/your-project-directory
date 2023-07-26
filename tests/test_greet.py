from lib.greet import *

def test_greet():
    result = greet("Lily")
    assert result == "Hello, Lily!"