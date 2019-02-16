# -*- coding: utf-8 -*-
import pytest
from model.user import User
from fixture.application import Applicaton


@pytest.fixture
def app(request):
    fixture = Applicaton()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_user(app):
    app.session.login(username="admin", password="secret")
    app.user.add(User(username="name", last_name="last_name", nickname="nicknames", title="title", tel="7777777",
                      mail="test@ya.ru"))
    app.session.logout()
