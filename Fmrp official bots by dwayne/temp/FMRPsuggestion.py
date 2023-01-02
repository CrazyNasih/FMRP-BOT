import discord
from discord import *
from discord.ext import commands
from discord.utils import get
TOKEN = "MTA1NTAwODc1NDcxNTg3MzMxMA.G7Zmpm.vcqaQxuV-luuhZhXGdwd-zeE2pJfOrHcPF0ltM"
intest = discord.Intents.all()
client = discord.Client(intents=intest) 
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Suggestions !  "))
    print("{0.user} is now online!".format(client))
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.channel.name == '📮║ꜱᴜɢɢᴇꜱᴛɪᴏɴꜱ':
        choice = message.content
        embedVar = discord.Embed(title="SUGGESTION", description=choice, color=0x00ff00)
        await message.delete()
        embedVar.add_field(name=message.author, value="React with ✅ to agree and ⭕ to disagree", inline=False)
        embedVar.set_image(url="https://media.discordapp.net/attachments/784318977005453312/784319451427373096/source-2.gif")
        msg = await message.channel.send(embed=embedVar)
        await msg.add_reaction("✅")
        await msg.add_reaction("⭕")
        channel = client.get_channel(1051131719106957462)
        role = client.get_guild(1032241486588297286).get_role(1036219213074927677)
        await channel.send(f"{message.author.mention} has posted a new suggestion ! {role.mention}" )
client.run(TOKEN)