#!/usr/bin/env python
# -*- coding: utf-8 -*-
from webtest import TestApp

from ..main import app

app = TestApp(app)


def test_index():
    response = app.get('/')
    assert 'This will be your homepage' in str(response), response
