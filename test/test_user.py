# -*- coding: utf-8 -*-
from model.user import User

user_begin = {
    "username": "name",
    "last_name": "last_name",
    "nickname": "nicknames",
    "title": "title",
    "tel": "7777777",
    "mail": "test@ya.ru"
}

user_edit = {
    "username": "name_edit",
    "last_name": "last_name_edit",
    "nickname": "nicknames_edit",
    "title": "title_edit",
    "tel": "7777778",
    "mail": "test_edit@ya.ru"
}


def test_add_user(app):
    app.session.login(username="admin", password="secret")
    app.user.add(User(**user_begin))
    app.session.logout()


def test_edit_user(app):
    app.session.login(username="admin", password="secret")
    app.user.change(User(**user_edit))
    app.session.logout()


def test_delete_user(app):
    app.session.login(username="admin", password="secret")
    app.user.delete()
    app.session.logout()
