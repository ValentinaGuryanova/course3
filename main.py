from utils import get_data, get_filtered_data, get_sorted_data, print_result

FILE_NAME = "operations.json"

def main():
    """выводит на экран список из 5 последних выполненных клиентом операций"""

    print("Курсовой проект по курсу «Основы backend-разработки»")
    data = get_data(FILE_NAME)
    data = get_filtered_data(data)
    data = get_sorted_data(data)
    data = print_result(data)
    print(data)


if __name__ == '__main__':
    main()
