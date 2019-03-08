# -*- coding: utf-8 -*-
from model.user import User
from random import randrange

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
    assert len(old_user) + 1 == app.user.count()
    new_user = app.user.get_user_list()
    old_user.append(user)
    assert sorted(old_user, key=User.id_or_nmx) == sorted(new_user, key=User.id_or_nmx)

def test_edit_user(app):
    if app.user.count() == 0:
        app.user.add(User(**user_begin))
    old_user = app.user.get_user_list()
    index = randrange(len(old_user))
    user = User(**user_edit)
    user.id = old_user[index].id
    app.user.change_by_index(index, user)
    assert len(old_user) == app.user.count()
    new_user = app.user.get_user_list()
    old_user[index] = user
    assert sorted(old_user, key=User.id_or_nmx) == sorted(new_user, key=User.id_or_nmx)


def test_delete_user(app):
    if app.user.count() == 0:
        app.user.add(User(**user_begin))
    old_user = app.user.get_user_list()
    index = randrange(len(old_user))
    indexid = old_user[index].id
    app.user.delete_by_index(indexid)
    new_user = app.user.get_user_list()
    old_user[index:index+1] = []
    assert sorted(old_user, key=User.id_or_nmx) == sorted(new_user, key=User.id_or_nmx)

