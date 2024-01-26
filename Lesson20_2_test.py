import pytest
import Lesson20_2
import user_data

def test_registration_success():
    assert Lesson20_2.registration() == user_data.nick