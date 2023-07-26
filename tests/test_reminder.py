import pytest
from lib.reminder import *

# def test_reminds_the_user_to_do_a_task():
#     reminder = Reminder("Lily")
#     reminder.remind_me_to("Feed the cat")
#     result = reminder.remind()
#     assert result == "Feed the cat, Lily!"


def test_reminder():
    reminder = Reminder("Kay")
    with pytest.raises(Exception) as e:
        reminder.remind()
    error_message = str(e.value)
    assert error_message == "No reminder set!"