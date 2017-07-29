# -*- coding: utf-8 -*-
import os

from unittest.mock import ANY

from aratrum import Aratrum

from pytest import fixture

import ujson


@fixture
def config_teardown(request):
    def teardown():
        os.remove('test.json')
    request.addfinalizer(teardown)


@fixture
def config_file(config_teardown):
    config = """
    {
        "server": {},
        "name": "myvalue"
    }
    """
    with open('test.json', 'w') as f:
        f.write(config)


@fixture
def aratrum():
    return Aratrum()


def test_init(mocker):
    expected = os.path.join(os.getcwd(), 'config.json')
    assert Aratrum().filename == expected


def test_init_filename():
    expected = os.path.join(os.getcwd(), 'config2.json')
    assert Aratrum('config2.json').filename == expected


def test_get(config_file):
    result = Aratrum(filename='test.json').get()
    assert 'server' in result
    assert 'name' in result


def test_set(aratrum):
    aratrum.set('option', 'value')
    assert aratrum.config['option'] == 'value'


def test_delete(aratrum):
    aratrum.config = {'option': 'value'}
    aratrum.delete('option')
    assert 'option' not in aratrum.config


def test_delete_empty(aratrum):
    aratrum.delete('option')


def test_defaults():
    result = Aratrum().defaults()
    assert type(result) == dict


def test_save(mocker, config_teardown):
    mocker.patch.object(ujson, 'dump')
    config = Aratrum('test.json')
    config.save()
    ujson.dump.assert_called_with(config.config, ANY, indent=4)
