#Copyright (c) 2021 TrustedInstaller
import discord
from discord.ext import commands

class Moderation(commands.Cog):
	def _init_(self, client):
		self.client = client

	filtered_word = ["fuck","shit","nsfw","địt mẹ mày","lồn","địt","cặc","https","http"]

	@commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'{member.mention} was kicked')
    
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'{member.mention} was banned')
    
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('a')
    
        for ban_entry in banned_users:
            user = ban_entry.user
        
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'{user.mention} was unbanned')
                return
            
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clean(ctx, amount : int):
        await ctx.channel.purge(limit=amount)
        await ctx.send(f'I was deleted {amount} messages for you')
    
    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def addrole(ctx, role: discord.Role, user: discord.Member):
        await user.add_roles(role)
        await ctx.send(f'Gave {role.mention} to {user.mention}')
    
    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def delrole(ctx, role: discord.Role, user: discord.Member):
        await user.remove_roles(role)
        await ctx.send(f'Removed {role.mention} from {user.mention}')

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def mute(ctx, member : discord.Member):
        muted_role = ctx.guild.get_role(866884884013121596)
        await member.add_roles(mute_role)
        await ctx.send(f'{member.mention} was muted')

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def unmute(ctx, member : discord.Member):
        mute_role = ctx.guild.get_role(866884884013121596)
        await member.remove_roles(mute_role)
        await ctx.send(f'{member.mention} was unmuted')

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def lockdown(ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
        await ctx.send(ctx.channel.mention + 'has been locked down due to some reason')

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def unlckdwn(ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
        await ctx.send(ctx.channel.mention + 'has been unlocked')

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def slowmode(ctx, seconds: int):
        await ctx.channel.edit(slowmode_delay=seconds)
        await ctx.send(f'We have set the slowmode of this channel to {seconds} seconds')

    @commands.command()
    @commands.has_permissions(manage_nicknames=True)
    async def cnick(ctx, member: discord.Member, nick):
        await member.edit(nick=nick)
        await ctx.send(f'We have set the your nickname to {member.mention}')

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def mulunban(ctx):
        banlist = await ctx.guild.bans()
        for user in banlist:
            try:
                await ctx.guild.bans(user=users.user)
            except:
                pass
        await ctx.send(f'We have mass unbanned')

def setup(client):
	client.add_cog(Moderation(client))