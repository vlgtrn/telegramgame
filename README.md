# Telegram Yaşına Göre Puan Veren Bot

Bu proje, kullanıcının Telegram yaşına göre puan veren bir bot oluşturur. Telegram'daki hesap yaşı hesaplanır ve belirli bir puan verilir.

## Kurulum

1. Bu projeyi klonlayın ya da indirin:
    ```
    git clone https://github.com/kullanici/telegram-game-bot.git
    ```

2. Gerekli bağımlılıkları yükleyin:
    ```
    pip install pyTelegramBotAPI
    ```

3. Botun `config.py` dosyasındaki `API_TOKEN`'ı güncelleyin.

4. Botu çalıştırın:
    ```
    python bot.py
    ```

## Komutlar

- `/start`: Botu başlatır ve tanıtıcı bir mesaj gönderir.
- `/puan`: Kullanıcının Telegram yaşını ve puanını hesaplar.
