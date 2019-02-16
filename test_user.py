# -*- coding: utf-8 -*-
import pytest
from user import User
from application import Applicaton

@pytest.fixture
def app(request):
    fixture = Applicaton()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_user(app):
    app.login(username="admin", password="secret")
    app.add_user(User(username="name", last_name="last_name", nickname="nicknames", title="title", tel="7777777",
                 mail="test@ya.ru"))
    app.logout()