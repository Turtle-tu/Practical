# Техническое руководство: Разработка Telegram-бота для загрузки фотографий грузов на Python

> **Цель документа:** Пошаговое руководство по созданию Telegram-бота для загрузки, хранения и обработки фотографий грузов. Документ описывает архитектуру проекта, реализацию функционала и процесс запуска системы.

---

# 1. Исследование предметной области

## Ключевые вопросы исследования

### 1. Какие компоненты обязательны для Telegram-бота проекта?

* Подключение к Telegram Bot API
* Система обработки пользовательских команд
* Хранение токена в переменных окружения
* Отправка форматированных сообщений
* Система загрузки изображений
* Сохранение файлов на сервере
* Ведение истории загрузок
* Формирование CSV-отчётов
* Поддержка Markdown-разметки
* Бесконечный цикл polling для работы бота

### 2. Почему выбран pyTelegramBotAPI (telebot)?

* Простота использования и минимальный объём кода
* Быстрая настройка команд и обработчиков
* Поддержка Markdown и HTML-разметки
* Большое количество примеров и документации
* Подходит для учебных и демонстрационных проектов
* Совместимость с Python 3.10+

### 3. Анализ аналогов

Изучены Telegram-боты для хранения и обработки пользовательских изображений. Выделены требования:

* Быстрая загрузка фотографий
* Простота интерфейса
* Поддержка мобильных устройств
* Возможность хранения истории загрузок
* Экспорт информации в CSV

---

## Сравнение библиотек для Telegram-ботов

| Библиотека                 | Сложность | Производительность | Гибкость | Подходит для проекта |
| -------------------------- | --------- | ------------------ | -------- | -------------------- |
| pyTelegramBotAPI (telebot) | Низкая    | Высокая            | Средняя  | Да                   |

---

# 2. Подготовка окружения

## Требования

* Python 3.10 или выше
* Telegram-аккаунт
* Токен Telegram-бота от BotFather
* Git для контроля версий (рекомендуется)

---

## Установка библиотек

```bash
pip install pyTelegramBotAPI
pip install python-dotenv
```

---

## Проверка установки

```bash
python --version
pip show pyTelegramBotAPI
pip show python-dotenv
```

---

## Создание файла `.env`

```env
BOT_TOKEN=your_telegram_bot_token
```

> **Примечание:** Никогда не публикуйте токен бота в открытом доступе или GitHub-репозитории.

---

# 3. Пошаговая реализация

## Шаг 1: Подключение библиотек и загрузка токена

```python
import os
import csv
import logging
from datetime import datetime

import telebot
from telebot import types
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)

```

---

## Шаг 2: Создание стартового меню

```python
@bot.message_handler(commands=['start'])
def start(message):

    markup = types.InlineKeyboardMarkup(row_width=2)

    btn1 = types.InlineKeyboardButton(
        "👥 Участники",
        callback_data="members"
    )

    btn2 = types.InlineKeyboardButton(
        "📝 Описание",
        callback_data="description"
    )

    btn3 = types.InlineKeyboardButton(
        "🎯 Цели",
        callback_data="goal"
    )

    btn4 = types.InlineKeyboardButton(
        "🛠 Технологии",
        callback_data="stack"
    )

    btn5 = types.InlineKeyboardButton(
        "📊 Статус",
        callback_data="status"
    )

    btn6 = types.InlineKeyboardButton(
        "📁 История",
        callback_data="history"
    )

    btn7 = types.InlineKeyboardButton(
        "📄 Отчёт CSV",
        callback_data="report"
    )

    btn8 = types.InlineKeyboardButton(
        "🔗 GitHub",
        url="https://github.com/Evenmurmur/AIS"
    )

    markup.add(
        btn1, btn2,
        btn3, btn4,
        btn5, btn6,
        btn7, btn8
    )

    text = (
        "👋 *Добро пожаловать в систему загрузки грузов!*\n\n"
        "Выберите нужный раздел:"
    )

    bot.send_message(
        message.chat.id,
        text,
        parse_mode="Markdown",
        reply_markup=markup
    )
```

### Назначение

* Отображение стартового интерфейса
* Вывод Inline-кнопок
* Навигация по разделам проекта

---

## Шаг 3: Реализация callback-кнопок

