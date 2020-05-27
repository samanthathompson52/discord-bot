# Bippity Boppity Bot
# bot.py
import random
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
WELCOME_CHANNEL = int(os.getenv('WELCOME_CHANNEL'))

bot = commands.Bot(command_prefix='!')

#Stuff that happens when the bot launches
@bot.event
async def on_ready():
    #guild = discord.utils.find(lambda g: g.id == GUILD, client.guilds)
    for guild in bot.guilds:
        if guild.id == GUILD:
            break

    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    members = '\n - '.join([member.name for member in guild.members])
    #print(f'Guild Members:\n - {members}')

#When new member joins the server
@bot.event
async def on_member_join(member):
    randomWelcome = [
        f'Welcome to the server {member.name}',
        f'{member.name} has joined the server',
        f'{member.name} is new to the server and has tig ol bitties'
    ]
    msgWelcome = random.choice(randomWelcome)

    channel = bot.get_channel(WELCOME_CHANNEL)
    await channel.send(msgWelcome)

#Error Statement
@bot.event
async def on_command_error(ctx, error):
    print(error)
    await ctx.send("ERROR: I cannot comprehand your nonsense") 

#Dice Rolls
@bot.command(name='roll', help='Simulates rolling a DnD dice.')
async def roll(ctx, number_of_sides = "d6"):
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

@bot.command(name='wato', help='What are the odds? Will you win against the bot? To use this command input as the following: !wato (your number) (Odds)')
async def wato(ctx, userNum: int, odds: int):
    rng = random.choice(range(1, int(odds) + 1))
    if userNum == rng:
        msg = (f'You lost! I guessed {rng} correctly! Robots will forever be superior.')
    elif userNum > odds:
        msg = ("You are a cheater and gave me an impossible task.")
    else:
        msg = (f'Your number was {userNum} and mine was {rng}....you win...this time.')
    await ctx.send(msg) 

#LAST - MUSt BE thE LAST THING DUMB BITCH
bot.run(TOKEN)