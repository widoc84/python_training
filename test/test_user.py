# -*- coding: utf-8 -*-
from model.user import User
from random import randrange
import re
import random



def test_add_user(app,db, json_users):
    user = json_users
    old_user = db.get_user_list()
    app.user.add(user)
    new_user = db.get_user_list()
    old_user.append(user)
    assert sorted(old_user, key=User.id_or_nmx) == sorted(new_user, key=User.id_or_nmx)

def test_edit_user(app,db,json_users,check_ui):
    user_j = json_users
    if len(db.get_group_list()) == 0:
        app.user.add(user_j)
    old_user = db.get_user_list()
    user = random.choice(old_user)
    app.user.change_by_id(user.id, user)
    new_user = db.get_user_list()
    assert len(old_user) == len(new_user)
    new_user = app.user.get_user_list()
    if check_ui:
        assert sorted(old_user, key=User.id_or_nmx) == sorted(new_user, key=User.id_or_nmx)

def test_delete_user(app,db,json_users,check_ui):
    user_j = json_users
    if len(db.get_group_list()) == 0:
        app.user.add(user_j)
    old_user = db.get_user_list()
    user = random.choice(old_user)
    app.user.delete_by_id(user.id)
    new_user = db.get_user_list()
    assert len(old_user) - 1 == len(new_user)
    old_user.remove(user)
    assert old_user == new_user
    new_user = app.user.get_user_list()
    if check_ui:
        assert sorted(old_user, key=User.id_or_nmx) == sorted(new_user, key=User.id_or_nmx)


def test_check_random_contact(app):
    old_user = app.user.get_user_list()
    index = randrange(len(old_user))
    contact_from_home_page = old_user[index]
    contact_from_edit_page = app.user.get_user_info_from_edit(index)
    assert contact_from_home_page.last_name == contact_from_edit_page.last_name
    assert contact_from_home_page.username == contact_from_edit_page.username
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phone == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_email == merge_email_like_on_home_page(contact_from_edit_page)


def test_phones_on_home_page(app):
    contact_from_home_page = app.user.get_user_list()[0]
    contact_from_edit_page = app.user.get_user_info_from_edit(0)
    assert contact_from_home_page.all_phone == merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_view_page(app):
    contact_from_view_page = app.user.open_contact_view_by_index(0)
    contact_from_edit_page = app.user.get_user_info_from_edit(0)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone

def clear(s):
    return re.sub("[() -]", "",s)

def merge_phones_like_on_home_page(user):
    return "\n".join(filter(lambda x: x!=" ",
                            map(lambda x: clear(x), filter(lambda x: x is not None,
                                                           [user.homephone, user.mobilephone,user.workphone,user.secondaryphone]))))

def merge_email_like_on_home_page(user):
    return "\n".join(filter(lambda x: x!=" ",
                            map(lambda x: clear(x), filter(lambda x: x is not None,
                                                           [user.email, user.email2,user.email3]))))