```python
@bot.callback_query_handler(func=lambda call: True)
def callback(call):

    if call.data == "members":

        text = (
            "👥 *Список участников проекта:*\n\n"
            "1. *Алиханов Богдан Тагирович* (241-333)\n2. *Алхедеров Омар* (241-337)\n"
            "3. *Бондаренко Кирилл Андреевич* (241-131)\n4. *Бортникова Дарина Артуровна* (241-336)\n"
            "5. *Гильдеева Виктория Сергеевна* (251-333)\n6. *Грехова Дарья Кирилловна* (251-334)\n"
            "7. *Гылычджанова Боссан* (251-622)\n8. *Дубинкин Антон Владимирович* (251-339)\n"
            "9. *Коваль Александр Евгеньевич* (251-331)\n10. *Леонтьев Александр Александрович* (251-331)\n"
            "11. *Майкова Елизавета Анатольевна* (251-334)\n12. *Мокшин Кирилл Александрович* (241-132)\n"
            "13. *Останин Платон Валерьевич* (251-336)\n14. *Островерхова Елена Олеговна* (251-621)\n"
            "15. *Пинчук Ренат Сергеевич* (241-132)\n16. *Полковникова Арина Александровна* (251-621)\n"
            "17. *Сулейманов Эмиль Шамилевич* (241-132)\n18. *Федоров Иван Сергеевич* (251-333)\n"
            "19. *Хомидов Дилшоджон Шерзодович* (251-337)\n20. *Хоруженко Дмитрий Андреевич* (251-337)"
        )

        bot.send_message(
            call.message.chat.id,
            text,
            parse_mode="Markdown"
        )

    elif call.data == "description":

        text = (
            "📝 *Суть проекта заключается в том, что в прокте необходимо настроить: *\n\n"
            "Использование нейронной сети для определения объёма в определенной зоне склада позволит:\n\n"
            "• *Контроль соответствия объема груза перед погрузкой*: Приложение позволит точно определить объем партии груза непосредственно перед помещением в транспортное средство.\n\n"
            "• *Оптимизация использования грузового пространства*: Автоматическое определение объема помогает рационально распределить груз в кузове.\n\n"
            "• *Повышение скорости и точности погрузочных работ*: Использование системы исключает задержки и человеческие ошибки."
        )

        bot.send_message(
            call.message.chat.id,
            text,
            parse_mode="Markdown"
        )

    elif call.data == "goal":

        text = (
            "🎯 *Цели проекта - нужно устранить следующее: *\n\n"
            "• *Низкая точность и субъективность*: Визуальная оценка подвержена значительным погрешностям и субъективному мнению.\n\n"
            "• *Нерациональное использование транспорта*: Ошибки в объеме приводят к неполной загрузке или перегрузу.\n\n"
            "• *Отсутствие объективного контроля*: Процесс не оставляет данных для аудита и разбора ошибок."
        )

        bot.send_message(
            call.message.chat.id,
            text,
            parse_mode="Markdown"
        )

    elif call.data == "stack":

        text = (
            "🛠 *Стек технологий:*\n\n"
            "• Python\n"
            "• Telegram Bot API\n"
            "• *OpenCV*: обработка изображений и видео\n"
            "• *YOLOv8*: модель детекции объектов\n"
            "• CSV\n"
            "• Docker"
        )

        bot.send_message(
            call.message.chat.id,
            text,
            parse_mode="Markdown"
        )

    elif call.data == "status":

        text = (
            "📊 *Статус системы*\n\n"
            "🟢 Telegram Bot\n"
            "🟢 Docker\n\n"
            "Система работает стабильно."
        )

        bot.send_message(
            call.message.chat.id,
            text,
            parse_mode="Markdown"
        )

    elif call.data == "history":

        history_list = user_history.get(call.message.chat.id)

        if not history_list:

            bot.send_message(
                call.message.chat.id,
                "📭 История загрузок пуста"
            )

            return

        text = "🕘 *Последние загрузки:*\n\n"

        for i, item in enumerate(history_list[-5:], start=1):
            text += f"{i}. {item}\n"

        bot.send_message(
            call.message.chat.id,
            text,
            parse_mode="Markdown"
        )

    elif call.data == "report":

        if os.path.exists("report.csv"):

            with open("report.csv", "rb") as file:

                bot.send_document(
                    call.message.chat.id,
                    file
                )

        else:

            bot.send_message(
                call.message.chat.id,
                "❌ CSV отчёт пока отсутствует"
            )

```

### Назначение обработчика

* Обработка нажатий на кнопки
* Формирование текста ответа
* Отправка информации пользователю

---

## Шаг 4: Реализация загрузки фотографий

