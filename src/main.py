from pathlib import Path
from src.operations import Operations
from src.utils import get_data_from_json, get_data_path, unzip

file_to_unzip = Path(get_data_path(), 'operations.zip')
unzip(file_to_unzip)
data_path = Path(get_data_path(), 'operations.json')

data = get_data_from_json(data_path)

transactions = []

for i in data:
	transactions.append(Operations(
		operation_id=i.get('id'),
		operation_state=i.get('state', {}),
		operation_date=i.get('date'),
		amount=i.get('operationAmount', {}).get('amount'),
		currency_name=i.get('operationAmount', {}).get('currency', {}).get('name', {}),
		currency_code=i.get('operationAmount', {}).get('currency', {}).get('code', {}),
		description=i.get('description', {}),
		sender=i.get('from', ''),
		recipient=i.get('to'))
	)

sorted_transactions = sorted(transactions, key=lambda operations: operations.convert_str2datetime(), reverse=True)

sorted_transactions[0]
# for i in range(5):
# 	print(sorted_transactions[i])
