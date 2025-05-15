from dataset_handler import DatasetHandler

def get_user_input():
    file_name = input('Введите путь к файлу (Например, data.csv): ').strip()
    columns_input = input('Введите ожидаемые колонки через запятую: ')
    expected_columns = [col.strip() for col in columns_input.split(',')]

    return file_name, expected_columns

def main():
    file_name, expected_columns = get_user_input()
    handler = DatasetHandler(file_name=file_name, expected_columns=expected_columns)
    success = handler.process_dataset()

    if success:
        print(f'Чтение датафрейма завершено успешно.')
    else:
        print(f'Возникла ошибка.')

if __name__ == '__main__':
    main()