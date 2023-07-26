import pytest
from lib.present import Present

def test_wrap_and_unwrap_present():
    present = Present()
    present.wrap("Socks")
    assert present.unwrap() == "Socks"
    
def test_wrapping_present():
    present = Present()
    with pytest.raises(Exception) as e:
        present.wrap("socks")
        error_message = str(e.value)
        assert error_message == "A contents has already been wrapped."

def test_unwrapping_present():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap("socks")
        error_message = str(e.value)
        assert error_message == "A contents has already been wrapped."

def test_wrap_and_unwrap_preserves_present():
    present = Present()
    present.wrap(44)
    with pytest.raises(Exception) as e:
        present.wrap(66)
    assert present.unwrap() == 44