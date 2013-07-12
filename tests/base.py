#!/usr/bin/env python
# -*- coding: utf-8 -*-
from webtest import TestApp

from ..main import app

app = TestApp(app)


def test_index():
    response = app.get('/')
    assert 'Hello world!' in str(response), response
