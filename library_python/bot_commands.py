# def get_location(lat, lon):
#     url = f'https://yandex.ru/pogoda/?utm_campaign=informer&utm_content=main_informer&utm_medium=web&utm_source=home&utm_term=title1'
#     return url

# def weather_command(city:'moscow'):
    # owm = OWM('b00807ac08bd8e6e2b4d8ee9da06388a')
    # mgr = owm.weather_manager()
    # observation = mgr.weather_at_place(city)
    # weather = observation.weather
    # location = get_location(observation.location.lat, observation.location.lon)
    # temperature = weather.temperature('celsius')
    # return temperature, location
from telegram import Update
from pprint import pprint
from pyowm import OWM
 
import requests #для курса доллара! Установил библиотеку из Pypi.org

from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime
from log import *

def Hi_command(update: Update, context: CallbackContext):
    log_command(update,context)
    update.message.reply_text(f'Hi {update.effective_user.first_name}')

def time_command(update: Update, context: CallbackContext):
    log_command(update,context)
    update.message.reply_text(f'{datetime.datetime.now().time()}')

def help_command(update: Update, context: CallbackContext):
    log_command(update,context)
    update.message.reply_text(f'/hello\n/time\n/help\n/sum\n/mult\n/sub\n/div\n/weather\n/dollars\n/euro')

def echo_command(update: Update, context: CallbackContext):
    msg = update.message.text
    print(msg)
    update.message.reply_text(f'{msg}')
    
# def weather_command(update: Update, context: CallbackContext):
    # msg = update.message.text
    # update.message.reply_text(f'https://www.gismeteo.ru/weather-sankt-peterburg-4079/')

def weather_command(update: Update, context: CallbackContext):
    lat = 59.5619
    lon = 30.1850
    url= f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=c69d4ec09661c0aaeac9005b4133b90e'
    pprint(url)
    data = open('file.txt', 'a')
    
    # city_msg = url['weather']['main']
    # weather_msg = url["weather"]
    # print(weather_msg)
    # print(city_msg)
    # update.message.reply_text(f'{city_msg}')

def dollars_command(update: Update, context: CallbackContext):
    data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()  
    pprint(data['Valute']['USD']) 
    name_msg = data['Valute']['USD']['Name']
    value_msg = data['Valute']['USD']['Value']
    update.message.reply_text(f'{name_msg}: {value_msg}')

def euro_command(update: Update, context: CallbackContext):
    data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()  
    pprint(data['Valute']['EUR']) 
    name_msg = data['Valute']['EUR']['Name']
    value_msg = data['Valute']['EUR']['Value']
    update.message.reply_text(f'{name_msg}: {value_msg}')

def sum_command(update: Update, context: CallbackContext):
    log_command(update,context)
    msg = update.message.text
    print(msg)
    items = msg.split() # /sum  123 321 
    x = int (items[1])
    y = int (items[2])
    update.message.reply_text(f'{x}+{y}={x+y}')

def mult_command(update: Update, context: CallbackContext):
    log_command(update,context)
    msg = update.message.text
    print(msg)
    items = msg.split() # /sum  123 321 
    x = int (items[1])
    y = int (items[2])
    update.message.reply_text(f'{x}*{y}={x*y}')

def sub_command(update: Update, context: CallbackContext):
    log_command(update,context)
    msg = update.message.text
    print(msg)
    items = msg.split() # /sum  123 321 
    x = int (items[1])
    y = int (items[2])
    update.message.reply_text(f'{x}-{y}={x-y}')

def div_command(update: Update, context: CallbackContext):
    log_command(update,context)
    msg = update.message.text
    print(msg)
    items = msg.split() # /sum  123 321 
    x = int (items[1])
    y = int (items[2])
    update.message.reply_text(f'{x}/{y}={x/y}')