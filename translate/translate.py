"""
author: Alex Sutay
file: chartle.py
"""

import discord
from googletrans import Translator
translator = Translator()
from config import TOKEN

client = discord.Client()


@client.event
async def on_message(message):
    channel = message.channel
    content = message.content

    # if the bot sent the message, ignore it
    if message.author == client.user:
        return

    # if the message starts with "!translate", send a dm of the translation
    if content.startswith("!translate"):
        prev = 1
        if len(content) > 10:
            content = content.split(' ')
            prev = int(content[1])
        await message.delete()
        history = await channel.history(limit=prev).flatten()
        trans_text = history[prev-1].content
        new_text = translator.translate(trans_text)
        await message.author.send("Original:" + trans_text + "\nTranslated: " + new_text.text)


@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)


client.run(TOKEN)
