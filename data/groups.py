# -*- coding: utf-8 -*-
from model.group import Group
from fixture.additional import MH

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
    Group(name=MH.random_string("name",10), header=MH.random_string("header",20),footer=MH.random_string("footer",20))
    for i in range(1)
]