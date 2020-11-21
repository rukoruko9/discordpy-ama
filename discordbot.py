import traceback
import os, sys
import discord
import time
import random
from discord.ext import commands
import random
import requests
from bs4 import BeautifulSoup


token = os.environ['DISCORD_BOT_TOKEN']

bot = commands.Bot(command_prefix = ".a ")






@bot.command()
async def voca(ctx, word):
    result = requests.get("https://dictionary.goo.ne.jp/word/"+word+"/")
    result = BeautifulSoup(result.text, "html.parser")
    for meta_tag in result.find_all('meta', attrs={'name': 'personal_snippet'}):
        await ctx.send(meta_tag.get('content'))
@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)
    




bot.run(TOKEN)  
