# onliner.by UI Автотесты

Автоматизированные UI-тесты для [onliner.by](https://www.onliner.by/) с использованием Selenium WebDriver и Page Object Model.

## 📌 О проекте

Проект содержит автоматические тесты для проверки функциональности крупнейшего белорусского портала onliner.by.  
Тесты написаны на **Python + pytest** и используют **Selenium WebDriver** для взаимодействия с браузером.  
Основной тест проверяет сценарий поиска товара в каталоге и перехода на страницу продукта.

## 🛠 Технологии

* **Python 3.11+**
* **pytest** — тестовый фреймворк
* **Selenium WebDriver** — управление браузером
* **Page Object Model** — структурирование кода
* **Chrome/Chromium** — целевой браузер (может быть адаптирован под другие)

## 🚀 Установка и запуск

### 1. Клонируйте репозиторий
```bash
git clone https://github.com/Waspish/onliner.git
cd onliner
```

### 2. Создайте виртуальное окружение
```bash
python -m venv .venv
# Активация:
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
```

### 3. Установите зависимости
```bash
pip install -r requirements.txt
```

Убедитесь, что у вас установлен **Google Chrome** (или другой браузер, если вы измените конфигурацию).  
Драйвер (`chromedriver`) автоматически подхватится, если он есть в `PATH`. При необходимости установите его вручную или используйте `webdriver-manager`.

### 4. Запустите тест
```bash
pytest tests/test_search_and_select_product_in_catalog.py -v
```

Если вы хотите видеть браузер (не headless), закомментируйте строку `chrome_options.add_argument('--headless')` в `conftest.py`.

## 📁 Структура проекта

```
.
├── .github/                         # (не используется, заготовка)
├── pages/                           # Page Object Model
│   ├── __init__.py
│   ├── base/                        # базовые классы (локаторы, общие методы)
│   ├── catalog/                     # страницы каталога
│   │   ├── catalog_page.py
│   │   └── product_details_page.py
│   └── main_site/                   # главная страница
│       └── home_page.py
├── tests/                           # тесты
│   ├── __init__.py
│   └── test_search_and_select_product_in_catalog.py  # основной тест
├── utils/                           # утилиты
│   ├── __init__.py
│   ├── screenshot.py               # скриншоты при падении теста
│   └── wait_utils.py               # кастомные ожидания
├── conftest.py                      # фикстуры (driver, headless, скриншоты)
├── requirements.txt
└── README.md
```

## ⚙️ Особенности

* **Headless-режим** — по умолчанию браузер запускается в фоне (без GUI).  
  Для отладки можно отключить, убрав флаг `--headless` в `conftest.py`.
* **Скриншоты** — при падении теста автоматически делается скриншот (функция `take_screenshot`).
* **Ожидания** — кастомные ожидания в `utils/wait_utils.py` (например, ожидание видимости элемента).
* **CI/CD** — в коммитах упоминается подготовка для Jenkins (параметризированная сборка, headless-опции).

## 🧪 Что делает основной тест?

`test_search_and_select_product_in_catalog.py`:

1. Открывает главную страницу onliner.by.
2. Переходит в каталог.
3. Выполняет поиск по ключевому слову (например, "iphone").
4. Выбирает третий продукт из результатов поиска.
5. Переходит на страницу продукта.
6. Сравнивает заголовок и ссылку продукта с сохранёнными из результатов поиска.
