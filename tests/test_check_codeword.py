from lib.check_codeword import *

def test_check_codeword_correct():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

def test_check_codeword_incorrect():
    result = check_codeword("hare")
    assert result == "Close, but nope."

def test_check_codeword_with_right_first_letter_and_wrong_last_letter():
    result = check_codeword("happy")
    assert result == "WRONG!"

def test_check_codeword_with_right_last_letter_and_wrong_first_letter():
    result = check_codeword("mice")
    assert result == "WRONG!"


def test_check_codeword_wrong():
    result = check_codeword("cheese")
    assert result == "WRONG!"