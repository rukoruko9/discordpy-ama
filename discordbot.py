import traceback
import os
import discord
import random
from discord.ext import commands
import requests
from bs4 import BeautifulSoup


bot = commands.Bot(command_prefix=".a ")

token = os.environ['DISCORD_BOT_TOKEN']
@bot.command(aliases=['8ball','eightball','8ボール'])
async def _8ball(ctx, *, question):
    responses = ["As I see it, yes.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don’t count on it.",
                "It is certain.",
                "It is decidedly so.",
                "Most likely.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Outlook good.",
                "Reply hazy, try again.",
                "Signs point to yes.",
                "Very doubtful.",
                "Without a doubt.",
                "Yes.",
                "Yes – definitely.",
                "You may rely on it."]
    await ctx.send(f'質問: {question};\n答え: {random.choice(responses)}')



bot.run(token)
