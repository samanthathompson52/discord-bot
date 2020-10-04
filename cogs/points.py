#Point system to be used a virtual currency in the discord server

import discord
from discord.ext import commands

class Points(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None



def setup(bot):
    bot.add_cog(Points(bot))