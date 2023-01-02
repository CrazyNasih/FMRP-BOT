from discord.ext import commands
import discord
client = commands.Bot(command_prefix=".", intents = discord.Intents.all())
command_prefix="."
client.remove_command("help")
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="fmrp.await || .help"))
    print("{0.user} is now online!".format(client))
    channel = client.get_channel(1051207829702328340)
    await channel.send("`Fmrp bot just got booted up !`")
@client.command()
async def message(ctx, arg1, *args):
    try:
        args = str(args)
        args = args.replace("'", "")
        args = args.replace("(", "")
        args = args.replace(")", "")
        args = args.replace(",", "")
        if args == '':
            ctx.reply(f"```{command_prefix}message [channelid] [message]```")
            return
        else:
            arg1 = int(arg1)
            channel = client.get_channel(arg1)
            await channel.send(args)
    except Exception as e:
        await ctx.reply("```Something went wrong !. Have you checked the format properly ?  (.message [channelid] [message])```")
        print(e)
        channel = client.get_channel(1051207829702328340)
        await channel.send(f"``` An occured while somebody was using ({command_prefix}message):\n{e}```")
@client.command()
async def announce(ctx, *args):
    args = str(args)
    args = args.replace("'", "")
    args = args.replace("(", "")
    args = args.replace(")", "")
    args = args.replace(",", "")
    embedVar = discord.Embed(title="ANNOUNCEMENT", description=args, color=0x00ff00)
    await ctx.reply("`Announcmet Sent Successfully` ✅")
    embedVar.set_footer(text='Official Farinzo Mallu Roleplay Bot Made By Dwayne#7270',icon_url="https://yt3.ggpht.com/_uyqYyGzOfOxsvxMrmoDRoYzDRE5uf8JyXqLAsue5XY5Ux-SBideNA0KzR6KIQD1u_7wnpCeUSw=s900-c-k-c0x00ffffff-no-rj")
    picuser = client.get_user(1054749194054815785)
    embedVar.set_thumbnail(url=picuser.avatar)
    embedVar.set_image(url="https://media.discordapp.net/attachments/784318977005453312/784319451427373096/source-2.gif")
    channel = client.get_channel(1032664906891264122)
    await channel.send(embed=embedVar)
    role = client.get_guild(1032241486588297286).get_role(1032745427772112916)
    await channel.send(role.mention)
@client.command()
async def whannounce(ctx):
    embedVar = discord.Embed(title="W̲H̲ ̲A̲N̲N̲O̲U̲N̲C̲M̲E̲N̲T̲", description="AN ADMIN IS NOW READY TO TAKE WHITELIST. SO NON WHITELISTED MEMBERS PLEASE JOIN WAITING VC", color=0x00ff00)
    embedVar.set_footer(text='Official Farinzo Mallu Roleplay Bot Made By Dwayne#7270',icon_url="https://yt3.ggpht.com/_uyqYyGzOfOxsvxMrmoDRoYzDRE5uf8JyXqLAsue5XY5Ux-SBideNA0KzR6KIQD1u_7wnpCeUSw=s900-c-k-c0x00ffffff-no-rj")
    picuser = client.get_user(1054749194054815785)
    embedVar.set_thumbnail(url=picuser.avatar)
    embedVar.set_image(url="https://media.discordapp.net/attachments/702831042276491345/803725715605946368/sv.gif")
    channel = client.get_channel(1032703147950489700)
    await channel.send(embed=embedVar)
    role = client.get_guild(1032241486588297286).get_role(1032745668172849192)
    await channel.send(role.mention)
@client.command()
async def showip(ctx, *args):
    embedVar = discord.Embed(title="SERVER IP", description="```fmrp.ddns.net:9999```", color=0x00ff00)
    botprogile = client.get_user(1054749194054815785)
    embedVar.set_thumbnail(url=botprogile.avatar)
    embedVar.set_image(url="https://media.discordapp.net/attachments/1051131719106957462/1058459089505628160/tenor.gif")
    await ctx.channel.send(embed=embedVar)
@client.command()
async def help(ctx, *args):
    print("me")
    embedVar = discord.Embed(title="          HELP MENU", description="```\n               WHITELISTED \n\n       << CURRENTLY NO COMMANDS >>\n\n                ADMINS \n\n          [+] > .announce\n          [+] > .whannounce\n          [+] > .showip\n          [+] > .wh\n          [+] > .makeadmin\n          [+] > .announce (ig)```", color=0x00ff00)
    embedVar.set_footer(text='Official Farinzo Mallu Roleplay Bot Made By Dwayne#7270',icon_url="https://yt3.ggpht.com/_uyqYyGzOfOxsvxMrmoDRoYzDRE5uf8JyXqLAsue5XY5Ux-SBideNA0KzR6KIQD1u_7wnpCeUSw=s900-c-k-c0x00ffffff-no-rj")
    embedVar.set_image(url="https://media1.tenor.com/images/2965622216ddbfde16614c4ecdf8fdbf/tenor.gif?itemid=27311270")
    await ctx.channel.send(embed=embedVar)

client.spotify_credentials = {
    'client_id': '6f4ed666ac9942d689f076bc2e901679',
    'client_secret': '6189ee7ce1b24c86bb85dd457aed778e'
}
client.run("MTA1NDc0OTE5NDA1NDgxNTc4NQ.GNr-K4.NT6IQA7tvi5JOhpgdHdnKaZUUK3Xe7gEdsyaVw")