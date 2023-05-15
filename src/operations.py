import datetime
from dataclasses import dataclass


@dataclass
class Operations:
	operation_id: int
	operation_state: str
	operation_date: str
	# operationAmount: dict
	amount: str
	# currency: str
	currency_name: str
	currency_code: str
	description: str
	sender: str = 'null'
	recipient: str = ''

	def convert_str2datetime(self):
		data_datetime = datetime.datetime.strptime(self.operation_date, "%Y-%m-%dT%H:%M:%S.%f")
		date_int = int(datetime.datetime.timestamp(data_datetime) * 10 ** 6)
		print(f'{data_datetime} -> {date_int}')
		# return date_int, data_datetime.date().strftime("%Y.%m.%d")
		return data_datetime.date().strftime("%Y.%m.%d")

	def mask_num_sender(self):
		nums = self.sender.split()[1]
		account_type = self.sender.split()[0]
		if len(nums) == 16:
			return f'{account_type} {nums[0:4]} {nums[4:6]} ****** {nums[-4:]}'
		elif len(nums) == 20:
			return f'{account_type} ** {nums[-4:]}'
		else:
			print(f'{account_type} {nums[0:4]} {nums[4:6]} ****** {nums[-4:]}')

	def mask_num_recipient(self):
		nums = self.recipient.split()[1]
		account_type = self.recipient.split()[0]
		if len(nums) == 16:
			return f'{account_type} {nums[0:4]} {nums[4:6]} ****** {nums[-4:]}'
		elif len(nums) == 20:
			return f'{account_type} ** {nums[-4:]}'

	def __repr__(self):
		return f'\n{self.convert_str2datetime()} {self.description}' \
			f'\n{self.mask_num_sender()} -> {self.mask_num_recipient()}' \
			f'\n{self.amount}'

	def __str__(self):
		return f'\n{self.convert_str2datetime()} {self.description}' \
			f'\n{self.mask_num_sender()} -> {self.mask_num_recipient()}' \
			f'\n{self.amount}'


if __name__ == '__main__':

	data = [{'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041',
		'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
		'description': 'Перевод организации', 'from': 'Maestro 1596837868705199',
		'to': 'Счет 64686473678894779589'},
		{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364',
		'operationAmount': {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}},
		'description': 'Перевод организации', 'from': 'MasterCard 7158300734726758',
		'to': 'Счет 35383033474447895560'},
			{'id': 41428800, 'state': 'EXECUTED', 'date': '2019-09-03T18:35:29.512364',
			 'operationAmount': {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}},
			 'description': 'Перевод организации', 'from': 'MasterCard 7158300734726758',
			 'to': 'Счет 35383033474447895560'}
			]

	transactions = []

	for i in data:
		transactions.append(Operations(
			operation_id=i['id'],
			operation_state=i['state'],
			operation_date=i['date'],
			amount=i['operationAmount']['amount'],
			currency_name=i['operationAmount']['currency']['name'],
			currency_code=i['operationAmount']['currency']['code'],
			description=i['description'],
			sender=i['from'],
			recipient=i['to'])
			)

	sorted_transactions = sorted(transactions, key=lambda operations: operations.convert_str2datetime(), reverse=True)
	print(sorted_transactions)
