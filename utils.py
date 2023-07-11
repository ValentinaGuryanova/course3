from datetime import datetime
import json

def get_data(file_name):
    """Получает данные из файла"""

    with open(file_name, "r", encoding="utf-8") as file:
        file_data = file.read()
    return json.loads(file_data)


def get_filtered_data(data):
    """Фильтрует данные из файла"""

    new_data = []
    for transaction in data:
        if transaction and transaction.get('state') == 'EXECUTED':
            new_data.append(transaction)
    return new_data


def get_sorted_data(data):
    """Сортирует данные из файла"""

    data = sorted(data, key=lambda x: x['date'], reverse=True)
    return data[:5]


def print_result(data):
    """Форматирует данные из файла и выводит на печать"""

    for transaction in data:
        if transaction.get("from"):
            old_data = transaction["date"]
            date_transaction = datetime.strptime(old_data, "%Y-%m-%dT%H:%M:%S.%f")
            date_transaction = date_transaction.strftime("%d.%m.%Y")
            old_count_to = transaction["to"]
            count_transaction_to = old_count_to[-4:]
            old_count_from = transaction["from"]
            if not old_count_from.find("Счет"):
                count_transaction_from = old_count_from[-4:]
                print(f'\n{date_transaction} {transaction.get("description")}\nСчет **{count_transaction_from} -> Счет **{count_transaction_to}\n{transaction["operationAmount"]["amount"]} руб.')
            else:
                count_transaction_from = old_count_from[:-16]
                count_transaction_from_number = old_count_from[-16:]
                c1 = count_transaction_from_number[:4]
                c2 = count_transaction_from_number[4:6]
                c3 = count_transaction_from_number[-4:]
                print(f'\n{date_transaction} {transaction.get("description")}\n{count_transaction_from}{c1} {c2}** **** {c3} -> Счет **{count_transaction_to}\n{transaction["operationAmount"]["amount"]} руб.')
        else:
            old_data = transaction["date"]
            date_transaction = datetime.strptime(old_data, "%Y-%m-%dT%H:%M:%S.%f")
            date_transaction = date_transaction.strftime("%d.%m.%Y")
            old_count_to = transaction["to"]
            count_transaction_to = old_count_to[-4:]
            print(f'\n{date_transaction} {transaction.get("description")}\n-> Счет **{count_transaction_to}\n{transaction["operationAmount"]["amount"]} руб.')

