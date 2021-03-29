import telebot 
from tele_token import TOKEN
from telebot import types
import json

token = TOKEN

bot = telebot.TeleBot(token)

lists_title = []
with open("my_json_file.json") as json_file_title:
    date = json.load(json_file_title)
    for date1 in date:
        lists_title.append(date1["title"])

lists_description = []
with open("my_json_file.json") as json_file_description:
    date = json.load(json_file_description)
    for date1 in date:
        lists_description.append(date1["description"])

lists_photo = []
with open("my_json_file.json") as json_file_photo:
    date = json.load(json_file_photo)
    for date1 in date:
        lists_photo.append(date1["photo"])

inline_keyboard = types.InlineKeyboardMarkup()

btn1 = types.InlineKeyboardButton(f"1 {lists_title[0]}",callback_data='1')
btn2 = types.InlineKeyboardButton(f"2 {lists_title[1]}",callback_data='2')
btn3 = types.InlineKeyboardButton(f"3 {lists_title[2]}",callback_data='3')
btn4 = types.InlineKeyboardButton(f"4 {lists_title[3]}",callback_data='4')
btn5 = types.InlineKeyboardButton(f"5 {lists_title[4]}",callback_data='5')
btn6 = types.InlineKeyboardButton(f"6 {lists_title[5]}",callback_data='6')
btn7 = types.InlineKeyboardButton(f"7 {lists_title[6]}",callback_data='7')
btn8 = types.InlineKeyboardButton(f"8 {lists_title[7]}",callback_data='8')
btn9 = types.InlineKeyboardButton(f"9 {lists_title[8]}",callback_data='9')
btn10 = types.InlineKeyboardButton(f"10 {lists_title[9]}",callback_data='10')
btn11 = types.InlineKeyboardButton(f"11 {lists_title[10]}",callback_data='11')
btn12 = types.InlineKeyboardButton(f"12 {lists_title[11]}",callback_data='12')
btn13 = types.InlineKeyboardButton(f"13 {lists_title[12]}",callback_data='13')
btn14 = types.InlineKeyboardButton(f"14 {lists_title[13]}",callback_data='14')
btn15 = types.InlineKeyboardButton(f"15 {lists_title[14]}",callback_data='15')
btn16 = types.InlineKeyboardButton(f"16 {lists_title[15]}",callback_data='16')
btn17 = types.InlineKeyboardButton(f"17 {lists_title[16]}",callback_data='17')
btn18 = types.InlineKeyboardButton(f"18 {lists_title[17]}",callback_data='18')
btn19 = types.InlineKeyboardButton(f"19 {lists_title[18]}",callback_data='19')
btn20 = types.InlineKeyboardButton(f"20 {lists_title[19]}",callback_data='20')

inline_keyboard.add(btn1,btn2,btn3,btn4,
                    btn5,btn6,btn7,btn8,
                    btn9,btn10,btn11,btn12,
                    btn13,btn14,btn15,btn16,
                    btn17,btn18,btn19,btn20)


@bot.message_handler(commands=["start"])
def start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id,"выберите обьвление",reply_markup=inline_keyboard)


