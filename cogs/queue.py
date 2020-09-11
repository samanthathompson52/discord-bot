import discord
import random
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure

class Queue(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        self.queue = None
        self.playerNumber = None

    @commands.group(name='queue', aliases = ['q'], invoke_without_command = True, pass_context = True)
    async def queue(self, ctx):
        if self.queue == None:
            msg = "There is currently no active queue."
        elif len(self.queue) == 0:
            msg = "There is no one in the queue :("
        else:
            msg = ', '.join([str(x) for x in self.queue])
        await ctx.send(msg)

    @queue.command(name = 'start')
    @commands.has_role('Moderator')
    async def start_cmd(self, ctx, entryNumber: int = 10):
        self.playerNumber = entryNumber
        if self.queue == None:
            self.queue = []
            msg = (f'The queue has been started for {self.playerNumber} players!')
        else:
            msg = "There is already an active queue! End the previous queue to create a new one."
        await ctx.send(msg)

    @queue.command(name = 'end')
    @commands.has_role('Moderator')
    async def end_cmd(self, ctx):
        self.queue = None
        msg = "The queue has ended - Thanks for playing!"
        await ctx.send(msg)
    
    @queue.command(name = 'pjoin')
    @commands.has_role('Ya girl')
    async def pjoin_cmd(self, ctx):
        if self.queue == None:
            msg = ('Sorry! There is currently no active queue to join :(')
        else:
            self.queue.insert(0, "Samaara")
            msg = "Samaara has joined the queue!"
        await ctx.send(msg)

    @queue.command(name = 'join')
    async def join_cmd(self, ctx):
        if self.queue == None:
            msg = ('Sorry! There is currently no active queue to join :(')
        elif ctx.message.author.name in self.queue:
            msg = ('You are already in line! Use !queue or !q to view the current queue.')
        else:
            self.queue.append(ctx.message.author.name)
            msg = "You have succesfully joined the queue! Please wait untill you are told to join the current game. Use !q or !queue to view the queue!"
        await ctx.send(msg)

    @queue.command(name = 'leave')
    async def leave_cmd(self, ctx):
        if self.queue == None:
            msg = (f'Huh, {ctx.message.author.name} is trying to leave a queue when a queue does not even exist!')
        else:
            self.queue.remove(ctx.message.author.name)
            msg = (f'{ctx.message.author.name} has left the queue.')
        await ctx.send(msg)

    @queue.command(name = 'kick')
    @commands.has_role('Moderator')
    async def kick_cmd(self, ctx, kickee: str = ""):
        if kickee == "":
            msg = ("Make sure to enter someone to kick! Use the command like this: !q kick Samaara")
        elif kickee not in self.queue:
            self.queue.remove(ctx.message.author.name)
            msg = ("That person is not currently in the queue.")
        elif kickee in self.queue:
            self.queue.remove(kickee)
            msg = (f'{kickee} has been kicked from queue.')
        await ctx.send(msg)

    @queue.command(name = 'add')
    @commands.has_role('Moderator')
    async def add_cmd(self, ctx, addee: str = ""):
        if addee == "":
            msg = ("Make sure to enter someone to Add! Use the command like this: !q add Samaara")
        elif addee not in self.queue:
            self.queue.append(addee)
            msg = (f'{addee} had been added to the queue! Thanks {ctx.message.author.name}.')
        elif addee in self.queue:
            msg = (f'{addee} is already in the que.')
        await ctx.send(msg)

    @queue.command(name = 'nextgame')
    @commands.has_role('Moderator')
    async def end_cmd(self, ctx):
        i = 0
        while i < int(self.playerNumber) and i < len(self.queue):
            if self.queue[i] == 'Samaara':
                i += 1
            else:
                self.queue.pop(i)

def setup(bot):
    bot.add_cog(Queue(bot))