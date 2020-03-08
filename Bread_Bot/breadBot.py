"""
author: Alex Sutay
file: Bread Bot.py
"""

import discord
import asyncio
from datetime import datetime
import urllib.request
import random
from config import TOKEN

client = discord.Client()


@client.event
async def on_message(message):
    channel = message.channel
    if message.content == "TEST":
        fp = urllib.request.urlopen("https://en.wikipedia.org/wiki/List_of_breads")
        mybytes = fp.read()
        mystr = mybytes.decode("utf8")
        fp.close()
        index1 = mystr.find('<tbody>')
        index2 = mystr.find('</tbody>')
        if index1 > 0:
            # isolate the table
            mystr = mystr[index1+7:index2]

            # remove header row
            index1 = mystr.find("</tr>")
            mystr = mystr[index1+6:]

            # divide the the table into rows
            mystr = mystr.split('<tr>')

            # pick a random row and remove it
            rand = random.randint(0, len(mystr)-1)
            row = mystr[rand]

            # find and remove the name of the bread
            name_index1 = row.find('">') + 2
            name_index2 = row.find('</a>')
            bread_name = row[name_index1:name_index2]

            # find and save the link
            bread_link = 'https://en.wikipedia.org/'
            link_index1 = row.find('wiki')
            link_index2 = row.find('" title')
            bread_link += row[link_index1:link_index2]

            # create the final message and send it
            msg = "Good morning everyone! Rise and grind, let's get this bread. Today's bread is "
            msg += bread_name + '!\n('
            msg += bread_link + ')'
            await channel.send(msg)

    # the bread reaction method
    if "bread" in message.content or "Bread" in message.content:
        await message.add_reaction('🍞')


@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    channel = client.get_channel(459365635093299201)
    while True:
        now = datetime.now()
        hour = int(now.strftime("%H"))
        if hour == 8:
            # unleash the bread
            fp = urllib.request.urlopen("https://en.wikipedia.org/wiki/List_of_breads")
            mybytes = fp.read()
            mystr = mybytes.decode("utf8")
            fp.close()
            index1 = mystr.find('<tbody>')
            index2 = mystr.find('</tbody>')
            if index1 > 0:
                # isolate the table
                mystr = mystr[index1 + 7:index2]

                # remove header row
                index1 = mystr.find("</tr>")
                mystr = mystr[index1 + 6:]

                # divide the the table into rows
                mystr = mystr.split('<tr>')

                # pick a random row and remove it
                rand = random.randint(0, len(mystr) - 1)
                row = mystr[rand]

                # find and remove the name of the bread
                name_index1 = row.find('">') + 2
                name_index2 = row.find('</a>')
                bread_name = row[name_index1:name_index2]

                # find and save the link
                bread_link = 'https://en.wikipedia.org/'
                link_index1 = row.find('wiki')
                link_index2 = row.find('" title')
                bread_link += row[link_index1:link_index2]

                # create the final message and send it
                msg = "Good morning everyone! Rise and grind, let's get this bread. Today's bread is "
                msg += bread_name + '!\n('
                msg += bread_link + ')'
                await channel.send(msg)
            await asyncio.sleep(3600)
        else:
            await asyncio.sleep(60)




client.run(TOKEN)
