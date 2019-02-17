# -*- coding: utf-8 -*-
from model.user import User


def test_add_user(app):
    app.session.login(username="admin", password="secret")
    app.user.add(User(username="name", last_name="last_name", nickname="nicknames", title="title", tel="7777777",
                      mail="test@ya.ru"))
    app.session.logout()


def test_edit_user(app):
    app.session.login(username="admin", password="secret")
    app.user.change(User(username="name_edit", last_name="last_name_edit", nickname="nicknames_edit", title="title_edit", tel="7777778",
                      mail="test_edit@ya.ru"))
    app.session.logout()


def test_delete_user(app):
    app.session.login(username="admin", password="secret")
    app.user.delete()
    app.session.logout()
