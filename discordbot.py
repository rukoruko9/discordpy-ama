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
async def clear(ctx, amount = 5):
    await ctx.channel.purge(limit = amount)
@bot.command()
async def info(ctx):
    embed = discord.Embed(title="素晴らしいボット", description="天中の情報を提供してくれる、素晴らしいボット", color=0xeee657)

    
    embed.add_field(name="製作者", value="rukoruko")

    
    embed.add_field(name="このボットの鯖加入数", value=f"{len(bot.guilds)}")
    await ctx.send(embed=embed)

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
@bot.command()
async def voca(ctx, word):
    result = requests.get("https://dictionary.goo.ne.jp/word/" + word + "/")
    result = BeautifulSoup(result.text, "html.parser")
    for meta_tag in result.find_all('meta', attrs={'name': 'personal_snippet'}):
        await ctx.send(meta_tag.get('content'))
@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)
    




bot.run(token)  
