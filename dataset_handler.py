import os
import pandas as pd

class DatasetHandler:
    def __init__(self, file_name: str, expected_columns: list = None, expected_types: dict = None):
        self.file_name = file_name
        self.expected_columns = expected_columns
        self.expected_dtypes = expected_types if expected_types is not None else {}
        self.dataset = None

    def check_file_exists(self):
        if not os.path.exists(self.file_name):
            raise FileNotFoundError(f'Ошибка: Файл {self.file_name} не был найден.')
        
    def check_file_not_empty(self):
        if os.path.getsize(self.file_name) == 0:
            raise ValueError(f'ошибка: Файл {self.file_name} пуст.')
        
    def load_dataset(self):
        try:
            self.dataset = pd.read_csv(self.file_name)
        except pd.errors.EmptyDataError:
            raise ValueError(f'Ошибка: Файл {self.file_name} не содержит данных.')
        except pd.errors.ParserError:
            raise ValueError(f'Ошибка: Неверный формат файла {self.file_name}. Ожидается CSV.')
        
    def check_columns(self):
        if self.expected_columns is None:
            return
        missing_columns = [col for col in self.expected_columns
            if col not in self.dataset.columns]
        if missing_columns:
            raise ValueError(f'Ошибка: Название столбцов не совпадают.\n'
                f'Ожидаемые: {self.expected_columns}\n'
                f'Фактическе: {list(self.dataset.columns)}.')
    
    def check_column_types(self):
        """Проверяет соответствие типов данных в колонках."""
        if not self.expected_dtypes:
            return

        type_errors = []
        
        for col, expected_type in self.expected_dtypes.items():
            if col not in self.dataset.columns:
                continue
                
            actual_type = self.dataset[col].dtype
            if not pd.api.types.is_dtype_equal(actual_type, expected_type):
                type_errors.append(
                    f"В столбце '{col}' тип данных не соответствует ожидаемому. "
                    f"Ожидается: {expected_type}, Фактически: {actual_type}"
                )
        
        if type_errors:
            raise TypeError("\n".join(type_errors))
        
    def process_dataset(self):
        try: 
            print(f'Попытка обработать файл {self.file_name}.')

            self.check_file_exists()
            self.check_file_not_empty()
            self.load_dataset()
            self.check_columns()
            self.check_column_types

            print(f'Обработка файла {self.file_name} завершена успешно.')
        except Exception as e:
            print(f'{str(e)}')
            return False
        
        return True