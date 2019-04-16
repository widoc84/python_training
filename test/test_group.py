# -*- coding: utf-8 -*-
from model.group import Group
import random
import pytest
import allure


def test_add_group(app, db, json_groups):
    with allure.step('Get new Group'):
        group = json_groups
    with allure.step('Get old Groups'):
        old_groups = db.get_group_list()
    with allure.step('Create Group with name %s' % group):
        app.group.create(group)
    with allure.step('Check Group'):
        new_groups = db.get_group_list()
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_nmx) == sorted(new_groups, key=Group.id_or_nmx)

def test_edit_group(app, db, json_groups, check_ui):
    with allure.step('Get new Group'):
        group_j = json_groups
    with allure.step('Check count Group'):
        if len(db.get_group_list()) == 0:
            app.group.create(group_j)
    with allure.step('Get list old Groups and choice'):
        old_groups = db.get_group_list()
        group = random.choice(old_groups)
    with allure.step('Edit Group with name %s' % group):
        app.group.edit_by_id(group.id, group)
    with allure.step('Check Group'):
        new_groups = db.get_group_list()
        assert len(old_groups) == len(new_groups)
        new_groups = app.group.get_group_list()
        if check_ui:
            assert sorted(old_groups, key=Group.id_or_nmx) == sorted(new_groups, key=Group.id_or_nmx)

def test_delete_group(app, db, json_groups, check_ui):
    with allure.step('Get new Group'):
        group = json_groups
    with allure.step('Check count Group'):
        if len(db.get_group_list()) == 0:
            app.group.create(group)
    with allure.step('Get list old Groups and choice'):
        old_groups = db.get_group_list()
        group = random.choice(old_groups)
    with allure.step('Edit Group with name %s' % group):
        app.group.delete_by_id(group.id)
    with allure.step('Check Group'):
        new_groups = db.get_group_list()
        assert len(old_groups) - 1 == len(new_groups)
        old_groups.remove(group)
        assert old_groups == new_groups
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_nmx) == sorted(app.group.get_group_list(), key=Group.id_or_nmx)


