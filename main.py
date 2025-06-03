# BY @gqdThinky 
# YouTube : https://www.youtube.com/@gqdThinky 


import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = ";")

@bot.event
async def on_ready():
	print("xxxxxx")



@bot.command()
@commands.has_permissions(manage_channels=True)
async def lockdown(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role,send_messages=False)
    await ctx.send(ctx.channel.mention + " ***is now in lockdown***")
    
@bot.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role,send_messages=True)
    await ctx.send(ctx.channel.mention + " ***has been unlocked.***")




bot.run("TOKEN")
