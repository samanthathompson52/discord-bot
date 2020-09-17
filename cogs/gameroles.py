import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

GUILD = os.getenv('DISCORD_GUILD')
GAME_ROLE_CHANNEL = int(os.getenv('GAME_ROLE_CHANNEL'))
GAME_ROLE_MESSAGE = int(os.getenv('GAME_ROLE_MESSAGE'))
GAME_EMOJIS = os.getenv('GAME_EMOJIS').split(", ")

class GameRoles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_ready(self):
        validEmojis = GAME_EMOJIS
        guild = discord.utils.find(lambda g: g.id == GUILD, self.bot.guilds)
        channel = self.bot.get_channel(GAME_ROLE_CHANNEL)
        message = await channel.fetch_message(GAME_ROLE_MESSAGE)
        reactions = message.reactions
        for i in reactions:
            try:
                if i.emoji.name not in validEmojis:
                    await message.clear_reaction(i)
            except:
                await message.clear_reaction(i.emoji) 

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        messageID = payload.message_id
        validEmojis = GAME_EMOJIS

        if messageID == GAME_ROLE_MESSAGE:
            guildID = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guildID, self.bot.guilds)
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
                member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        if payload.message_id == GAME_ROLE_MESSAGE:
            guildID = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guildID, self.bot.guilds)
            role = discord.utils.find(lambda r : r.name == payload.emoji.name, guild.roles)
            if role is not None:
                member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                await member.remove_roles(role)
            
def setup(bot):
    bot.add_cog(GameRoles(bot))