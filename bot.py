import telebot
import random

bot = telebot.TeleBot("7816112590:AAGZy5TL-QoHls9iUdqxlRWcqmKFsqTnYvc")

quotes = [
    "Believe in yourself and all that you are.",
    "Your only limit is your mind.",
    "Push yourself because no one else is going to do it for you.",
    "Great things never come from comfort zones.",
    "Dream it. Wish it. Do it.",
    "Success doesn't just find you. You have to go out and get it.",
    "The harder you work for something, the greater you’ll feel when you achieve it.",
    "Don’t watch the clock; do what it does. Keep going.",
    "Sometimes later becomes never. Do it now.",
    "Little things make big days."
]

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Welcome! Type /motivate to get a motivational quote today.")

@bot.message_handler(commands=['motivate'])
def motivate(message):
    quote = random.choice(quotes)
    bot.reply_to(message, quote)

print("Bot is running...")
bot.polling(non_stop=True)
