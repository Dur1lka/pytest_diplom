# pytest_diplom

### Стек:
-pytest
-selenium
-requests
-allure
-config

### Струткура:
- ./test - тесты
- ./pages - описание страниц
- ./api - хелперы для работы с API
- pytest.ini - маркеры для запуска pytest
- README.md - отчет-инструкция к работе
- config.py - конфигурации
- requirements.txt - зависимости

### Шаги
1. Склонировать проект 'git clone https://github.com/имя_пользователя/
   pytest_ui_api_template.git'
2. Установить зависимости
3. Запустить тесты 'pytest'

### Библиотеки (!)
- pyp install pytest
- pip install selenium
- pip install webdriver-manager

###Инструкция по работе с тестами
##Подготовка:

1.Запускаем VS Code или PyCharm
2.Нажимаем Ctrl+Shift+P (или Cmd+Shift+P на macOS), чтобы открыть командную панель
3.Клонируем репозиторий git clone <ссылка на проект>
4.Создаем и активируем виртуальное окружение python -m venv venv venv\Scripts\activate
5.Устанавливаем зависимости из файла requirements.txt. Команда pip install -r requirements.txt
##Запуск API тестов:

Команда pytest tests/test_api.py --alluredir=./allure_result_api
После завершения тестирования вводим команду allure serve allure_result_api для просмотра отчета о тестировании
##Запуск UI тестов:

Команда pytest tests/test_ui.py --alluredir=./allure_result_ui
После завершения тестирования вводим команду allure serve allure_result_ui для просмотра отчета о тестировании
##Запуск всех тестов:

Команду pytest --alluredir=./allure_result_all
После завершения тестирования вводим команду allure serve allure_result_all для просмотра отчета о тестирован

