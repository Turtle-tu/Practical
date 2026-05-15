import os
import csv
import logging
from datetime import datetime

import telebot
from telebot import types
from dotenv import load_dotenv

# =========================
# CONFIG
# =========================

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)

# =========================
# LOGGING
# =========================

logging.basicConfig(
    filename='bot.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

# =========================
# USER HISTORY
# =========================

user_history = {}

# =========================
# START MENU
# =========================

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

# =========================
# CALLBACK BUTTONS
# =========================

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

# =========================
# HELP
# =========================

@bot.message_handler(commands=['help'])
def help_command(message):

    text = (
        "🆘 *Помощь*\n\n"
        "📸 Отправьте изображение груза.\n\n"
        "Поддерживаются:\n"
        "• JPG\n"
        "• PNG\n"
        "• Фото паллет"
    )

    bot.send_message(
        message.chat.id,
        text,
        parse_mode="Markdown"
    )

# =========================
# STATUS COMMAND
# =========================

@bot.message_handler(commands=['status'])
def status(message):

    text = (
        "📊 *Система активна*\n\n"
        "🟢 Telegram Bot\n"
        "🟢 Docker Container"
    )

    bot.send_message(
        message.chat.id,
        text,
        parse_mode="Markdown"
    )

# =========================
# HISTORY COMMAND
# =========================

@bot.message_handler(commands=['history'])
def history(message):

    history_list = user_history.get(message.chat.id)

    if not history_list:

        bot.send_message(
            message.chat.id,
            "📭 История пуста"
        )

        return

    text = "🕘 *История загрузок:*\n\n"

    for i, item in enumerate(history_list[-5:], start=1):
        text += f"{i}. {item}\n"

    bot.send_message(
        message.chat.id,
        text,
        parse_mode="Markdown"
    )

# =========================
# REPORT COMMAND
# =========================

@bot.message_handler(commands=['report'])
def report(message):

    if os.path.exists("report.csv"):

        with open("report.csv", "rb") as file:

            bot.send_document(
                message.chat.id,
                file
            )

    else:

        bot.send_message(
            message.chat.id,
            "❌ Отчёт отсутствует"
        )

# =========================
# EXPORT HTML
# =========================

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

# =========================
# PHOTO HANDLER
# =========================

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

        with open(filepath, 'wb') as new_file:
            new_file.write(downloaded_file)

        # =========================
        # SAVE USER HISTORY
        # =========================

        if message.chat.id not in user_history:
            user_history[message.chat.id] = []

        user_history[message.chat.id].append(filepath)

        # =========================
        # SAVE CSV REPORT
        # =========================

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

        # =========================
        # SEND PHOTO BACK
        # =========================

        with open(filepath, 'rb') as photo_file:

            bot.send_photo(
                message.chat.id,
                photo_file,
                caption="📸 Загруженное изображение"
            )

        logging.info(
            f"User {message.chat.id} uploaded image {filename}"
        )

    except Exception as e:

        logging.error(str(e))

        bot.send_message(
            message.chat.id,
            f"❌ Ошибка обработки:\n{e}"
        )

# =========================
# UNKNOWN COMMAND
# =========================

@bot.message_handler(func=lambda message: True)
def unknown(message):

    bot.send_message(
        message.chat.id,
        "❓ Неизвестная команда.\nИспользуйте /help"
    )

# =========================
# RUN BOT
# =========================

if __name__ == "__main__":

    print("✅ Бот запущен")

    bot.infinity_polling()