```python
@bot.message_handler(content_types=['photo'])
def handle_photo(message):

    try:

        bot.send_message(
            message.chat.id,
            "📥 Фото получено."
        )

        photo = message.photo[-1]

        file_info = bot.get_file(photo.file_id)

        downloaded_file = bot.download_file(
            file_info.file_path
        )

        filename = f"{datetime.now().timestamp()}.jpg"

        filepath = os.path.join(
            UPLOAD_DIR,
            filename
        )
```

### Возможности

* Получение фотографий через Telegram
* Скачивание файлов с серверов Telegram
* Сохранение изображений в папку `uploads`
* Ведение истории загрузок
* Формирование CSV-отчёта
* Отправка изображения обратно пользователю

---

## Шаг 5: Сохранение фотографий

```python
with open(filepath, 'wb') as new_file:
    new_file.write(downloaded_file)
```

### Технические детали

* Изображения сохраняются локально
* Имя файла формируется автоматически
* Используется timestamp для уникальности имени

---

## Шаг 6: Формирование CSV-отчёта

```python
 with open(
            "report.csv",
            "a",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                datetime.now(),
                message.chat.id
            ])
```

### Назначение

* Сохранение информации о загрузках
* Фиксация даты и ID пользователя
* Подготовка отчёта для дальнейшего анализа

---

## Шаг 7: Отправка сообщений пользователю

```python
bot.send_message(
    message.chat.id,
    text,
    parse_mode="Markdown"
)
```

### Технические детали

* `message.chat.id` определяет получателя
* `parse_mode="Markdown"` включает форматирование
* Бот отвечает в том же чате, где получил сообщение

---

## Шаг 8: Запуск бота

```python
if __name__ == "__main__":
    print("✅ Бот запущен")
    bot.infinity_polling()
```

### Назначение

* Проверка запуска файла напрямую
* Вывод сообщения в консоль
* Бесконечный цикл обработки сообщений

---

# 4. Архитектура приложения

## Структура Telegram-бота

```text
TelegramProjectBot
├── Импорт библиотек
│
├── Конфигурация
│   ├── .env
│   ├── BOT_TOKEN
│   └── uploads/
│
├── Обработчики команд
│   ├── /start
│   ├── /help
│   ├── /status
│   ├── /history
│   └── /report
│
├── Callback-кнопки
│
├── PHOTO HANDLER
│   ├── Получение фото
│   ├── Сохранение файла
│   ├── CSV отчёт
│   └── История пользователя
│
└── bot.infinity_polling()
```

---

## Диаграмма последовательности: Обработка фотографии

```text
Пользователь -> Telegram: Отправка фотографии
Telegram -> Bot API: Передача изображения
Bot API -> TelegramProjectBot: message object
TelegramProjectBot -> handle_photo(): Обработка файла
handle_photo() -> uploads/: Сохранение изображения
handle_photo() -> report.csv: Запись информации
TelegramProjectBot -> Bot API: send_photo()
Bot API -> Пользователь: Возврат изображения
```

---

# 5. Ключевые модификации

## Модификация 1: Система обработки команд

### Задача

Обеспечить быстрый доступ к разделам информации через Telegram-кнопки и команды.

### Реализация

```python
@bot.message_handler(commands=['start'])
def start(message):
```

### Технические детали

* Используются Inline-кнопки
* Реализована обработка callback-запросов
* Поддерживается расширение функционала

---

## Модификация 2: Использование Markdown-разметки

### Задача

Сделать сообщения более читаемыми и структурированными.

### Реализация

```python
bot.send_message(
    message.chat.id,
    text,
    parse_mode="Markdown"
)
```

### Технические детали

* Жирный текст выделяется через `*текст*`
* Поддерживаются эмодзи Unicode
* Telegram автоматически форматирует сообщение

---

## Модификация 3: Хранение токена через `.env`

### Задача

Повысить безопасность хранения конфиденциальных данных.

### Реализация

```python
from dotenv import load_dotenv
load_dotenv()

bot = telebot.TeleBot(os.getenv('BOT_TOKEN'))
```

### Технические детали

* Токен не хранится напрямую в коде
* Используется переменная окружения
* Исключается случайная публикация токена

---

## Модификация 4: Обработка фотографий

### Назначение

Бот принимает изображения от пользователей, сохраняет их в папку uploads и фиксирует информацию в CSV-файле.

### Реализация

```python
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
```

### Возможности

* Получение фотографий через Telegram
* Сохранение файлов на сервере
* Ведение истории загрузок
* Формирование CSV-отчёта
* Отправка изображения обратно пользователю

---

## Модификация 5: Экспорт HTML-отчёта

### Назначение

Система позволяет автоматически формировать HTML-отчёт со списком загрузок пользователей.

