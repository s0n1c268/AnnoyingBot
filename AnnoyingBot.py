import discord
from discord.ext import commands
import time
import random

bot = commands.Bot(command_prefix='!')
bot.remove_command('help')
token = 'Api Token'

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Sonic Coding | use prefix: ?"))
    print('Bot is ready.')

@bot.event
async def on_message(msg):
    content = msg.content.lower()

    annoying_statements = ['Get pinged',
                           'You have been pinged',
                           'Get wrecked',
                           'Get annoyed',
                           'Yo Bro',
                           'Yo Bruhhhhh']
    client_ids = ['clients ids']

    if "annoy" in content:
        while True:
            time.sleep(2)
            await msg.channel.send(f'{random.choice(annoying_statements)}, {random.choice(client_ids)}')

    await bot.process_commands(msg)

@bot.command()
async def bruh(ctx):
    await ctx.send('bruh')

bot.run(token)