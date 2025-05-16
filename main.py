from dataset_handler import DatasetHandler

def main():
    file_name = input('Введите название файла, который хотите проверить (Пример: data.csv): ')
    handler = DatasetHandler(file_name)
    handler.check_file()
    
if __name__ == '__main__':
    main()