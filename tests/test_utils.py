import pytest
from pathlib import Path
from src.utils import get_data_path, get_data_from_json


@pytest.mark.parametrize("test_input,expected", [("operations.json", "operations.json")])
def test_get_data_path(test_input, expected):
	assert get_data_path(test_input) == Path(__file__)
