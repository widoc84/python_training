# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Applicaton


@pytest.fixture
def app(request):
    fixture = Applicaton()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="test1", header="testheader1", footer="testfooter1"))
    app.group.delete()
    app.session.logout()
