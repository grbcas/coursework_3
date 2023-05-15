"""
Get data from zip file
"""
import json
import zipfile
from pathlib import Path


def get_data_path() -> Path:
	"""
	get path for folder 'data' in project
	:return: Path
	"""
	return Path(Path(__file__).parent.parent, 'data')


def unzip(path_to_zip_file):
	"""
	Unzip input zip file to 'project/data' folder
	:param path_to_zip_file:
	"""
	with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
		zip_ref.extractall(Path(path_to_zip_file).parent)


def get_data_from_json(path_to_json_file: Path) -> list:
	"""
	Load data from json file
	:param path_to_json_file:
	:return: list
	"""
	try:
		with open(path_to_json_file, mode='r', encoding='UTF8') as f:
			data = json.load(f)
		return data
	except FileNotFoundError:
		print('The file is not present.')


if __name__ == '__main__':
	print(get_data_path())
	file_to_unzip = Path(get_data_path(), 'operations.zip')
	unzip(file_to_unzip)
	data_path = Path(get_data_path(), 'operations.json')
	res = get_data_from_json(data_path)
	print(res)
