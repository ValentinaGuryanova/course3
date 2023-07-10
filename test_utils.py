from utils import get_data, get_filtered_data, get_sorted_data, get_formatted

def test_get_data():
    assert isinstance(get_data(), list)


def test_get_filtered_data():
    assert len(get_filtered_data([{"state": "EXECUTED"}, {"state": "CANCELED"}])) == 2


def test_get_sorted_data():
    assert get_sorted_data([{'date': "2020-08-26T10:50:58.294041"}, {'date': "2019-08-26T10:50:58.294041"}, {'date': "2021-08-26T10:50:58.294041"}])


def test_get_formatted():
    assert get_formatted(data=[{
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
    }]) == ['\n26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n82771.72 руб.']
