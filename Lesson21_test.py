import pytest
import Lesson21
from helpers.data import user as user_data

def test_registration_success():
    assert Lesson21.registration() == user_data.nick