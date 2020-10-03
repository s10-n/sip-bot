# sip_bot.py - a bot that responds to messages by sipping

import os
import wikipedia_grabber
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='sip', help='Prefaces a description of the keyword with a big sip')
async def sips(ctx, *keywords):
    key_phrase = ' '.join(keywords)
    description = wikipedia_grabber.get_description(key_phrase)
    await ctx.send("*sips*\nNow there's " + description)
    
bot.run(TOKEN)
