# -*- coding: utf-8 -*-
from model.group import Group

group_begin = {
    "name": "test1",
    "header": "testheader1",
    "footer": "testfooter1"
}

group_edit = {
    "name": "test1edit",
    "header": "testheader1edit",
    "footer": "testfooter1edit"
}

def test_add_group(app):
    app.group.create(Group(**group_begin))

def test_edit_group(app):
    if app.group.count() == 0:
        app.group.create(Group(**group_begin))
    app.group.edit(Group(**group_edit))

def test_delete_group(app):
    if app.group.count() == 0:
        app.group.create(Group(**group_begin))
    app.group.delete()

def test_check_count_edit_group(app):
    if app.group.count() == 0:
        app.group.create(Group(**group_begin))
    app.group.edit(Group(**group_edit))
    app.group.delete()

def test_check_count_delete_group(app):
    if app.group.count() == 0:
        app.group.create(Group(**group_begin))
    app.group.delete()


