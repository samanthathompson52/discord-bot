#Creates commands related to a dog such as pet, fetch, etc.
#This discord bot is modeled and themed as a dog and this serves to add to that theme

import discord
from discord.ext import commands

class Dog(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

#Pet Command
#Sends a random message to the user related to a dog being pet
    @commands.command(name='pet', help='Pet the Loki man!')
    async def roll(self, member):
        randomPet = [
             f'Ooooo that is the spot {member.name}!',
             f'Thank you for the best head pats.',
             f'Keep petting me human!',
             f'Belly rubs better be next {member.name}!',
             f'I really am the bestest boy!',
             f'{member.name}, these pets are pretty good....but Samaara does it better',
             f'Woof Woof!'
         ]
        msg = random.choice(randomPet)
        await channel.send(msg)

#Fetch command for user interaction with Loki. Key words trigger different reactions.
#Current keywords: bone, steak, gift, ball, cardboard, money, Samaara
    @commands.command(name='fetch', help='Tell Loki to fetch an item!')
    async def roll(self, ctx, item = ""):
        if item == "bone":
            msg = "🦴       Here. Only because I want it for myself mwahahahaaha"
        elif item == "steak":
            msg = "🥩       Here. Only because I want it for myself mwahahahaaha"
        elif item == "gift":
            msg = "🎁       Here. It's literally an empty box so I have no idea why you want this thing."
        elif item == "ball":
            msg = "⚾       OH BOY! YOU GONNA PLAY WITH ME?"
        elif item == "cardboard" or item == "card board":
            msg = "📦       REALLY? Don't be a snitch and tell my momma. Tasty Tasty cardboard...."
        elif item == "money":
            msg = "💰💵💰💵💰      I gotchu bro"
        elif item == "Samaara" or item == "samaara" or item == "Sam" or item == "sam":
            msg = "You can't summon my mother like that!"
        else:
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
        await channel.send(msg)


def setup(bot):
    bot.add_cog(Dog(bot))