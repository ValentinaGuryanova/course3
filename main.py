from utils import get_data, get_filtered_data, get_sorted_data, get_formatted
FILE_NAME = "operations.json"
def main():
    print("Course work 3")
    data = get_data(FILE_NAME)
    print(data)
    data = get_filtered_data(data)
    print(data)
    data = get_sorted_data(data)
    print(data)
    data = get_formatted(data)
    print(data)


if __name__ == '__main__':
    main()
