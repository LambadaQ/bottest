import telebot
from telebot import types
#Токен
bot = telebot.TeleBot('1149268072:AAEubXJnEAC_c-gFGlalvGzobeL7z8BzvMY')
#Мейн
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('📚️ Запросить прайс', '📋 Запросить наличие тканей Suerte','📝 Задать вопрос по Suerte')
keyboard1.row('📞 Позвонить в компанию', '👍 Facebook','📷 Instagram')
#Телефоны
keyboard2 = telebot.types.ReplyKeyboardMarkup()
keyboard2.row('Директор','Офис менеджер', 'Клиент-менеджеры')
keyboard2.row('Региональные менеджеры по городам', 'Бренд-менеджеры')
keyboard2.row('🔙 Назад')
#Переход на алфавит
keyboard3 = telebot.types.ReplyKeyboardMarkup()
keyboard3.row('📓 Наличие тканей Suerte без разбивки', '🔠 Наличие с разбивкой по рулонам')
keyboard3.row('🔙 Назад')
#Алфавит Каталогов№1
keyboard4 = telebot.types.ReplyKeyboardMarkup()
keyboard4.row('A', 'B', 'C', 'D','E-F','G-H',)
keyboard4.row('I-G', 'L', 'M', 'N-O', 'P','R','S-T', 'V-W')
keyboard4.row('🔙 Назад',)
#Клиент-менеджеры
keyboard5 = telebot.types.ReplyKeyboardMarkup()
keyboard5.row('Липовая Юлия', 'Бычковская Екатерина',)
keyboard5.row('Некипелая Катя','Пинчук Лилия')
keyboard5.row('🔙 Назад', '🔙 Назад на один шаг')
#Региональные менеджеры по городам
keyboard6 = telebot.types.ReplyKeyboardMarkup()
keyboard6.row('Киев', 'Харьков',)
keyboard6.row('Львов','Днепр', 'Одесса')
keyboard6.row('🔙 Назад', '🔙 Назад на один шаг')
#Бренд-менеджеры
keyboard7 = telebot.types.ReplyKeyboardMarkup()
keyboard7.row('Suerte Elegancia', 'FR One Margo Iliv',)
keyboard7.row('🔙 Назад', '🔙 Назад на один шаг')



