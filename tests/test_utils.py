import pytest
from pathlib import Path
from src.utils import get_data_path, get_data_from_json, unzip

import json

PATH = Path(Path(__file__).parent, 'data')


def test_get_data_path():
    """
    data pathfinding test
    :return:
    """
    assert isinstance(get_data_path(), Path) == True


def test_unzip():
    """
    test unpacking of .zip file to .json file
    :return:
    """
    zip_file = Path(PATH, 'operations.zip')
    unzip(zip_file)
    data_file = Path(PATH, 'operations.json')
    unzip_file = Path.is_file(data_file)
    assert unzip_file == True


def test_get_data_from_json_negative():
    """
    test Load data if file absent
    :return:
    """
    path_to_json_file = Path(PATH, 'operations.json.none')
    result = get_data_from_json(path_to_json_file)
    assert result is None


def test_get_data_from_json():
    """
    test Load data from json file
    :return:
    """
    path_to_json_file = Path(PATH, 'operations.json')
    result = get_data_from_json(path_to_json_file)
    assert isinstance(result, list)


# def load_tc_from_file(tc_params, tc_file):
#     params = [x.strip() for x in tc_params.split(',')]
#
#     def wrapper(function):
#         with open(tc_file) as f:
#             tc_data = json.loads(f.read())
#         tc_cases = [tuple((case[p] for p in params)) for case in tc_data]
#         function.tc_cases = tc_cases
#         function.tc_params = tc_params
#
#         return function
#     return wrapper
#
#
# def pytest_generate_tests(metafunc):
#     if getattr(metafunc.function, 'tc_cases', None):
#         metafunc.parametrize(metafunc.function.tc_params, metafunc.function.tc_cases)


# @load_tc_from_file('test_input, expected', './tc.json')
# def get_data_from_json(test_input, expected):
#     assert eval(test_input) == expected
