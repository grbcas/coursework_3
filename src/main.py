from pathlib import Path
from src.operation import Operation
from src.utils import get_data_from_json, get_data_path, unzip

file_to_unzip = Path(get_data_path(), 'operations.zip')
unzip(file_to_unzip)
data_path = Path(get_data_path(), 'operations.json')

data = get_data_from_json(data_path)

transactions = []

for i in data:
	transactions.append(Operation(
		operation_id=i.get('id'),
		operation_state=i.get('state', {}),
		operation_date=i.get('date', '2010-10-10T00:00:00.000000'),
		amount=i.get('operationAmount', {}).get('amount'),
		currency_name=i.get('operationAmount', {}).get('currency', {}).get('name', {}),
		currency_code=i.get('operationAmount', {}).get('currency', {}).get('code', {}),
		description=i.get('description', {}),
		sender=i.get('from', '__ __'),
		recipient=i.get('to', '__ __'))
	)
# print(transactions)
sorted_transactions = sorted(transactions, key=lambda operation: operation.convert_str_to_datetime(), reverse=True)

for i in range(5):
	print(sorted_transactions[i])
