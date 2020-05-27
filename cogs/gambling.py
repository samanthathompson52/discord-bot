import discord
import random
from discord.ext import commands

class Gambling(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    #Dice Rolls
    @commands.command(name='roll', help='Simulates rolling a DnD dice.')
    async def roll(self, ctx, number_of_sides = "d6"):
        if number_of_sides[0] == "d":
            number_of_sides = number_of_sides[1:]
        try:
            number_of_sides = int(number_of_sides)
        except ValueError:
            await ctx.send("That is not a valid dice 🤔")
            return
        if (number_of_sides != 4 and 
            number_of_sides != 6 and 
            number_of_sides != 10 and
            number_of_sides != 12 and
            number_of_sides != 20 and
            number_of_sides != 100
        ):         
            await ctx.send("That is not a valid DnD dice 🤔")
            return
        dice = str(random.choice(range(1, int(number_of_sides) + 1)))
        await ctx.send(dice) 

    @commands.command(name='wato', aliases = ['whataretheodds','odds'], help='What are the odds? Will you win against the bot? To use this command input as the following: !wato (your number) (Odds)')
    async def wato(self, ctx, userNum: int, odds: int):
        rng = random.choice(range(1, int(odds) + 1))
        if userNum == rng:
            msg = (f'You lost! I guessed {rng} correctly! Robots will forever be superior.')
        elif userNum > odds:
            msg = ("You are a cheater and gave me an impossible task.")
        else:
            msg = (f'Your number was {userNum} and mine was {rng}....you win...this time.')
        await ctx.send(msg) 

def setup(bot):
    bot.add_cog(Gambling(bot))