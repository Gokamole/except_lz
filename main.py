from dataset_handler import DatasetHandler

def get_input(prompt, required=True):
    while True:
        value = input(prompt).strip()
        if value or not required:
            return value if value else None
        print("Это поле обязательно для заполнения!")

def get_file_name():
    while True:
        file_name = input("Введите путь к файлу с данными (CSV): ").strip()
        if file_name:
            return file_name
        print("Путь к файлу не может быть пустым!")

def get_expected_columns():
    cols = input("Введите ожидаемые колонки через запятую: ").strip()
    return [col.strip() for col in cols.split(",")]

def get_expected_types(columns):
    print("\nУкажите типы для колонок (доступно: int, float, str, bool):")
    type_map = {
        'int': 'int64',
        'float': 'float64',
        'str': 'object',
        'bool': 'bool'
    }

    return {
        col: type_map[get_input(f"{col} (int/float/str/bool): ").lower()]
        for col in columns
    }

def main():
    file_name = get_file_name()
    expected_columns = get_expected_columns()
    expected_types = get_expected_types(expected_columns)

    handler = DatasetHandler(
        file_name=file_name,
        expected_columns=expected_columns,
        expected_types=expected_types)
    success = handler.process_dataset()

    if success:
        print(f'Чтение датафрейма завершено успешно.')
    else:
        print(f'Возникла ошибка.')

if __name__ == '__main__':
    main()