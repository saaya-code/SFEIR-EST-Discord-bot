from dotenv import load_dotenv
from discord.ext import commands
import discord
import requests
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("=========================")
    print("Bot is ready")
    print(bot.user.id)
    print("=========================")

@bot.command()
async def change(ctx):
    pass

bot.run(TOKEN)

