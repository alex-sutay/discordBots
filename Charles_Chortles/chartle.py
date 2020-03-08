"""
author: Alex Sutay
file: chartle.py
"""

import discord
from data_manage import total_current, add_entry, find_average, add_to_current, scores_str, remove_last_input

TOKEN = 'NjQ2ODIwNTg1NTQ0MDg5NjEx.XdWssg.yxwhV7MV7wM36Z8cfNkSlmCwMqg'
client = discord.Client()


@client.event
async def on_message(message):
    channel = message.channel
    try:

        # if the bot sent the message, ignore it
        if message.author == client.user:
            return

        # if the message says "!help", send the help message
        if message.content == "!help":
            await channel.send("!help - this message\n!remove - remove the last score"
                               "\ndone - add the current score to the total as an image instance\n!average - display "
                               "the Charles Chortle average\n!total - display a summary of all the images so far")

        # if the message says "done", send the stats
        elif message.content == "done":
            total = total_current()
            add_entry()
            average = find_average()
            await channel.send("Total score for this image: "+str(total)+"\nAverage score overall: "+str(average))

        # if the message says "!remove", remove an image instance
        elif message.content.startswith("!remove"):
            remove_last_input()
            await channel.send("Removed the most recent score.")

        elif message.content == "!average":
            average = find_average()
            await channel.send("The current average score is: "+str(average))

        # if the message starts with "+", take that as a command adding to the score
        elif message.content.startswith('+'):
            if not str(message.author) == "ArseneLupin42#2757":
                try:
                    message_txt = message.content
                    message_txt = message_txt.split(" ")
                    message_txt = message_txt[0]
                    score = float(message_txt[1:])
                    add_to_current(str(message.author), score)
                    await channel.send(str(score) + " has been added to the score.")
                except Exception as e:
                    await channel.send(message.author.mention + " has caused an error and needs to do better!")
                    await channel.send("Error:" + str(e))

        # if the message is "!total", print the totals
        elif message.content == "!total":
            msg = scores_str()
            if len(msg) > 2000:
                msg = msg[-1999:]
            await channel.send(msg)

    except Exception as e:
        await channel.send("Uh oh, that did not work. Oops. Here's the error, someone should fix it.")
        await channel.send("Error:" + str(e))


@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)


client.run(TOKEN)
