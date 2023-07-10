from datetime import datetime
import json
FILE_NAME = "operations.json"

def get_data(file_name):
    """Получает данные из файла"""

    with open(file_name, "r", encoding="utf-8") as file:

       for data in file:
           print(data)

get_data("operations.json")

def get_filtered_data(data):
    """Фильтрует данные из файла"""

    new_data = []
    for transaction in data:
        if transaction['state'] in transaction and transaction['state'] == 'EXECUTED':
            new_data.append(transaction)
    print(new_data)


def get_sorted_data(data):
    """Сортирует данные из файла"""

    data = sorted(data, key=lambda x: x['date'], reverse=True)
    return data[:5]


def get_formatted(data):
    """Форматирует данные из файла"""

    for i in data:
        old_data = data[i]['date']
        print(old_data)
        date_transaction = datetime.strptime(old_data, "%Y-%m-%dT%H:%M:%S.%f")
        print(date_transaction)
        date_transaction = date_transaction.strftime("%d.%m.%Y")
        print(date_transaction)
        return [f"""
{date_transaction} Перевод организации
Visa Platinum 7000 79** **** 6361 -> Счет **9638
82771.72 руб."""]
