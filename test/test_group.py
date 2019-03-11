# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange
from fixture.additional import MH
import pytest



group_begin = {
    "name": "test1",
    "header": "testheader1",
    "footer": "testfooter1"
}

group_edit = {
    "name": "test1",
    "header": "testheader1",
    "footer": "testfooter1"
}

testdata = [
    Group(name=MH.random_string("name",10), header=MH.random_string("header",20),footer=MH.random_string("footer",20)),
    Group(name=MH.random_string("name", 10), header="",footer=MH.random_string("footer", 20)),
    Group(name=MH.random_string("name", 10), header=MH.random_string("header", 20),footer=""),
    Group(name="", header=MH.random_string("header",20),footer=MH.random_string("footer",20)),
    Group(name="", header="", footer=""),
]
@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_nmx) == sorted(new_groups, key=Group.id_or_nmx)

def test_edit_group(app):
    if app.group.count() == 0:
        app.group.create(Group(**group_begin))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(**group_edit)
    group.id = old_groups[index].id
    app.group.edit_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_nmx) == sorted(new_groups, key=Group.id_or_nmx)

def test_delete_group(app):
    if app.group.count() == 0:
        app.group.create(Group(**group_begin))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.delete_by_index(index)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index:index+1] = []
    assert old_groups == new_groups


