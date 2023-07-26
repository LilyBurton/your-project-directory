from lib.report_length import *

def test_report_length():
    result = report_length("Lily")
    length = len("Lily")
    assert result == f"This string was 4 characters long."