from newssite import create_app
import pytest as pt


@pt.mark.parametrize("input,expected", [
    ('newssite.config.DevConfig', False),
    ('newssite.config.ProdConfig', False),
    ('newssite.config.TestConfig', True)
])
def test_config_load(input, expected):
    app = create_app(input)
    assert app.config['TESTING'] == expected
