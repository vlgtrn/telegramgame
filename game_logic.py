# game_logic.py
from datetime import datetime

# Telegram yaşına göre puan hesaplama
def calculate_age_and_points(user_id, account_creation_date):
    # Şu anki zaman
    now = datetime.now()

    # Account creation date (Unix timestamp'i normal zamana çeviriyoruz)
    account_creation = datetime.utcfromtimestamp(account_creation_date)

    # Kullanıcının Telegram'daki süresi (yıl olarak)
    age_in_years = (now - account_creation).days // 365

    # Puanlama sistemi
    if age_in_years < 1:
        points = 10
    elif 1 <= age_in_years < 3:
        points = 50
    else:
        points = 100

    return age_in_years, points
