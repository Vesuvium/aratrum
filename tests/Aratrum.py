# -*- coding: utf-8 -*-
import json
import os

from unittest.mock import ANY

from aratrum import Aratrum

from pytest import fixture


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


def test_init():
    assert Aratrum().filename == 'config.json'


def test_init_filename():
    assert Aratrum('config2.json').filename == 'config2.json'


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
    mocker.patch.object(json, 'dump')
    config = Aratrum('test.json')
    config.save()
    json.dump.assert_called_with(config.config, ANY, indent=4)
