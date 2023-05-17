import datetime
from dataclasses import dataclass


@dataclass
class Operation:
	operation_id: int = None
	operation_state: str = None
	operation_date: str = None
	# operationAmount: dict
	amount: str = None
	# currency: str
	currency_name: str = None
	currency_code: str = None
	description: str = None
	sender: str = None
	recipient: str = None

	def convert_str_to_datetime(self) -> str:
		"""
		Convert input string to "%Y.%m.%d"
		:return: str
		"""
		if self.operation_date:
			data_datetime = datetime.datetime.strptime(self.operation_date, "%Y-%m-%dT%H:%M:%S.%f")
			return data_datetime.date().strftime("%Y.%m.%d")
		else:
			return f"%Y.%m.%d"

	def mask_num_sender(self) -> str:
		"""
		Mask sender account digits
		:return: str
		"""
		if not self.sender:
			return 'None None'
		nums = self.sender.split()[-1]
		account_type = ' '.join(self.sender.split()[:-1])
		if len(nums) == 16:
			return f'{account_type} {nums[0:4]} {nums[4:6]}** **** {nums[-4:]}'
		elif len(nums) == 20:
			return f'{account_type} **{nums[-4:]}'
		else:
			return f'{account_type}'

	def mask_num_recipient(self) -> str:
		"""
		Mask recipient account digits
		:return: str
		"""
		if not self.recipient:
			return 'None None'
		nums = self.recipient.split()[-1]
		account_type = ' '.join(self.recipient.split()[:-1])
		if len(nums) == 16:
			return f'{account_type} {nums[0:4]} {nums[4:6]}** **** {nums[-4:]}'
		elif len(nums) == 20:
			return f'{account_type} **{nums[-4:]}'

	def __repr__(self):
		return f'\n{self.convert_str_to_datetime()} {self.description}' \
			f'\n{self.mask_num_sender()} -> {self.mask_num_recipient()}' \
			f'\n{self.amount} {self.currency_name}'

	def __str__(self):
		return self.__repr__()
		# return f'\n{self.convert_str_to_datetime()} {self.description}' \
		# 	f'\n{self.mask_num_sender()} -> {self.mask_num_recipient()}' \
		# 	f'\n{self.amount} {self.currency_name}'


# if __name__ == '__main__':
# 	print(Operation())
#
# 	data = [{'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041',
# 		'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
# 		'description': 'Перевод организации', 'from': 'Maestro 1596837868705199',
# 		'to': 'Счет 64686473678894779589'},
# 		{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364',
# 		'operationAmount': {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}},
# 		'description': 'Перевод организации', 'from': 'MasterCard 7158300734726758',
# 		'to': 'Счет 35383033474447895560'},
# 			{'id': 41428800, 'state': 'EXECUTED', 'date': '2019-09-03T18:35:29.512364',
# 			 'operationAmount': {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}},
# 			 'description': 'Перевод организации', 'from': 'MasterCard 7158300734726758',
# 			 'to': 'Счет 35383033474447895560'}
# 			]
#
# 	transactions = []
#
# 	for i in data:
# 		transactions.append(Operation(
# 			operation_id=i['id'],
# 			operation_state=i['state'],
# 			operation_date=i['date'],
# 			amount=i['operationAmount']['amount'],
# 			currency_name=i['operationAmount']['currency']['name'],
# 			currency_code=i['operationAmount']['currency']['code'],
# 			description=i['description'],
# 			sender=i['from'],
# 			recipient=i['to'])
# 			)
#
# 	sorted_transactions = sorted(transactions, key=lambda operation: operation.convert_str_to_datetime(), reverse=True)
# 	print(sorted_transactions)
