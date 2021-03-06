#!/usr/bin/env python3
# sip_bot.py - a bot that responds to messages by sipping

import os
import wikipedia_grabber
import discord
from dotenv import load_dotenv
from discord.ext import commands

# load the bot's Discord token from the .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
print('Token loaded.')

# create the bot
bot = commands.Bot(command_prefix='!',help_command=None)
print('Sip Bot successfully initiated.')

# when a user calls the command !sip followed by a key phrase, the bot returns the description provided by get_description()
@bot.command(name='sip', help='Prefaces a description of the keyword with a big sip')
async def sips(ctx, *keywords):
    key_phrase = ' '.join(keywords)
    print('Request made for "' + key_phrase + '"\n') 
    description = wikipedia_grabber.get_description(key_phrase)
    message = "*sips*\nNow there's " + description    
    await ctx.send(message)
    print('Successfully delivered the following message:\n\n' + message + '\n')

# handle all other commands
@bot.event
async def on_command_error(ctx,error):
    pass
    
bot.run(TOKEN)
