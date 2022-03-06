import discord
import asyncio
import requests
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')
key = os.getenv('KEY')

client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("-Weather"):
        if message.content[len(message.content)-1:len(message.content)].lower() == 'f' or message.content[len(message.content)-1:len(message.content)].lower() == 'c' :
            city = message.content[9:len(message.content)-2]
        else:
            city = message.content[9:len(message.content)]
        r = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}")
        data = r.json()
        temp_k = data['main']['temp']
        temp_c = temp_k - 273.15
        if message.content[len(message.content)-1:len(message.content)].lower() == 'f':
            temp_f = 1.8 * (temp_k - 273) + 32
            await message.channel.send(f"It is {round(temp_f, 2)}° Fahrenheit in {city}")
            await message.delete()
        else:
            await message.channel.send(f"It is {round(temp_c,2) }° Celsius in {city}")
            await message.delete()


@client.event
async def on_ready():
    print("Ready")


client.run(TOKEN)