#Used to allow users and admins to create polls for everyone to vote on. 
#Key functions:
#Admins - create official poles that mention roles
#Members - Fun polls that are timed and get removed after x amount of time after completion. 

import discord
import random
from discord.ext import commands

class Poll(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None



def setup(bot):
    bot.add_cog(Poll(bot))