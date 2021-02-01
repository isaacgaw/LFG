import discord
from discord.ext import commands
from enum import Enum
import monster
import math
import csv
import os
import io
from shutil import rmtree
import re
import urllib

import json
import sys
from pathlib import Path

TOKEN = 'abc123'

client = commands.Bot(command_prefix='-')

ALL_COMMANDS = "```-ping\n-fu\n-as\n-help```"

@client.command()
@commands.is_owner()
async def shutdown(ctx):
    await ctx.send("Shutting down")
    await ctx.bot.logout()

@client.event
async def on_message(message): 
    if message.author == client.user:
        return

    if message.content.startswith('-ping'):
        print(message.guild,":", message.channel)
        print(message.author)
        print(message.content)
        msg = 'pong'.format(message)
        print('Pinged')
        print('')
        await message.channel.send(msg)
    
    if message.content.startswith('-fu'):
        print(message.guild,":", message.channel)
        print(message.author)
        print(message.content)
        start = message.content.find('<@')
        end = message.content.find(">") + 1
        atUser=message.content[start:end]
        
        if atUser == -1: # Checks if there is a user mentioned
            atUser=""
            print('A fuck has been given')
        else:
            print('A fuck has been given to %s' % atUser)
            atUser=" %s" % atUser
                
        msg = ("Fuck you%s!" % atUser).format(message)
        print('')
        await message.channel.send(msg)
        
    if message.content.startswith('-as'):
        print(message.guild,":", message.channel)
        print(message.author)
        print(message.content)
        msg = "Energy Ball".format(message)
        await message.channel.send(msg)

    if message.content  == ('-help'):
        print(message.guild,":", message.channel)
        print(message.author)
        print(message.content)
        print('')
        msg = ALL_COMMANDS.format(message)
        await message.channel.send(msg)
        
        
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
