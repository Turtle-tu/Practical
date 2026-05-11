import os
import telebot
from utils import get_daily_horoscope

BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start', 'horoscope'])
def sign_handler(message):
    text = (
        "Напиши свой знак зодиака на русском языке.\n"
        "Например: *Овен, Телец, Близнецы, Рак, Лев, Дева, Весы, Скорпион, Стрелец, Козерог, Водолей* или *Рыбы*."
    )
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, day_handler)


def day_handler(message):
    sign = message.text
    text = (
        "На какой день прогноз?\n"
        "Напиши: *Сегодня*, *Завтра*, *Вчера* или дату в формате *ДД-ММ-ГГ* (например: 20-05-26)"
    )
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, fetch_horoscope, sign)


def fetch_horoscope(message, sign):
    day = message.text
    horoscope = get_daily_horoscope(sign, day)
    data = horoscope["data"]

    if data['date'] == "ошибка":
        bot.send_message(message.chat.id, data['horoscope_data'])
    else:
        horoscope_message = (
            f"🔮 *Гороскоп: {sign.capitalize()}*\n"
            f"📅 *Дата:* {data['date']}\n\n"
            f"✨ {data['horoscope_data']}"
        )
        bot.send_message(message.chat.id, horoscope_message, parse_mode="Markdown")


if __name__ == "__main__":
    print("Бот запущен...")
    bot.infinity_polling()
