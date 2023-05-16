import datetime
from pathlib import Path
import pytest
from src.operation import Operation

PATH = Path(Path(__file__).parent, 'data')


@pytest.fixture
def test_data():
    return [{
        'id': 441945886,
        'state': 'EXECUTED',
        'date': '2019-08-26T10:50:58.294041',
        'operationAmount': {
            'amount': '31957.58',
            'currency': {
                'name': 'руб.',
                'code': 'RUB'
            }
        },
        'description': 'Перевод организации',
        'from': 'Maestro 1596837868705199',
        'to': 'Счет 64686473678894779589'
    },
        '2019.08.26',
        'Maestro 1596 83** **** 5199',
        'Счет **9589'
        ]


def test_convert_convert_str_to_datetime(test_data):
    """
    string-to-date-to-string conversion test
    :return:
    """
    data = test_data[0]
    operation = Operation()
    operation.operation_date = data.get('date')
    str2datetime = operation.convert_str_to_datetime()
    assert str2datetime == test_data[1]


def test_mask_num_sender(test_data):
    """
    masks the card number and is not displayed entirely in XXX XXX** **** XXXX format
    :param test_data:
    :return:
    """
    data = test_data[0]
    operation = Operation()
    operation.sender = data.get('from')
    masked_account = operation.mask_num_sender()
    assert masked_account == test_data[2]


def test_mask_num_recipient(test_data):
    """
    masks the account number and is not displayed entirely in the format **XXXX
    :param test_data:
    :return: True
    """
    data = test_data[0]
    operation = Operation()
    operation.recipient = data.get('to')
    masked_account = operation.mask_num_recipient()
    assert masked_account == test_data[3]


def test_mask_num_sender_empty():
    """
    tests the function if the account number is empty
    :return: str
    """
    operation = Operation()
    operation.sender = 'None None'
    masked_account = operation.mask_num_sender()
    assert masked_account == 'None'
