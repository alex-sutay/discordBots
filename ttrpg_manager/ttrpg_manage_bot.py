"""
author: Alex Sutay
file: ttrpg_manage_bot.py
"""

import discord
from .config import TOKEN
from .data_manage import get_key_char


client = discord.Client()


# Functions called from the CMDs dict. They all take the message object that called them as a parameter
def cmd_help(msg):
    """
    Private message the person who asked for help
    :param msg: the Message object that triggered this command
    :return: None
    """
    msg.channel.send("A help message will exist here eventually!")


def cmd_set_key(msg):
    """
    Change the key character for the guild that the message was sent in
    :param msg: the Message object that triggered this command
    :return: None
    """
    msg.channel.send("This will eventually let you change the \"Key Character\" (!)")


def cmd_create_object(msg):
    """
    Create a new object to be placed in someone's inventory
    :param msg: the Message object that triggered this command
    :return: None
    """
    msg.channel.send("This will be the command for creating an object")


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
            CMDs[key](message)


client.run(TOKEN)
