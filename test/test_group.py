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
    old_groups = app.group.get_group_list()
    group = Group(**group_begin)
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_nmx) == sorted(new_groups, key=Group.id_or_nmx)

def test_edit_group(app):
    if app.group.count() == 0:
        app.group.create(Group(**group_begin))
    old_groups = app.group.get_group_list()
    group = Group(**group_edit)
    group.id = old_groups[0].id
    app.group.edit(Group(**group_edit))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_nmx) == sorted(new_groups, key=Group.id_or_nmx)

def test_delete_group(app):
    if app.group.count() == 0:
        app.group.create(Group(**group_begin))
    old_groups = app.group.get_group_list()
    app.group.delete()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[0:1] = []
    assert old_groups == new_groups

def test_check_count_edit_group(app):
    if app.group.count() == 0:
        app.group.create(Group(**group_begin))
    old_groups = app.group.get_group_list()
    group = Group(**group_edit)
    group.id = old_groups[0].id
    app.group.edit(Group(**group_edit))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_nmx) == sorted(new_groups, key=Group.id_or_nmx)
    app.group.delete()

def test_check_count_delete_group(app):
    if app.group.count() == 0:
        app.group.create(Group(**group_begin))
    old_groups = app.group.get_group_list()
    app.group.delete()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[0:1] = []
    assert old_groups == new_groups


