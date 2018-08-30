import telebot
import requests
import pyowm

TOKEN = '587300436:AAHHx7mrfvwvruPXnjSYC6zdOlzyADwu-iM'

bot = telebot.TeleBot(TOKEN)
user = bot.get_me()
@bot.message_handler(content_types=["text"])
def send_massage(message):
    if 'График' in message.text:
        photo = open('ret.jpg','rb')
        bot.send_photo(message.chat.id, photo)
    elif 'Погода' in message.text:
        owm = pyowm.OWM('99f729b4e3f725e19b776819d24b3ad4')
        observation = owm.weather_at_place('Kyiv')
        w = observation.get_weather()
        temperature = w.get_temperature('celsius')
        bot.send_message(message.chat.id,"Макс.темп: " + str(temperature['temp_max']) + ", " + "Мин.темп: " + str(temperature['temp_min'])
        + ", " + "В данный момент темп: " + str(temperature['temp']))
    elif 'Привет' in message.text:
        bot.send_message(message.chat.id,"Привет, что хотел?")
    else:
        bot.send_message(message.chat.id,"Я не знаю такого слова!!")

        

if __name__ == '__main__':
    bot.polling(none_stop=True)