@bot.callback_query_handler(func=lambda c: True)
def inline(c): 
    if c.data == "1":
        chat_id = c.message.chat.id
        income_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
        k1 = types.KeyboardButton(f'Описание !')
        income_keyboard.add(k1)
        msg = bot.send_message(chat_id,f"Нажмите 'Описание' чтобы увидеть данные!",reply_markup=income_keyboard)
        bot.register_next_step_handler(msg,describe)

    if c.data == "2":
        chat_id = c.message.chat.id
        income_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
        k1 = types.KeyboardButton(f'Описание !')
        income_keyboard.add(k1)
        msg = bot.send_message(chat_id,f"Нажмите описание чтобы увидеть данные!",reply_markup=income_keyboard)
        bot.register_next_step_handler(msg,describe2)

    if c.data == "3":
        chat_id = c.message.chat.id
        income_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
        k1 = types.KeyboardButton(f'Описание !')
        income_keyboard.add(k1)
        msg = bot.send_message(chat_id,f"Нажмите описание чтобы увидеть данные!",reply_markup=income_keyboard)
        bot.register_next_step_handler(msg,describe3)

    if c.data == "4":
        chat_id = c.message.chat.id
        income_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
        k1 = types.KeyboardButton(f'Описание !')
        income_keyboard.add(k1)
        msg = bot.send_message(chat_id,f"Нажмите описание чтобы увидеть данные!",reply_markup=income_keyboard)
        bot.register_next_step_handler(msg,describe4)

    if c.data == "5":
        chat_id = c.message.chat.id
        income_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
        k1 = types.KeyboardButton(f'Описание !')
        income_keyboard.add(k1)
        msg = bot.send_message(chat_id,f"Нажмите описание чтобы увидеть данные!",reply_markup=income_keyboard)
        bot.register_next_step_handler(msg,describe5)
 
    if c.data == "6":
        chat_id = c.message.chat.id
        income_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
        k1 = types.KeyboardButton(f'Описание !')
        income_keyboard.add(k1)
        msg = bot.send_message(chat_id,f"Нажмите описание чтобы увидеть данные!",reply_markup=income_keyboard)
        bot.register_next_step_handler(msg,describe6)

    if c.data == "7":
        chat_id = c.message.chat.id
        income_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
        k1 = types.KeyboardButton(f'Описание !')
        income_keyboard.add(k1)
        msg = bot.send_message(chat_id,f"Нажмите описание чтобы увидеть данные!",reply_markup=income_keyboard)
        bot.register_next_step_handler(msg,describe7)

    if c.data == "8":
        chat_id = c.message.chat.id
        income_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
        k1 = types.KeyboardButton(f'Описание !')
        income_keyboard.add(k1)
        msg = bot.send_message(chat_id,f"Нажмите описание чтобы увидеть данные!",reply_markup=income_keyboard)
        bot.register_next_step_handler(msg,describe8)
 
    if c.data == "9":
        chat_id = c.message.chat.id
        income_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
        k1 = types.KeyboardButton(f'Описание !')
        income_keyboard.add(k1)
        msg = bot.send_message(chat_id,f"Нажмите описание чтобы увидеть данные!",reply_markup=income_keyboard)
        bot.register_next_step_handler(msg,describe9)

    if c.data == "10":
        chat_id = c.message.chat.id
        income_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
        k1 = types.KeyboardButton(f'Описание !')
        income_keyboard.add(k1)
        msg = bot.send_message(chat_id,f"Нажмите описание чтобы увидеть данные!",reply_markup=income_keyboard)
        bot.register_next_step_handler(msg,describe10)
 
    if c.data == "11":
        chat_id = c.message.chat.id
        income_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
        k1 = types.KeyboardButton(f'Описание !')
        income_keyboard.add(k1)
        msg = bot.send_message(chat_id,f"Нажмите описание чтобы увидеть данные!",reply_markup=income_keyboard)
        bot.register_next_step_handler(msg,describe11)
 
    if c.data == "12":
        chat_id = c.message.chat.id
        income_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
        k1 = types.KeyboardButton(f'Описание !')
        income_keyboard.add(k1)
        msg = bot.send_message(chat_id,f"Нажмите описание чтобы увидеть данные!",reply_markup=income_keyboard)
        bot.register_next_step_handler(msg,describe12)

    if c.data == "13":
        chat_id = c.message.chat.id
        income_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
        k1 = types.KeyboardButton(f'Описание !')
        income_keyboard.add(k1)
        msg = bot.send_message(chat_id,f"Нажмите описание чтобы увидеть данные!",reply_markup=income_keyboard)
        bot.register_next_step_handler(msg,describe13)

    if c.data == "14":
        chat_id = c.message.chat.id
        income_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
        k1 = types.KeyboardButton(f'Описание !')
        income_keyboard.add(k1)
        msg = bot.send_message(chat_id,f"Нажмите описание чтобы увидеть данные!",reply_markup=income_keyboard)
        bot.register_next_step_handler(msg,describe14)

    if c.data == "15":
        chat_id = c.message.chat.id
        income_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
        k1 = types.KeyboardButton(f'Описание !')
        income_keyboard.add(k1)
        msg = bot.send_message(chat_id,f"Нажмите описание чтобы увидеть данные!",reply_markup=income_keyboard)
        bot.register_next_step_handler(msg,describe15)

    if c.data == "16":
        chat_id = c.message.chat.id
        income_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
        k1 = types.KeyboardButton(f'Описание !')
        income_keyboard.add(k1)
        msg = bot.send_message(chat_id,f"Нажмите описание чтобы увидеть данные!",reply_markup=income_keyboard)
        bot.register_next_step_handler(msg,describe16)
 
    if c.data == "17":
        chat_id = c.message.chat.id
        income_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
        k1 = types.KeyboardButton(f'Описание !')
        income_keyboard.add(k1)
        msg = bot.send_message(chat_id,f"Нажмите описание чтобы увидеть данные!",reply_markup=income_keyboard)
        bot.register_next_step_handler(msg,describe17)



    if c.data == "18":
        chat_id = c.message.chat.id
        income_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
        k1 = types.KeyboardButton(f'Описание !')
        income_keyboard.add(k1)
        msg = bot.send_message(chat_id,f"Нажмите описание чтобы увидеть данные!",reply_markup=income_keyboard)
        bot.register_next_step_handler(msg,describe18)
 
    if c.data == "19":
        chat_id = c.message.chat.id
        income_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
        k1 = types.KeyboardButton(f'Описание !')
        income_keyboard.add(k1)
        msg = bot.send_message(chat_id,f"Нажмите описание чтобы увидеть данные!",reply_markup=income_keyboard)
        bot.register_next_step_handler(msg,describe19)

    if c.data == "20":
        chat_id = c.message.chat.id
        income_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
        k1 = types.KeyboardButton(f'Описание !')
        income_keyboard.add(k1)
        msg = bot.send_message(chat_id,f"Нажмите описание чтобы увидеть данные!",reply_markup=income_keyboard)
        bot.register_next_step_handler(msg,describe20)

