import discord
from discord.ext import commands
import requests
import os
from pytube import search
import request
from bs4 import BeautifulSoup

# Ustawienia bota
TOKEN = 'TWÓJ TOKEN'
PREFIX = '$'

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

def kody_do_sims4 ():
    # Możesz to zmienić na wyszukiwanie w internecie lub na API z kodami
    cheats = [
        'motherlode - 50 000 Simoleonów',
        'kaching - 1000 Simoleonów',
        'testingcheats true - Włącza tryb testowy',
        'bb.moveobjects - Umożliwia swobodne przesuwanie obiektów',
        'freerealestate on - Wszystkie nieruchomości są darmowe',
        # Dodaj więcej kodów, jak chcesz
    ]
    return cheats

# Komenda do wywołania kodów
@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć, jestem bot{bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def sub(ctx, left: int, right: int):
    """Substract two numbers together."""
    await ctx.send(left - right)


@bot.command()
async def lista_memow(ctx):
    lista = os.listdir('memy')

    await ctx.send(lista)


@bot.command()
async def mem(ctx, image_name: str):
    with open(f'memy/{image_name}.jpg', 'rb') as f:
        # Zapiszmy przekonwertowany plik biblioteki Discord w tej zmiennej!

        picture = discord.File(f)

    await ctx.senun(TOKEN)

@bot.command()
async def kody(ctx):
    cheats = kody_do_sims4()
    # Wyślij listę kodów do kanału
    await ctx.send("Oto kilka kodów do The Sims 4:")
    for cheat in cheats:
        await ctx.send(cheat)

# Komenda powitalna
@bot.event
async def on_ready():
    print(f'Bot {bot.user} jest online!')

# Uruchomienie bota
bot.run(TOKEN)
