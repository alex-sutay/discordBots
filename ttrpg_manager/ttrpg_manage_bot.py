"""
author: Alex Sutay
file: ttrpg_manage_bot.py
"""

import discord
from ttrpg_manager.config import TOKEN
from ttrpg_manager.data_manage import *


client = discord.Client()


# Functions called from the CMDs dict. They all take the message object that called them as a parameter
async def cmd_help(msg):
    """
    Private message the person who asked for help
    :param msg: the Message object that triggered this command
    :return: None
    """
    await msg.channel.send("A help message will exist here eventually!")


async def cmd_set_key(msg):
    """
    Change the key character for the guild that the message was sent in
    :param msg: the Message object that triggered this command
    :return: None
    """
    if len(msg.content.split(' ')) > 1:
        key_char = msg.content.split(' ')[1]
        set_key_char(msg.guild, key_char)
        await msg.channel.send("Key character updated! Your key character is now: " + key_char)
    else:
        await msg.channel.send("Use this command to set the key character for the server! (The character used to tell"
                               "the bot which messages are commands\n"
                               "Example: `!key .`")


async def cmd_create_object(msg):
    """
    Create a new object to be placed in someone's inventory
    :param msg: the Message object that triggered this command
    :return: None
    """
    await msg.channel.send("This will be the command for creating an object")


CMDs = {"help" : cmd_help,
        "key"  : cmd_set_key,
        "create" : cmd_create_object,
        }


@client.event
async def on_message(message):
    """
    This is the function called when a message is sent that the bot can see.
    :param message: the discord Message object
    :return: None
    """

    # if the bot sent the message, ignore it
    if message.author == client.user:
        return

    # First check if the first character is this guild's key character.
    key_char = get_key_char(message.guild)
    if message.content[0] == key_char:
        key = message.content.split(" ")[0][len(key_char):]  # this grabs the first word minus the key character
        if key in CMDs:
            await CMDs[key](message)


@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)


client.run(TOKEN)
