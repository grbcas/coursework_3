from pathlib import Path
from src.utils import get_data_path, get_data_from_json, unzip


PATH = Path(Path(__file__).parent, 'data')


def test_get_data_path():
    """
    data pathfinding test
    """
    assert isinstance(get_data_path(), Path) is True


def test_unzip():
    """
    test unpacking of .zip file to .json file
    """
    zip_file = Path(PATH, 'operations.zip')
    unzip(zip_file)
    data_file = Path(PATH, 'operations.json')
    unzip_file = Path.is_file(data_file)
    assert unzip_file is True


def test_get_data_from_json_negative():
    """
    test Load data if file absent
    """
    path_to_json_file = Path(PATH, 'operations.json.none')
    result = get_data_from_json(path_to_json_file)
    assert result == 'The file is not present'


def test_get_data_from_json():
    """
    test Load data from json file
    """
    path_to_json_file = Path(PATH, 'operations.json')
    result = get_data_from_json(path_to_json_file)
    assert isinstance(result, list)