def describe(message):
    chat_id = message.chat.id
    bot.send_message(chat_id,f"{lists_description[0]} {lists_photo[0]}")
    
def describe2(message):
    chat_id = message.chat.id
    bot.send_message(chat_id,f"{lists_description[1]} {lists_photo[1]}")

def describe3(message):
    chat_id = message.chat.id
    bot.send_message(chat_id,f"{lists_description[2]} {lists_photo[2]}")

def describe4(message):
    chat_id = message.chat.id
    bot.send_message(chat_id,f"{lists_description[3]} {lists_photo[3]}")

def describe5(message):
    chat_id = message.chat.id
    bot.send_message(chat_id,f"{lists_description[4]} {lists_photo[4]}")

def describe6(message):
    chat_id = message.chat.id
    bot.send_message(chat_id,f"{lists_description[5]} {lists_photo[5]}")

def describe7(message):
    chat_id = message.chat.id
    bot.send_message(chat_id,f"{lists_description[6]} {lists_photo[6]}")

def describe8(message):
    chat_id = message.chat.id
    bot.send_message(chat_id,f"{lists_description[7]} {lists_photo[7]}")

def describe9(message):
    chat_id = message.chat.id
    bot.send_message(chat_id,f"{lists_description[8]} {lists_photo[8]}")

def describe10(message):
    chat_id = message.chat.id
    bot.send_message(chat_id,f"{lists_description[9]} {lists_photo[9]}")

def describe11(message):
    chat_id = message.chat.id
    bot.send_message(chat_id,f"{lists_description[10]} {lists_photo[10]}")

def describe12(message):
    chat_id = message.chat.id
    bot.send_message(chat_id,f"{lists_description[11]} {lists_photo[11]}")

def describe13(message):
    chat_id = message.chat.id
    bot.send_message(chat_id,f"{lists_description[12]} {lists_photo[12]}")

def describe14(message):
    chat_id = message.chat.id
    bot.send_message(chat_id,f"{lists_description[13]} {lists_photo[13]}")

def describe15(message):
    chat_id = message.chat.id
    bot.send_message(chat_id,f"{lists_description[14]} {lists_photo[14]}")

def describe16(message):
    chat_id = message.chat.id
    bot.send_message(chat_id,f"{lists_description[15]} {lists_photo[15]}")

def describe17(message):
    chat_id = message.chat.id
    bot.send_message(chat_id,f"{lists_description[16]} {lists_photo[16]}")

def describe18(message):
    chat_id = message.chat.id
    bot.send_message(chat_id,f"{lists_description[17]} {lists_photo[17]}")

def describe19(message):
    chat_id = message.chat.id
    bot.send_message(chat_id,f"{lists_description[18]} {lists_photo[18]}")

def describe20(message):
    chat_id = message.chat.id
    bot.send_message(chat_id,f"{lists_description[19]} {lists_photo[19]}")

bot.polling()