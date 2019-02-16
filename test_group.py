# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Applicaton

@pytest.fixture
def app(request):
    fixture = Applicaton()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="test1", header="testheader1", footer="testfooter1"))
    app.delete_group()
    app.logout()