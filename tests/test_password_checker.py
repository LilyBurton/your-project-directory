import pytest
from lib.password_checker import PasswordChecker

def test_to_check_password():
    password_checker = PasswordChecker()
    password_checker.check("12345678")
    with pytest.raises(Exception) as e:
        password_checker.check("12345678")
        error_message = str(e.value)
        assert error_message == "Invalid password, must be 8+ characters."