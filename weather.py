import discord
from discord.ext import commands
import requests
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')
key = os.getenv('KEY')
intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix="-", intents=discord.Intents.all())


@bot.command()
async def Weather(message, *arguments):
    city = ''
    type_temp = ''
    for i in range (len(arguments)):
        if arguments[i].lower() == 'f' or arguments[i].lower() == 'c':
            type_temp = arguments[i].lower()
        else:
            city += arguments[i] + ' '
    city = city.strip()
    if len(arguments) < 1:
        await message.channel.send(f"Not enough arguments")
    else:
        r = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}")
        data = r.json()
        temp_k = data['main']['temp']
        temp_c = temp_k - 273.15
        if type_temp == 'f':
            temp_f = 1.8 * (temp_k - 273) + 32
            await message.channel.send(f"It is {round(temp_f, 2)}° Fahrenheit in {city}")
        else:
            await message.channel.send(f"It is {round(temp_c, 2)}° Celsius in {city}")


@bot.event
async def on_ready():
    print("Ready")


bot.run(TOKEN)
