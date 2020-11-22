import traceback
import os
import discord
import random
from discord.ext import commands
import requests
from bs4 import BeautifulSoup


bot = commands.Bot(command_prefix=".a ")

token = os.environ['DISCORD_BOT_TOKEN']

@bot.command()
async def voca(ctx, word):
    result = requests.get("https://dictionary.goo.ne.jp/word/" + word + "/")
    result = BeautifulSoup(result.text, "html.parser")
    for meta_tag in result.find_all('meta', attrs={'name': 'personal_snippet'}):
        await ctx.send(meta_tag.get('content'))


bot.run(token)
