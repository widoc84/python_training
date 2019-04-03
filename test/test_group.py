# -*- coding: utf-8 -*-
from model.group import Group
import random



def test_add_group(app, db, json_groups):
    group = json_groups
    old_groups = db.get_group_list()
    app.group.create(group)
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_nmx) == sorted(new_groups, key=Group.id_or_nmx)

def test_edit_group(app, db, json_groups, check_ui):
    group_j = json_groups
    if len(db.get_group_list()) == 0:
        app.group.create(group_j)
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.edit_by_id(group.id, group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    new_groups = app.group.get_group_list()
    if check_ui:
        assert sorted(old_groups, key=Group.id_or_nmx) == sorted(new_groups, key=Group.id_or_nmx)

def test_delete_group(app, db, json_groups, check_ui):
    group = json_groups
    if len(db.get_group_list()) == 0:
        app.group.create(group)
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_nmx) == sorted(app.group.get_group_list(), key=Group.id_or_nmx)


