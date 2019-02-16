# -*- coding: utf-8 -*-
from model.user import User


def test_add_user(app):
    app.session.login(username="admin", password="secret")
    app.user.add(User(username="name", last_name="last_name", nickname="nicknames", title="title", tel="7777777",
                      mail="test@ya.ru"))
    app.session.logout()
