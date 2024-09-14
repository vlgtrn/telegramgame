# bot.py
import telebot
from config import API_TOKEN
from game_logic import calculate_age_and_points

# Botu başlatıyoruz
bot = telebot.TeleBot(API_TOKEN)

# /start komutunu ele alma
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Merhaba! Telegram yaşınıza göre puan kazanacaksınız! /puan komutunu kullanın.")

# Kullanıcının Telegram yaşına göre puan hesaplama
@bot.message_handler(commands=['puan'])
def send_points(message):
    user = message.from_user

    # Kullanıcının Telegram ID'sine göre hesaplama yapıyoruz
    account_creation_date = user.id  # Telegram ID'si kullanıcının oluşturulma tarihi gibidir (UNIX timestamp)
    
    # Yaş ve puan hesaplama
    age_in_years, points = calculate_age_and_points(user.id, account_creation_date)
    
    # Yanıt gönder
    response = f"Sizin Telegram yaşınız {age_in_years} yıl. Kazandığınız puan: {points}."
    bot.reply_to(message, response)

# Botu çalıştır
bot.polling()
