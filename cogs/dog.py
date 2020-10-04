#Creates commands related to a dog such as pet, fetch, etc.
#This discord bot is modeled and themed as a dog and this serves to add to that theme


import discord
from discord.ext import commands

class Dog(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None



def setup(bot):
    bot.add_cog(Dog(bot))