#Copyright (c) 2021 TrustedInstaller
import discord
from discord.ext import commands

class ErrorHandling(commands.Cog):
	def _init_(self, client):
		self.client = client

    @commands.Cog.listener()
    async def on_command_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please send all required arguments,')
        
    @commands.Cog.listener()
        async def on_command_error(ctx, error):
            if isinstance(error, commands.MissingPermissions):
                await ctx.send('You are not allowed to use this command')
        
    @commands.Cog.listener()
        async def on_command_error(ctx, error):
            if isinstance(error, commands.CommandNotFound):
                await ctx.send('What the heck, that command is illegal')
    

def setup(client):
	client.add_cog(ErrorHandling(client))