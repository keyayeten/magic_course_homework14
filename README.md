# magic_course_homework14
Шаблон кода для выполнения финального задания

### Задание

Покройте тестами основные эндпоинты апи https://github.com/keyayeten/test_api .

Примерная стркутура проекта с тестами:

magic_course_homework14/

├── tests/                     # Каталог с тестами

│   ├── ```__init__.py```

│   ├── test_authentication.py # Тесты аутентификации/авторизации

│   ├── test_posts.py

│   ├── test_comments.py

│   ├── fixtures/              # Фикстуры для тестов

│       ├── ```__init__.py```

│       ├── user_fixtures.py   # Фикстуры для пользователей

│       ├── data_fixtures.py   # Фикстуры для тестовых данных

├── conftest.py                # Общие фикстуры и настройки для pytest

├── pytest.ini                 # Конфигурация pytest

├── requirements.txt           # Зависимости проекта

└── README.md                  # Описание тестового проекта