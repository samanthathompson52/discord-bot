#Creates commands related to a dog such as pet, fetch, etc.
#This discord bot is modeled and themed as a dog and this serves to add to that theme

import discord
import random
from discord.ext import commands

class Dog(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        self.messageMap = {'bone': "🦴       Here. Only because I want it for myself mwahahahaaha",
                        'steak': "🥩       Here. Only because I want it for myself mwahahahaaha",
                        'gift': "🎁       Here. It's literally an empty box so I have no idea why you want this thing.",
                        'ball': "⚾       OH BOY! YOU GONNA PLAY WITH ME?",
                        'cardboard': "📦       REALLY? Don't be a snitch and tell my momma. Tasty Tasty cardboard....",
                        'card board': "📦       REALLY? Don't be a snitch and tell my momma. Tasty Tasty cardboard....",
                        'money': "💰💵💰💵💰      I gotchu bro",
                        'Samaara': "You can't summon my mother like that!",
                        'samaara': "You can't summon my mother like that!",
                        'Sam': "You can't summon my mother like that!",
                        'sam': "You can't summon my mother like that!"  }    
            

#Pet Command
#Sends a random message to the user related to a dog being pet
    @commands.command(name='pet', help='Pet the Loki man!')
    async def pet(self, ctx):
        randomPet = [
             f'Ooooo that is the spot!',
             f'Thank you for the best head pats.',
             f'Keep petting me human!',
             f'Belly rubs better be next!',
             f'I really am the bestest boy!',
             f'These pets are pretty good....but Samaara does it better',
             f'Woof Woof!'
         ]
        msg = random.choice(randomPet)
        await ctx.channel.send(msg)

#Fetch command for user interaction with Loki. Key words trigger different reactions.
#Current keywords: bone, steak, gift, ball, cardboard, money, Samaara
    @commands.command(name='fetch', help='Tell Loki to fetch an item!')
    async def fetch(self, ctx, item = ""):
        msg = self.messageMap.get(item, default=False)
        if msg == False:
            randomFetch = [
                "I ain't getting that",
                "You really think I care about that?",
                "No.",
                "**Angry Barks**",
                "Naw, I'm good",
                "You go get it",
                "Nope, not for you!"
            ]
            msg = random.choice(randomFetch)
        await ctx.channel.send(msg)

def setup(bot):
    bot.add_cog(Dog(bot))