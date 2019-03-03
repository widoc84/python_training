# -*- coding: utf-8 -*-
from model.user import User

user_begin = {
    "last_name": "last_name",
    "username": "name",
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
    old_user = app.user.get_user_list()
    user = User(**user_begin)
    app.user.add(user)
    new_user = app.user.get_user_list()
    assert len(old_user) + 1 == len(new_user)
    old_user.append(user)
    assert sorted(old_user, key=User.id_or_nmx) == sorted(new_user, key=User.id_or_nmx)

def test_edit_user(app):
    if app.user.count() == 0:
        app.user.add(User(**user_begin))
    old_user = app.user.get_user_list()
    user = User(**user_edit)
    user.id = old_user[0].id
    app.user.change(user)
    new_user = app.user.get_user_list()
    assert len(old_user) == len(new_user)
    old_user[0] = user
    assert sorted(old_user, key=User.id_or_nmx) == sorted(new_user, key=User.id_or_nmx)


def test_delete_user(app):
    if app.user.count() == 0:
        app.user.add(User(**user_begin))
    app.user.delete()
    new_user = app.user.get_user_list()
    old_user = []
    assert sorted(old_user, key=User.id_or_nmx) == sorted(new_user, key=User.id_or_nmx)

def test_count_edit_user(app):
    if app.user.count() == 0:
        app.user.add(User(**user_begin))
    old_user = app.user.get_user_list()
    user = User(**user_edit)
    user.id = old_user[0].id
    app.user.change(User(**user_edit))
    new_user = app.user.get_user_list()
    assert len(old_user) == len(new_user)
    old_user[0] = user
    assert sorted(old_user, key=User.id_or_nmx) == sorted(new_user, key=User.id_or_nmx)
    app.user.delete()

def test_count_delete_user(app):
    if app.user.count() == 0:
        app.user.add(User(**user_begin))
    app.user.delete()
    new_user = app.user.get_user_list()
    old_user = []
    assert sorted(old_user, key=User.id_or_nmx) == sorted(new_user, key=User.id_or_nmx)
