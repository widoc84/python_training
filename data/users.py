# -*- coding: utf-8 -*-
from model.user import User
from fixture.additional import MH

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

testdata = [
    User(last_name=MH.random_string("last_name", 10),
         username=MH.random_string("username", 10),
         nickname=MH.random_string("nickname", 10),
         title=MH.random_string("title", 8),
         address=MH.random_string("address", 40),
         homephone=MH.random_number(7),
         workphone=MH.random_number(7),
         mobilephone=MH.random_number(7),
         secondaryphone=MH.random_number(7),
         email=MH.random_email(7),
         email2=MH.random_email(7),
         email3=MH.random_email(7))
    for i in range(1)
]