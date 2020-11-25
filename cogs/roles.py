#Creates a new general member role users get by reacting to a message
#Serves as an agreement to the established rules in the discord server

import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

GUILD = os.getenv('DISCORD_GUILD')
ROLE_CHANNEL = int(os.getenv('ROLE_CHANNEL'))
ROLE_MESSAGE = int(os.getenv('ROLE_MESSAGE'))
VALID_ROLE_EMOJIS = os.getenv('VALID_ROLE_EMOJIS').split(", ")

class Roles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    #Removes any reactions that are not permitted
    @commands.Cog.listener()
    async def on_ready(self):
        validEmojis = VALID_ROLE_EMOJIS
        guild = discord.utils.find(lambda g: g.id == GUILD, self.bot.guilds)
        channel = self.bot.get_channel(ROLE_CHANNEL)
        message = await channel.fetch_message(ROLE_MESSAGE)
        reactions = message.reactions
        for i in reactions:
            try:
                if i.emoji.name not in validEmojis:
                    await message.clear_reaction(i)
            except:
                await message.clear_reaction(i.emoji) 

    #Adds the member role upon reaction the the rules and information message
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        messageID = payload.message_id
        validEmojis = VALID_ROLE_EMOJIS
        print(messageID)
        if messageID == ROLE_MESSAGE:
            guildID = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guildID, self.bot.guilds)
            print(guild)
            channel = discord.utils.find(lambda g: g.id == payload.channel_id, guild.channels)
            message = await channel.fetch_message(messageID)
            role = discord.utils.find(lambda m: m.name == payload.emoji.name, guild.roles)
            
            if payload.emoji.name not in validEmojis:
                await message.remove_reaction(payload.emoji, payload.member)

            for i in validEmojis:
                emoji = discord.utils.get(guild.emojis, name=i)
                if emoji:
                    await message.add_reaction(emoji)

            if role is not None:
                member = guild.get_member(payload.user_id)
                if member is not None:
                    await member.add_roles(role)

    #Removes the role upon user removing their reaction to the rules and information message. 
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        if payload.message_id == ROLE_MESSAGE:
            guildID = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guildID, self.bot.guilds)
            role = discord.utils.find(lambda r : r.name == payload.emoji.name, guild.roles)
            if role is not None:
                member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)
            
def setup(bot):
    bot.add_cog(Roles(bot))