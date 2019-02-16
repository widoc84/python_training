# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="test1", header="testheader1", footer="testfooter1"))
    app.session.logout()


def test_delete_group(app):
    app.session.login(username="admin", password="secret")
    app.group.delete()
    app.session.logout()
