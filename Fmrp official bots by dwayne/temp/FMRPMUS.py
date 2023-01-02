from discord.ext import commands
import discord
bot = commands.Bot(command_prefix=".")
bot.lava_nodes = [
    {
        'host' :  'lava.link',
        'port' : '80',
        'rest_url' : f"https:lava.link:80",
        'identifier' : 'MAIN',
        'password' : 'anything',
        'region' : 'singapore'
    }
]

@bot.event
async def on_ready():
    print("bot ready !")
    bot.load_extension('dismusic')

bot.run("MTA1ODA0NTIyNDUwNjYzMDE4NA.GSeBtm.5CoOrfcwJcRQnjLfGp16Tq-nijzG-AcsWbkhok")