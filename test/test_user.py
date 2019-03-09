# -*- coding: utf-8 -*-
from model.user import User
from random import randrange
import random
import string
import re
import pytest


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_number(maxlen):
    symbols = string.digits
    return ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_email(maxlen):
    symbols = string.ascii_letters
    return ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + "@ya.ru"

testdata = [
    User(last_name=last_name, username=username,nickname=nickname,title=title,address=address, homephone=homephone,
         workphone=workphone,mobilephone=mobilephone,secondaryphone=secondaryphone,email=email,email2=email2,email3=email3)
    for last_name in random_string("last_name",10)
    for username in random_string("username",10)
    for nickname in random_string("nickname",10)
    for title in random_string("title",8)
    for address in random_string("address",40)
    for homephone in random_number(7)
    for workphone in [random_number(7)]
    for mobilephone in [random_number(7)]
    for secondaryphone in [random_number(7)]
    for email in [random_email(7)]
    for email2 in [random_email(7)]
    for email3 in [random_email(7)]
]
user_begin = {
    "last_name": "last_name",
    "username": "name",
    "nickname": "nicknames",
    "title": "title",
    "address": "new address",
    "homephone": "7777777",
    "workphone": "7777777",
    "mobilephone": "7777777",
    "secondaryphone": "7777777",
    "email": "test1@ya.ru",
    "email2": "test2@ya.ru",
    "email3": "test3@ya.ru"
}

user_edit = {
    "username": "name_edit",
    "last_name": "last_name_edit",
    "nickname": "nicknames_edit",
    "title": "title_edit",
    "address": "new address",
    "homephone": "7777778",
    "workphone": "7777778",
    "mobilephone": "7777778",
    "secondaryphone": "7777778",
    "email": "test1_edit@ya.ru",
    "email2": "test2_edit@ya.ru",
    "email3": "test3_edit@ya.ru"
}


@pytest.mark.parametrize("user", testdata, ids=[repr(x) for x in testdata])
def test_add_user(app, user):
    old_user = app.user.get_user_list()
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


