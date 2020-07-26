import discord
from discord.ext import commands
import json
import steamcode as sc

prefix = '!'
client = commands.Bot(command_prefix=prefix)
TOKEN = json.load(open('./token.json'))


@client.event
async def on_ready():
    print(f'{client.user.name} (BOT) is online!')


@client.command()
async def auth(ctx):
    code = sc.get_code()
    await ctx.send(code)

client.run(TOKEN)  # leave at end of code
