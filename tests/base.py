from ..main import app
from webtest import TestApp

app = TestApp(app)


def test_index():
    response = app.get('/')
    assert 'Hello world!' in str(response), response
