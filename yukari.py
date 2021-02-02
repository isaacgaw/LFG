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
import random

import aiohttp
from ply import lex
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageChops

import json
import sys
from pathlib import Path

TOKEN = 'abc123'

client = commands.Bot(command_prefix='-')

ALL_COMMANDS = "```-ping   Checks if the bot is online\n-fu     Flip someone off\n-as     UwU whats this?\n-help   Aren't you using this command right now?```"

@client.command()
@commands.is_owner()
async def shutdown(ctx):
    await ctx.send("Shutting down")
    await ctx.bot.logout()

@client.event
async def on_message(message): # manually implementing the Yukari commands where the input is a string with whitespace, so you don't need to surround it with quotes.
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('-highlow'): # Need to figure out why this doesn't work
        print(message.guild,":", message.channel)
        print(message.author)
        print(message.content)
        print("High Low game started")
        temp = random.randint(0,100)
        temp2 = random.randint(0,100)
        print(temp)
        print(temp2)
        msg = ("> Is it going to be higher or lower %d?" % temp).format(message)
        await message.channel.send(msg)
        tempbool = True
        #while (tempbool == True):
            #print ("zzzz")
            #if message.content == ('-high'):
               # if (temp2 > temp):
                  #  print("Win")
                  #  msg = ("Number is %d\n You Win!!!!!" % temp2)
                  #  break
                #else:
                  #  print("Lose")
                   # msg = ("Number is %d\n You Lose!" % temp2)
        print('')        
        

    if message.content == ('-ping'): # Ping command to see if the bot is online
        print(message.guild,":", message.channel)
        print(message.author)
        print(message.content)
        msg = 'pong'.format(message)
        print('Pinged')
        print('')
        await message.channel.send(msg)
    
    if message.content.startswith('-fu'): # Flip someone off
        print(message.guild,":", message.channel)
        print(message.author)
        print(message.content)
        start = message.content.find('<@')
        end = message.content.find(">") + 1
        atUser=message.content[start:end]
        
        if atUser == -1: # Checks if there is a user mentioned...why this no work
            atUser=""
            print('A fuck has been given')
            msg = ("Fuck you!").format(message)
        else:
            print('A fuck has been given to %s' % atUser)
            atUser=" %s" % atUser
            msg = ("Fuck you%s!" % atUser).format(message)
                
        print('')
        await message.channel.send(msg)
        
    if message.content == ('-as'): # Yukari's Active skill
        print(message.guild,":", message.channel)
        print(message.author)
        print(message.content)
        msg = "Dark Rise: Assault".format(message)
        await message.channel.send(msg)
        
    if message.content == ('-help'): # Help Command to list all the commands of the bot
        print(message.guild,":", message.channel)
        print(message.author)
        print(message.content)
        print('Help Sent')
        msg = ALL_COMMANDS.format(message)
        await message.channel.send(msg)
    
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="Something big coming"))
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
