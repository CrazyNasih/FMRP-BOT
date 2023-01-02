from discord.ext import commands
import discord


bot = commands.Bot(command_prefix=".",intents=discord.Intents.all(), description="Sugestion Bot By Dwayne#7270")

@bot.event
async def on_ready():
    print("i have logged in")

@bot.command(pass_context=True)
async def hello(ctx, name :str):
    await ctx.send(f"Hello I am bot {name}")

bot.run("MTA1NTAwODc1NDcxNTg3MzMxMA.G7Zmpm.vcqaQxuV-luuhZhXGdwd-zeE2pJfOrHcPF0ltM", reconnect=True)