```python
@bot.message_handler(commands=['export_html'])
def export_html(message):

    if not os.path.exists("report.csv"):

        bot.send_message(
            message.chat.id,
            "❌ CSV файл отсутствует"
        )

        return

    html_content = """
    <html>
    <head>
        <meta charset='utf-8'>
        <title>Отчёт</title>
    </head>
    <body>
        <h1>Отчёт по загрузкам</h1>
        <table border='1' cellpadding='5'>
            <tr>
                <th>Дата</th>
                <th>User ID</th>
            </tr>
    """

    with open(
        "report.csv",
        "r",
        encoding="utf-8"
    ) as file:

        reader = csv.reader(file)

        for row in reader:

            html_content += f"""
            <tr>
                <td>{row[0]}</td>
                <td>{row[1]}</td>
            </tr>
            """

    html_content += """
        </table>
    </body>
    </html>
    """

    with open(
        "report.html",
        "w",
        encoding="utf-8"
    ) as html_file:

        html_file.write(html_content)

    with open("report.html", "rb") as file:

        bot.send_document(
            message.chat.id,
            file
        )
```

## Возможности

* Автоматическое создание HTML-файла
* Табличное отображение данных
* Экспорт истории загрузок
* Отправка HTML-файла пользователю

# 6. Дополнительные инструменты

## Добавление новых команд

Для расширения функционала можно добавить команды:

* `/contacts` — контакты команды
* `/help` — список всех команд
* `/news` — новости проекта
* `/demo` — ссылка на демонстрацию

---

## Поддержка кнопок Telegram

Пример клавиатуры:

```python
from telebot import types

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup.add("/history", "/report")

bot.send_message(message.chat.id, "Выберите команду:", reply_markup=markup)
```

---

## Логирование действий

```python
logging.info(
    f"User {message.chat.id} uploaded image"
)
```

Позволяет отслеживать активность пользователей.

---

# 7. Тестирование и запуск

## Инструкция по запуску

```bash
git clone <repository-url>
cd telegram-project-bot
python main.py
```

---

## Чек-лист функционального тестирования

* [ ] Бот запускается без ошибок
* [ ] Команда `/start` отображает меню
* [ ] Кнопки работают корректно
* [ ] Бот принимает фотографии
* [ ] Фото сохраняются в uploads
* [ ] CSV отчёт формируется корректно
* [ ] История загрузок отображается
* [ ] Markdown-разметка отображается корректно
* [ ] `.env` корректно загружается
* [ ] Бот отвечает без задержек

---

## Известные ограничения

* Отсутствует база данных
* Нет системы авторизации пользователей
* Бот работает только в режиме polling
* Нет обработки ошибок Telegram API
* CSV используется вместо базы данных
* Отсутствует анализ изображений

---

# 8. Хронология работы и индивидуальные планы

## Этапы реализации

| Период        | Задача                                 | Результат                    |
| ------------- | -------------------------------------- | ---------------------------- |
| 03.02 – 15.02 | Исследование Telegram Bot API          | Изучение библиотеки telebot  |
| 16.02 – 01.03 | Настройка окружения и подключение бота | Рабочий шаблон проекта       |
| 02.03 – 20.03 | Реализация команд и логики             | Полностью рабочий бот        |
| 21.03 – 15.04 | Реализация загрузки фото               | Система хранения изображений |
| 16.04 – 12.05 | Подготовка документации                | Готовый отчёт и код          |

---

## Индивидуальные планы участников

| Участник                     | Роль                   | Ключевые задачи                                 |
| ---------------------------- | ---------------------- | ----------------------------------------------- |
| Гильдеева Виктория Сергеевна | Ведущий разработчик    | Реализация Telegram-бота, обработка изображений |
| Федоров Иван Сергеевич       | Аналитик / Тестировщик | Тестирование функционала, документация          |

---

# 9. Полезные ресурсы

1. [https://pytba.readthedocs.io/](https://pytba.readthedocs.io/)
2. [https://core.telegram.org/bots/api](https://core.telegram.org/bots/api)
3. [https://pypi.org/project/python-dotenv/](https://pypi.org/project/python-dotenv/)
4. [https://docs.python.org/3/](https://docs.python.org/3/)
5. [https://git-scm.com/doc](https://git-scm.com/doc)

---

# 10. Остальная информация

Проект разработан в рамках учебной проектной практики. Исходный код предоставляется для ознакомления и внутреннего использования командой проекта.

**Контактное лицо:** Семенова Валерия Валерьевна

**Организация-партнёр:** Автоматизированная информационная система для транспортной компании
