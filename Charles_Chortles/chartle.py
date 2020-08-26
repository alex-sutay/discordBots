"""
author: Alex Sutay
file: chartle.py
"""

import discord
from Charles_Chortles.data_manage import total_current, add_entry, find_average, add_to_current, scores_str, \
    remove_last_input, set_current, AuthorException, get_current
from Charles_Chortles.config import TOKEN

client = discord.Client()


@client.event
async def on_message(message):
    channel = message.channel
    text = message.content
    try:

        # if the bot sent the message, ignore it
        if message.author == client.user:
            return

        # If the message contains an image, assume it's a meme and set the current user to be rated to the author
        if len(message.attachments) > 0:
            set_current(message.author)

        # if the message says "!help", send the help message
        if text == "!help":
            # await channel.send("!help - this message\n!remove - remove the last score"
            #                   "\ndone - add the current score to the total as an image instance\n!average - display "
            #                   "the Charles Chortle average\n!total - display a summary of all the images so far")
            await channel.send("Currently under maintenance. Bug me and I might fix this.")

            """
            # if the message says "done", send the stats
            elif message.content == "done":
                total = total_current()
                add_entry()
                average = find_average()
                await channel.send("Total score for this image: "+str(total)+"\nAverage score overall: "+str(average))
            """

        # if the message says "!remove", remove an image instance
        elif text.startswith("!remove"):
            # remove_last_input()
            # await channel.send("Removed the most recent score.")
            await channel.send("Currently under maintenance. Bug me and I might fix this.")

        elif message.content == "!average":
            average = find_average()
            current = get_current()
            await channel.send("The current average score for" + current + " is: "+str(average))

        elif message.content == "!current":
            current = get_current()
            await channel.send("The current user is " + current)

        # if the message starts with "+", take that as a command adding to the score
        elif message.content.startswith('+'):
            try:
                message_txt = message.content
                message_txt = message_txt.split(" ")
                message_txt = message_txt[0]
                score = float(message_txt[1:])
                add_to_current(str(message.author), score)
                await channel.send(str(score) + " has been added to the score.")
            except AuthorException as e:
                await channel.send("You can't rate your own meme")
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
