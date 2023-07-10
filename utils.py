from datetime import datetime
import json


# FILE_NAME = "operations.json"


def get_data(file_name):
    """Получает данные из файла"""

    with open(file_name, "r", encoding="utf-8") as file:
        # for data in file:
        #     print(data)
        #     return
        file_data = file.read()
        # ЗДЕСЬ ФАЙЛ ЕЩЕ ОТКРЫТ
    # ЗДЕСЬ ФАЙЛ УЖЕ ЗАКРЫТ
    return json.loads(file_data)


get_data("operations.json")


def get_filtered_data(data):
    """Фильтрует данные из файла"""

    new_data = []
    for transaction in data:
        if transaction and transaction.get("state") == 'EXECUTED':
            new_data.append(transaction)
    return new_data


def get_sorted_data(data):
    """Сортирует данные из файла"""
    data = sorted(data, key=lambda x: x['date'], reverse=True)
    return data[:5]


def get_formatted(data): # print_formatted_data
    """Форматирует данные из файла"""
    # пришло 5 обьектов
    for transaction in data:
        # transaction = {
        # 'id': 863064926,
        # 'state': 'EXECUTED',
        # 'date': '2019-12-08T22:46:21.935582',
        # 'operationAmount':
        # {'amount': '41096.24', 'currency': {'name': 'USD', 'code': 'USD'}},
        # 'description': 'Открытие вклада', 'from': 'Visa Classic 2842878893689012', 'to': 'Счет 90424923579946435907'}

        # для каждой transaction обработать случаи:
        # нет from / есть from
        # visa / maestro / счёт
        # обработать дату (уже сделано)
        # вывести на печать в отформ. виде

        old_data = transaction['date']
        # print(old_data)
        date_transaction = datetime.strptime(old_data, "%Y-%m-%dT%H:%M:%S.%f")
        # print(date_transaction)
        date_transaction = date_transaction.strftime("%d.%m.%Y")
        # print(date_transaction)
#     return [f"""
# {date_transaction} Перевод организации
# Visa Platinum 7000 79** **** 6361 -> Счет **9638
# 82771.72 руб."""]
