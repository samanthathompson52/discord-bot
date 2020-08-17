import discord
import random
from discord.ext import commands

class Blackjack(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None



def setup(bot):
    bot.add_cog(Blackjack(bot))