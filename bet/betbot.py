"""
author: Alex Sutay
file: betbot.py
"""

import discord
from config import TOKEN

client = discord.Client()


@client.event
async def on_message(message):
    channel = message.channel
    content = message.content

    # if the bot sent the message, ignore it
    if message.author == client.user:
        return

    # If the message contains "bet", react with bet
    content = content.split()
    for item in content:
        if "Β" in item or "Ε" in item:
            item = "bet"
        item = item.lower()
        item = item.translate({ord('*'): None})
        if item == "bet":
            emoji = await message.guild.fetch_emoji(684988702954749974)
            await message.add_reaction(emoji)
            await channel.send("bet", tts=True)


@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)


client.run(TOKEN)
