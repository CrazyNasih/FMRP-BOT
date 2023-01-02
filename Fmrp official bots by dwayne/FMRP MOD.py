import discord
TOKEN = "MTA1ODI2MDY0NjMwODg5MjcxMg.GHN8P0.Ol9R7KOTdOjZb2ErM85simoWFo_mgAvwRCqpK0"
client = discord.Client(intents=discord.Intents.all()) 
bad_words= ["fuck", "patti", "myre", "thendi", "chetta", "pundichi", "thayoli", "thantha", "thalla ", "kundi", "poori"]
dbr = open("C:\\Users\\user\\Documents\\Vs Code\\Fmrp official bots by dwayne\\database\\db.txt", "r")
dbw = open("C:\\Users\\user\\Documents\\Vs Code\\Fmrp official bots by dwayne\\database\\db.txt", "w")
@client.event
async def on_ready():
    member_count = 0
    guild = client.get_guild(1032241486588297286)
    for member in guild.members:
        member_count += 1
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f"fmrp.audit || {member_count} members"))
    print("{0.user} is now online!".format(client))
    channel = client.get_channel(1051207829702328340)
    await channel.send("```Fmrp bot just got booted up !```")
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    else:
        if '`'in message.content:
            msg = str(message.content)
            msg = msg.replace("`", "")
            msg = msg.replace("``````", "")
            msgp = f"```Channel :{message.channel.name}\nUser :{message.author}\nMessage :{msg}```"
            print(msgp)
            if message.author.id == 1051211039397654620:
                return
            if message.author.name == 'ＦＭＲＰ ║ 🤖#0000':
                return
            channel = client.get_channel(1051207829702328340)
            await channel.send(f"{msgp}")
            return
        else:
            msgp = f"```Channel :{message.channel.name}\nUser :{message.author}\nMessage :{message.content}```"
            print(msgp)
            if message.author.id == 1051211039397654620:
                return
            if message.author.name == 'ＦＭＲＰ ║ 🤖#0000':
                return
            channel = client.get_channel(1051207829702328340)
            await channel.send(f"{msgp}")
    if message.content == 'fmrpnew':
        role = client.get_guild(1032241486588297286).get_role(1032745427772112916)
        embedVar = discord.Embed(title="EVENT", description=f"```HAPPY NEW YEAR DEAR FMRP BUDDIE'S ```{role.mention}", color=0x00ff00)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/1019925497129484329/1058819943082250431/standard_1.gif")
        await message.delete()
        await message.channel.send(embed=embedVar)
    if message.channel.name == '📮║ꜱᴜɢɢᴇꜱᴛɪᴏɴꜱ':
        choice = message.content
        embedVar = discord.Embed(title="SUGGESTION", description=choice, color=0x00ff00)
        await message.delete()
        embedVar.add_field(name=message.author, value="React with ✅ to agree and ⭕ to disagree", inline=False)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/885763246185930802/886555888624762900/ww.gif")
        msg = await message.channel.send(embed=embedVar)
        await msg.add_reaction("✅")
        await msg.add_reaction("⭕")
        channel = client.get_channel(1051131719106957462)
        role = client.get_guild(1032241486588297286).get_role(1036219213074927677)
        await channel.send(f"{message.author.mention} has posted a new suggestion ! {role.mention}" )
    if message.channel.name == '📩║ɪɴɢᴀᴍᴇ-ɴᴀᴍᴇ':
        if '_' in message.content:
            msg = message.content.split("_")
            if (msg[0][0].isupper()):
                if(msg[1][0].isupper()):
                    channel = client.get_channel(1032251947589316629)
                    embedVar = discord.Embed(title="NAME CHECK", description="```You're name is in rp format. This name has been submitted to the admins !```", color=0x00ff00)
                    embedVar.set_image(url="https://media1.tenor.com/images/bf37e8dded18aaa840331bb87f99d3a9/tenor.gif")
                    embedadm = discord.Embed(title="IG WH REQUEST", description=F"```A whitelisted user has requested to whitelist an rp name which is in format. AKA {message.content}```", color=0x00ff00)
                    embedadm.set_image(url="https://media1.tenor.com/images/bf37e8dded18aaa840331bb87f99d3a9/tenor.gif")
                    channel = client.get_channel(1051131719106957462)
                    await channel.send(embed=embedadm)
                    role = client.get_guild(1032241486588297286).get_role(1036221612606902323)
                    await channel.send(role.mention)
                    await message.reply(embed=embedVar)
                else:
                    embedVar = discord.Embed(title="NAME CHECK", description="```This name is not in format !```", color=0x00ff00)
                    await message.reply(embed=embedVar)
            else:
                embedVar = discord.Embed(title="NAME CHECK", description="```This name is not in format !```", color=0x00ff00)
                await message.reply(embed=embedVar)
        else:
            embedVar = discord.Embed(title="NAME CHECK", description="```This name is not in format !```", color=0x00ff00)
            await message.reply(embed=embedVar)
            return
    if message.channel.name == "🎴║ᴅᴄᴄ-ᴄᴍᴅ":
        if "doesnt exist" in message.content:
            if message.author.id == 1055008754715873310:
                msg = message.content.split("(")
                s = msg[1].split(")")
                channel = client.get_channel(1032703167718244404)
                await channel.send(f"```{s[0]} were unable to be whitelisted since the user is not registered```")
        if "been whitelisted" in message.content:
            msg = message.content.split("(")
            message1 = msg[1]
            s = message1.split(")")
            channel = client.get_channel(1032703167718244404)
            await channel.send(f"```{s[0]} was successfully whitelisted !```")
        else:
            return
    for words in bad_words:
        if words in message.content:
           await message.delete()
client.run(TOKEN)