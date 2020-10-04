#Queue class that allows for admins to make a queue for members to join.
#To be used during community nights with Twitch Subscriber priority. 

import discord
import random
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure

#Identifies if the user is a Twitch Subscriber
def isSub(roles):
    for currRole in roles:
        print(currRole)
        if(currRole.name == "Subscriber"):
            return True
    return False

class Queue(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        self.queue = None
        self.playerNumber = None

    #Displays the queue in order. Lets the user know if there is no queue currently active.
    @commands.group(name='queue', aliases = ['q'], invoke_without_command = True, pass_context = True)
    async def queue(self, ctx):
        if self.queue == None:
            msg = "There is currently no active queue."
        elif len(self.queue) == 0:
            msg = "There is no one in the queue :("
        else:
            msg = ', '.join([str(x[0].name) for x in self.queue])
        await ctx.send(msg)

    #Starts the queue and sets the number of players that can play in the game. Moderator use only.
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

    #Ends the queue. Moderator use only.
    @queue.command(name = 'end')
    @commands.has_role('Moderator')
    async def end_cmd(self, ctx):
        self.queue = None
        msg = "The queue has ended - Thanks for playing!"
        await ctx.send(msg)
    
    #Permenant join function meant to be used only by Samaara. Places her in the first position of the queue automatically.
    @queue.command(name = 'pjoin')
    @commands.has_role('Ya girl')
    async def pjoin_cmd(self, ctx):
        author = (ctx.message.author, isSub(ctx.message.author.roles))
        if self.queue == None:
            msg = ('Sorry! There is currently no active queue to join :(')
        else:
            self.queue.insert(0, author)
            msg = "Samaara has joined the queue!"
        await ctx.send(msg)

    #Adds the user to the queue. Places subscribers above non subscribers in the queue.
    @queue.command(name = 'join')
    async def join_cmd(self, ctx):        
        author = (ctx.message.author, isSub(ctx.message.author.roles))
        if self.queue == None:
            msg = ('Sorry! There is currently no active queue to join :(')
        elif author in self.queue:
            msg = ('You are already in line! Use !queue or !q to view the current queue.')
        else: 
            if author[1] == False:
                self.queue.append(author)
            else:
                i=0
                while i<len(self.queue) and self.queue[i][1] == True:
                    i += 1
                self.queue.insert(i, author)

            msg = "You have succesfully joined the queue! Please wait untill you are told to join the current game. Use !q or !queue to view the queue!"
        await ctx.send(msg)

    #Allows any user to leave the queue
    @queue.command(name = 'leave')
    async def leave_cmd(self, ctx):
        author = (ctx.message.author, isSub(ctx.message.author.roles))
        if self.queue == None:
            msg = (f'Huh, {author[0].name} is trying to leave a queue when a queue does not even exist!')
        elif author in self.queue:
            self.queue.remove(author)
            msg = (f'{author[0].name} has left the queue.')
        else:
            msg = "You were never in the queue in the first place!"
        await ctx.send(msg)

    #Kick a single user from the queue. Moderator use only.
    @queue.command(name = 'kick')
    @commands.has_role('Moderator')
    async def kick_cmd(self, ctx, kickee: str = ""):
        if kickee == "":
            msg = ("Make sure to enter someone to kick! Use the command like this: !q kick Samaara")
        else:
            for i in range(len(self.queue)):
                if self.queue[i][0].name == kickee:
                    self.queue.remove(self.queue[i])
                    msg = (f'{kickee} has been kicked from queue.') 
                    await ctx.send(msg)
                    return
            msg = ("That person is not currently in the queue.")
            
        await ctx.send(msg)

    #Add function - to be used by Moderators only. 
    #Functionally, this may be left out if the owner of discord server prefers users to enter themselves.
    # @queue.command(name = 'add')
    # @commands.has_role('Moderator')
    # async def add_cmd(self, ctx, addee: str = ""):
    #     if addee == "":
    #         msg = ("Make sure to enter someone to Add! Use the command like this: !q add Samaara")
    #     elif addee not in self.queue:
    #         self.queue.append(addee)
    #         msg = (f'{addee} had been added to the queue! Thanks {ctx.message.author.name}.')
    #     elif addee in self.queue:
    #         msg = (f'{addee} is already in the que.')
    #     await ctx.send(msg)

    #Moves the queue. Bumps up the number of players in the queue. Moderator use only. 
    @queue.command(name = 'nextgame')
    @commands.has_role('Moderator')
    async def nxtgame_cmd(self, ctx):
        i = 0
        while i < int(self.playerNumber) and i < len(self.queue):
            if self.queue[i][0].name == 'Samaara':
                i += 1
            else:
                self.queue.pop(i)

    #Presents an image in discord with guidance on how moderators should use the commands.
    @queue.command(name = 'modhelp')
    @commands.has_role('Moderator')
    async def modhelp_cmd(self, ctx):
        msg = "https://imgur.com/gallery/AOt8ABK"
        await ctx.send(msg)

    #Presents an image in discord with guidance on how members can use the queue commands. 
    @queue.command(name = 'help')
    async def help_cmd(self, ctx):
        msg = "https://imgur.com/h77HQS3"
        await ctx.send(msg)

def setup(bot):
    bot.add_cog(Queue(bot))