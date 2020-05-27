import discord
import asyncio
import aiohttp


TOKEN = ""

client = discord.Client()

bugreportchannel = "af1hd-testing"

@client.event
async def on_ready():
    print("----------")
    print(client.user.name)
    print("----------")
    print("guilds")
    for guild in client.guilds:
        print(guild)
    print("----------")
    guilds = len([s for s in client.guilds])
    activity = discord.Game(name="af1 | " + (str(guilds)) + " guilds")
    await client.change_presence(activity=activity)


@client.event
async def on_message(message):
    # bug report channel for dev server
    if (message.channel.name) == (bugreportchannel):
        if message.author != client.user:
            if "bug" in message.content:
                await message.add_reaction("✅")
                await message.add_reaction("♻️")



@client.event
async def on_reaction_add(reaction, user):
    if "bug" in reaction.message.content:
        if str(reaction.message.channel.name) == (bugreportchannel):
            messagek = str(reaction.message.content)
            if str(reaction.emoji) == "✅":
                tickperson = user
                if user == client.user:
                    return
                role = discord.utils.get(reaction.message.guild.roles, name = "Developer")
                if role in reaction.message.author.roles:
                    if reaction.message.attachments:
                        urles = await reaction.message.attachments[0].save("/Users/snakeshavelegs/Documents/slightlycold.png")
                        await reaction.message.delete()
                    for channel in reaction.message.guild.channels:
                        if channel.name == "af1hd-development":
                            channes = client.get_channel(channel.id)


                            embed = discord.Embed(
                            title = "Reporter: " + str((reaction.message.author)),
                            description = ((messagek) + "\n" + (reaction.message.author.mention)),
                            colour = discord.Colour.blue()
                            )
                            embed.set_footer(text = "ticked by: " + str(user))
                            await channes.send(embed=embed)

                            print("DONE")
                            if reaction.message.attachments:
                                with open('/Users/snakeshavelegs/Documents/slightlycold.png') as f:
                                    picturexd = discord.File(f)
                                    await channes.send(file=discord.File('/Users/snakeshavelegs/Documents/slightlycold.png'))





        if str(reaction.emoji) == "♻️":
            if "bug" in reaction.message.content:
                tickperson = user
                if user == client.user:
                    return
                role = discord.utils.get(reaction.message.guild.roles, name = "Developer")
                if role in reaction.message.author.roles:
                    await reaction.message.author.send(user.mention + " deleted this post you made in bug reports;")



                    if reaction.message.content:
                        print("CONTENT")
                        await reaction.message.author.send(reaction.message.content)
                    else:
                        await reaction.message.author.send("no message content....")
                    if reaction.message.attachments:
                        with open('/Users/snakeshavelegs/Documents/slightlycold.png') as f:
                            picturexd = discord.File(f)
                            urlesdelete = await reaction.message.attachments[0].save("/Users/snakeshavelegs/Documents/slightlycold.png")

                            await reaction.message.author.send(file=discord.File('/Users/snakeshavelegs/Documents/slightlycold.png'))
                    await reaction.message.delete()

client.run(TOKEN)
