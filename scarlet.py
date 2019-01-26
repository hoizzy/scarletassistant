import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '$')
Clientdiscord = discord.Client()
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(game=Game(name='$help | Enderman slayerr'))
    
@client.command()
async def session(member):
    role = discord.utils.get(member.server.roles, name='Session')
    client.add_roles(member, role)
    client.say('Success! You are added to session list.')

@client.command()
async def say(*args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await client.say(output)


@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.blue()
    )

    embed.set_author(name='Help')
    embed.add_field(name='$help', value='Sends help', inline=False)
    embed.add_field(name='$releasedate', value='Shows release date for the new hotel', inline=False)
    embed.add_field(name='$credits', value='Shows credits', inline=False)
    embed.add_field(name='$coinflip', value='Flips a coin', inline=False)
    embed.add_field(name='$shift', value='Post a shift(IN TESTING)', inline=False)
    embed.add_field(name='$clear (amount)', value='Deletes an amount of messages.', inline=False)
    
    
    await client.send_message(author, embed=embed)
    await client.say(':white_check_mark: list of commands sent in DMs!')

@client.command(pass_context=True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount)):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say('Messages deleted.')


 
client.run('NTM0NzkzMTk5OTE1NjMwNjI2.Dx-xfA.0SyfAxDCEVZLhnvKOKymJw4f08Q')
