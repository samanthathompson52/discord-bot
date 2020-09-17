import discord
from discord.ext import commands
import random
import os
from dotenv import load_dotenv

load_dotenv()
GUILD = os.getenv('DISCORD_GUILD')
WELCOME_CHANNEL = int(os.getenv('WELCOME_CHANNEL'))
ROLE_MESSAGE = int(os.getenv('ROLE_MESSAGE'))

class Events(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    #Stuff that happens when the bot launches
    @commands.Cog.listener()
    async def on_ready(self):
        #guild = discord.utils.find(lambda g: g.id == GUILD, client.guilds)
        for guild in self.bot.guilds:
            if guild.id == GUILD:
                break

        print(
            f'{self.bot.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )

        channel = self.bot.get_channel(WELCOME_CHANNEL)
        members = '\n - '.join([member.name for member in guild.members])

        

    #When new member joins the server
    @commands.Cog.listener()
    async def on_member_join(self, member):
        randomWelcome = [
            f'Welcome to the server @{member.name}!',
            f'@{member.name} has joined the server!',
            f'@{member.name} is new to the server give them a hello!',
            f'Welcome to the best server in all the land @{member.name}!',
            f'Welcome to the SamFam @{member.name}!',
            f'Welcome @{member.name}! Thanks for joining!',
            f'Welcome @{member.name}! I am glad you made the best choice and joined this discord',
            f'Welcome @{member.name}, enjoy your stay!',
            f'Welcome @{member.name}! Did you bring any food?',
            f'A wild @{member.name} has appeared!',
            f'@{member.name} has stumbled into the discord! Are they lost? No? OH - WELCOME!"',
            f'Hello @{member.name}! Are you a new friend for Loki?',
            f'Hello There @{member.name}! Just ignore the moderators trapped in the basement :)',
            f'@{member.name} is new here! **Welcome!**'
        ]

        msgWelcome = random.choice(randomWelcome)
        channel = self.bot.get_channel(WELCOME_CHANNEL)
        await channel.send(msgWelcome)

    #Error Statement
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("You don't have permission to use this command!")
            return
        print(error)
        await ctx.send("ERROR: I cannot comprehand your nonsense") 

def setup(bot):
    bot.add_cog(Events(bot))