@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, '👋 Здраствуйте, вы запустили нашего бота, для дальнейшей навигации в нём, используйте клавиатуру представленую внизу экрана ↘️', reply_markup=keyboard1)
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == '📚️ запросить прайс':
        bot.send_message(message.chat.id, 'Отправьте свой e-mail сюда @TelegramStarinets')
    elif message.text.lower() == '📋 запросить наличие тканей suerte':
        keyboard = types.InlineKeyboardMarkup(row_width=3)
        bot.send_message(message.chat.id, 'Выберете каталог, указав его первую букву ⬇️', reply_markup=keyboard4)

    elif message.text == '📓 Наличие тканей Suerte без разбивки':
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Наличие тканей Suerte без разбивки",
                                                url="https://drive.google.com/file/d/1y14Khdtp6_PHQzCdL4VKO9jSww-_9r5F/view")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Нажмите на кнопку, чтобы перейти на Google Docs.", reply_markup=keyboard)

    elif message.text == '📋 Запросить наличие тканей Suerte':
        keyboard = types.InlineKeyboardMarkup(row_width=3)
        bot.send_message(message.chat.id, 'Выберете каталог, указав его первую букву', reply_markup=keyboard4)

    elif message.text == '📝 Задать вопрос по Suerte':
        keyboard = types.InlineKeyboardMarkup(row_width=3)
        bot.send_message(message.chat.id, 'Отправьте свой e-mail сюда @TelegramStarinets', reply_markup=keyboard)

    elif message.text == '📞 Позвонить в компанию':
        bot.send_message(message.chat.id, 'Выберите нужный вам варинт ⬇️', reply_markup=keyboard2)
        keyboard = types.InlineKeyboardMarkup()

    elif message.text.lower() == '👍 facebook':
        keyboard = types.InlineKeyboardMarkup(row_width=3)
        url_button = types.InlineKeyboardButton(text="Перейти", url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Нажмите на кнопку, чтобы перейти в Facebook.", reply_markup=keyboard)
    elif message.text.lower() == '📷 instagram':
        keyboard = types.InlineKeyboardMarkup(row_width=3)
        url_button = types.InlineKeyboardButton(text="Перейти", url="https://www.instagram.com/suerte.elegancia/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "\n Нажмите на кнопку, чтобы перейти в Instagram.", reply_markup=keyboard)
    elif message.text == '🔙 Назад':
           bot.send_message(message.chat.id, 'Вы вернулись к главному меню', reply_markup=keyboard1)

    elif message.text == '🔙 Назад на один шаг':
           bot.send_message(message.chat.id, 'Вы вернулись к предыдущему меню', reply_markup=keyboard2)

    elif message.text == 'Клиент-менеджеры':
           bot.send_message(message.chat.id, 'Выберите менеджера ⬇️', reply_markup=keyboard5)

    elif message.text == 'Региональные менеджеры по городам':
        bot.send_message(message.chat.id, 'Выберите город, какой вам нужен', reply_markup=keyboard6)

    elif message.text == 'Киев':
        bot.send_message(message.chat.id, 'Турик С. \n '+
        '\n'
                        '📱   +38 (067) 445 32 05 \n'+
                         '\n'
                         '☎️  +38 (044) 545-60-70 \n'+
                         '\n'
                         '📲️  +38 (044) 545-60-80 \n'+
                         '\n',)
        bot.send_message(message.chat.id, 'Шевцова К. \n ' +
                         '\n'
                         '📱   +38 (067) 767-87-86 \n' +
                         '\n'
                         '☎️  +38 (044) 545-60-70 \n' +
                         '\n'
                         '📲️  +38 (093) 767-87-86 \n' +
                         '\n', )
    elif message.text == 'Харьков':
        bot.send_message(message.chat.id, 'Беличенко А. \n '+
        '\n'
                        '📱   +38 (066) 831 89 69  \n'+
                         '\n'
                         '☎️  +38 (067) 502 89 92 \n'+
                         '\n'
                         '📲️  +38 (057) 728 23 14 \n'+
                         '\n',)
    elif message.text == 'Львов':
        bot.send_message(message.chat.id, 'Бакун Ю. \n ' +
                         '\n'
                         '📱   +38 (066) 831 89 69  \n' +
                         '\n'
                         '☎️  +38 (067) 502 89 92 \n' +
                         '\n'
                         '📲️  +38 (057) 728 23 14 \n' +
                         '\n', )
    elif message.text == 'Днепр':
        bot.send_message(message.chat.id, 'Загуба М. \n ' +
                         '\n'
                         '📱   +38 (067) 236-25-24  \n' +
                         '\n'
                         '☎️  +38 (056) 372-09-23 \n' +
                         '\n')
    elif message.text == 'Одесса':
        bot.send_message(message.chat.id, 'Семенова И. \n ' +
                         '\n'
                         '📱   +38 (067) 504 91 09  \n' +
                         '\n' )


    elif message.text == 'Директор':
        bot.send_message(message.chat.id, 'Елена Геннадьевна \n '+
        '\n'
                        '📱   +38 (067) 401 32 03 \n'+
                         '\n'
                         '☎️  +38 (044) 545 60 80 \n'+
                         '\n'
                         '📧 director@daylight.com.ua \n')
        keyboard = types.InlineKeyboardMarkup()

    elif message.text == 'Офис менеджер':
        bot.send_message(message.chat.id, 'Офис менеджер \n ' +
                         '\n'
                         '📱  +38 (044) 545 60 80 \n' +
                         '\n'
                         '📧 office-assistant@daylight.com.ua \n')
        keyboard = types.InlineKeyboardMarkup()

    elif message.text == 'Бычковская Екатерина':
        bot.send_message(message.chat.id, 'Бычковская Екатерина  \n ' +
                         '\n'
                         'Менеджер отдела продаж \n '
                         +
                         '\n'
                         '📱   +38 (067) 327 80 81 \n' +
                         '\n'
                         '☎️ +38 (044) 545 60 80 \n' +
                         '\n'
                         '📧 manager3@daylight.com.ua \n')
        keyboard = types.InlineKeyboardMarkup()

    elif message.text == 'Липовая Юлия':
        bot.send_message(message.chat.id, 'Липовая Юлия  \n ' +
                         '\n'
                         'Менеджер отдела продаж \n '
                         +
                         '\n'
                         '📱  +38 (067) 405 66 84 \n' +
                         '\n'
                         '☎️+38 (044) 545 60 80 \n' +
                         '\n'
                         '📧  manager2@daylight.com.ua \n')
        keyboard = types.InlineKeyboardMarkup()

    elif message.text == 'Некипелая Катя':
        bot.send_message(message.chat.id, 'Некипелая Катя  \n ' +
                         '\n'
                         'Менеджер отдела продаж \n '
                         +
                         '\n'
                         '📱   +38 (067) 564 10 15 \n' +
                         '\n'
                         '☎️+38 (044) 545 60 80 \n' +
                         '\n'
                         '📧  manager4@daylight.com.ua \n')
        keyboard = types.InlineKeyboardMarkup()

    elif message.text == 'Старинец Наталья':
        bot.send_message(message.chat.id, 'Старинец Наталья  \n ' +
                         '\n'
                         'Менеджер отдела продаж \n '
                         +
                         '\n'
                         '📱   +38(067) 405-66-74 \n' +
                         '\n'
                         '☎️@TelegramStarinets \n' +
                         '\n'
                         '📧  manager4@daylight.com.ua \n')
        keyboard = types.InlineKeyboardMarkup()
    elif message.text == 'Пинчук Лилия':
        bot.send_message(message.chat.id, 'Пинчук Лилия \n ' +
                         '\n'
                         'Менеджер отдела продаж \n '
                         +
                         '\n'
                         '📱   +38 (066) 88 623 63 \n' +
                         '\n')
        keyboard = types.InlineKeyboardMarkup()

    elif message.text == 'Бренд-менеджеры':
        bot.send_message(message.chat.id, 'Выберите наиминование бренда ⬇️', reply_markup=keyboard7)
        keyboard = types.InlineKeyboardMarkup()

    elif message.text == 'Suerte Elegancia':
        bot.send_message(message.chat.id, 'Старинец Наталья  \n ' +
                         '\n'
                         'Менеджер отдела продаж \n '
                         +
                         '\n'
                         '📱   +38(067) 405-66-74 \n' +
                         '\n'
                         '☎️@TelegramStarinets \n' +
                         '\n'
                         '📧  manager4@daylight.com.ua \n')
        keyboard = types.InlineKeyboardMarkup()

    elif message.text == 'Suerte Elegancia':
        bot.send_message(message.chat.id, 'Старинец Наталья  \n ' +
                         '\n'
                         'Менеджер отдела продаж \n '
                         +
                         '\n'
                         '📱   +38(067) 405-66-74 \n' +
                         '\n'
                         '☎️@TelegramStarinets \n' +
                         '\n'
                         '📧  manager4@daylight.com.ua \n')
        keyboard = types.InlineKeyboardMarkup()
    elif message.text == 'FR One Margo Iliv':
        bot.send_message(message.chat.id, 'Самотохина Л \n ' +
                         '\n'
                         'Менеджер отдела продаж \n '
                         +
                         '\n'
                         '📱   +38 (066) 88 623 63 \n' +
                         '\n'
                         '☎️+38 (044) 545 60 70 \n' +
        '\n')
        keyboard = types.InlineKeyboardMarkup()

    #Коды букв алфавитов
    elif message.text == 'A':
        keyboard = types.InlineKeyboardMarkup(row_width=3)
        url_button = types.InlineKeyboardButton(text="Ancona discount",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        url_button = types.InlineKeyboardButton(text="Aria",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        url_button = types.InlineKeyboardButton(text="Atlanta",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        url_button = types.InlineKeyboardButton(text="Aurora discount",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Отображены все каталоги, которые начинаются на:  A ", reply_markup=keyboard)

    elif message.text == 'B':
        keyboard = types.InlineKeyboardMarkup(row_width=3)
        url_button = types.InlineKeyboardButton(text="Bavaria",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        url_button = types.InlineKeyboardButton(text="Beatrice",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        url_button = types.InlineKeyboardButton(text="Bergamo",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        url_button = types.InlineKeyboardButton(text="Bianca",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        url_button = types.InlineKeyboardButton(text="Boston",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        url_button = types.InlineKeyboardButton(text="Braveheart",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Отображены все каталоги, которые начинаются на:  B ", reply_markup=keyboard)
    elif message.text == 'C':
        keyboard = types.InlineKeyboardMarkup(row_width=3)
        url_button = types.InlineKeyboardButton(text="Calista",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        url_button = types.InlineKeyboardButton(text="Chalet",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        url_button = types.InlineKeyboardButton(text="Chelsea",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        url_button = types.InlineKeyboardButton(text="Chicago",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        url_button = types.InlineKeyboardButton(text="Convoy",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Отображены все каталоги, которые начинаются на:  С", reply_markup=keyboard)
    elif message.text == 'D':
        keyboard = types.InlineKeyboardMarkup(row_width=3)
        url_button = types.InlineKeyboardButton(text="Dallas dim-out",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        url_button = types.InlineKeyboardButton(text="Diamante discount",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Отображены все каталоги, которые начинаются на:  D", reply_markup=keyboard)
    elif message.text == 'E-F   ':
        keyboard = types.InlineKeyboardMarkup(row_width=3)
        url_button = types.InlineKeyboardButton(text="Elegante",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        url_button = types.InlineKeyboardButton(text="Feliche",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        url_button = types.InlineKeyboardButton(text="Florence",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        url_button = types.InlineKeyboardButton(text="Fuji dim-out",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Отображены все каталоги, которые начинаются на:  С", reply_markup=keyboard)
    elif message.text == 'E-F':
        keyboard = types.InlineKeyboardMarkup(row_width=3)
        url_button = types.InlineKeyboardButton(text="Elegante",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        url_button = types.InlineKeyboardButton(text="Feliche",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        url_button = types.InlineKeyboardButton(text="Florence",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        url_button = types.InlineKeyboardButton(text="Fuji dim-out",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Отображены все каталоги, которые начинаются на:  E-F", reply_markup=keyboard)
    elif message.text == 'G-H':
        keyboard = types.InlineKeyboardMarkup(row_width=3)
        url_button = types.InlineKeyboardButton(text="Gentleman",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        url_button = types.InlineKeyboardButton(text="Georgia discount",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        url_button = types.InlineKeyboardButton(text="Grace",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        url_button = types.InlineKeyboardButton(text="Historia discount",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        url_button = types.InlineKeyboardButton(text="Houston",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Отображены все каталоги, которые начинаются на:  G-H", reply_markup=keyboard)
    elif message.text == 'I-G':
        keyboard = types.InlineKeyboardMarkup(row_width=3)
        url_button = types.InlineKeyboardButton(text="Isabella",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        url_button = types.InlineKeyboardButton(text="Janett",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        url_button = types.InlineKeyboardButton(text="Journal",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Отображены все каталоги, которые начинаются на:  I-G", reply_markup=keyboard)
    elif message.text == 'L':
        keyboard = types.InlineKeyboardMarkup(row_width=3)
        url_button = types.InlineKeyboardButton(text="Lion",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        url_button = types.InlineKeyboardButton(text="Lluvia",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        url_button = types.InlineKeyboardButton(text="Loreto*",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        url_button = types.InlineKeyboardButton(text="Lure trevira",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        url_button = types.InlineKeyboardButton(text="Luxury",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Отображены все каталоги, которые начинаются на:  L", reply_markup=keyboard)
    elif message.text == 'M':
        keyboard = types.InlineKeyboardMarkup(row_width=3)
        url_button = types.InlineKeyboardButton(text="Millenium*",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        url_button = types.InlineKeyboardButton(text="Mist",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        url_button = types.InlineKeyboardButton(text="Montana",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        url_button = types.InlineKeyboardButton(text="Monte Carlo",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        url_button = types.InlineKeyboardButton(text="Monterey",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Отображены все каталоги, которые начинаются на:  L", reply_markup=keyboard)
    elif message.text == 'N-O':
        keyboard = types.InlineKeyboardMarkup(row_width=3)
        url_button = types.InlineKeyboardButton(text="Natural",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        url_button = types.InlineKeyboardButton(text="New York",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        url_button = types.InlineKeyboardButton(text="Novara",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        url_button = types.InlineKeyboardButton(text="Olivia",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Отображены все каталоги, которые начинаются на:  N-O", reply_markup=keyboard)
    elif message.text == 'P':
        keyboard = types.InlineKeyboardMarkup(row_width=3)
        url_button = types.InlineKeyboardButton(text="Paola",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        url_button = types.InlineKeyboardButton(text="Philadelphia*",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        url_button = types.InlineKeyboardButton(text="Polo",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        url_button = types.InlineKeyboardButton(text="Pure Linen",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Отображены все каталоги, которые начинаются на:  P", reply_markup=keyboard)
    elif message.text == 'R':
        keyboard = types.InlineKeyboardMarkup(row_width=3)
        url_button = types.InlineKeyboardButton(text="Ramo*",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        url_button = types.InlineKeyboardButton(text="Reach",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        url_button = types.InlineKeyboardButton(text="Renato*",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        url_button = types.InlineKeyboardButton(text="Reni",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        url_button = types.InlineKeyboardButton(text="Residence",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        url_button = types.InlineKeyboardButton(text="Riviera",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        url_button = types.InlineKeyboardButton(text="Rodos",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Отображены все каталоги, которые начинаются на:  R", reply_markup=keyboard)
    elif message.text == 'S-T':
        keyboard = types.InlineKeyboardMarkup(row_width=3)
        url_button = types.InlineKeyboardButton(text="Shetland",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        url_button = types.InlineKeyboardButton(text="Smart dim-out",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        url_button = types.InlineKeyboardButton(text="Sorrento",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        url_button = types.InlineKeyboardButton(text="Swan",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        url_button = types.InlineKeyboardButton(text="Tiffany",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        url_button = types.InlineKeyboardButton(text="Tokyo",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        url_button = types.InlineKeyboardButton(text="Tweed",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Отображены все каталоги, которые начинаются на:  S-T", reply_markup=keyboard)
    elif message.text == 'V-W':
        keyboard = types.InlineKeyboardMarkup(row_width=3)
        url_button = types.InlineKeyboardButton(text="Velutto",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        url_button = types.InlineKeyboardButton(text="Vera",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        url_button = types.InlineKeyboardButton(text="Verona",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        url_button = types.InlineKeyboardButton(text="Violett",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        url_button = types.InlineKeyboardButton(text="Vito",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        url_button = types.InlineKeyboardButton(text="Vitoria",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        url_button = types.InlineKeyboardButton(text="Wool",
                                                url="https://www.facebook.com/suerte.elegancia/?fref=mentions")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Отображены все каталоги, которые начинаются на:  V-W", reply_markup=keyboard)

@bot.message_handler(commands=['start'])
def send_text(message):
    if message.text:
        bot.send_message(message.chat.id, 'Отправьте свой e-mail сюда @TelegramStarinets')

bot.polling()
