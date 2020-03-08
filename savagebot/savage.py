"""
author: Alex Sutay
file: chartle.py
"""

import discord
from deckman import *
from config import TOKEN

client=discord.Client()

@client.event
async def on_message(message):
    filepath = '/home/AlexS/discordbots/savagebot/decks/'
    channel = message.channel

    # if the bot sent the message, ignore it
    if message.author == client.user:
        return

    # if the message says "!help", send the help message
    if message.content == "!help":
        await channel.send('Deck management:\n!draw - draw a card\n!shuffle - shuffle all cards back together\n\
                \n!raise [target] [rolled] - calculate the number of raises')

    # if the message says "!draw", draw a card
    elif message.content == "!draw":
        card = draw_card(filepath + str(message.guild))
        if card.number == 0:
            await channel.send(message.author.mention + ' your card is a Joker!', file=discord.File(card.path))
        else:
            if card.number in range(2,11):
                number = str(card.number)
            elif card.number == 1:
                number = 'Ace'
            elif card.number == 11:
                number = 'Jack'
            elif card.number == 12:
                number = 'Queen'
            elif card.number == 13:
                number = 'King'
            await channel.send(message.author.mention + ' your card is the ' + number + ' of ' + card.suit + '!', file=discord.File(card.path))

    # if the message says "!shuffle", reset the deck and shuffle
    elif message.content == "!shuffle":
        await channel.send("Shuffling all cards!")
        new_deck(filepath + str(message.guild))

    elif message.content.startswith('!raise'):
        data = message.content
        data = data.split(' ')
        if len(data) == 3:
            target = int(data[1])
            rolled = int(data[2])
            raises = -1
            if target > rolled:
                (target, rolled) = (rolled, target)
            while rolled >= target:
                raises += 1
                rolled -=4
            await channel.send(str(raises) + ' raises!')
        else:
            await channel.send('usage: !raise [target] [rolled]')


@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)


client.run(TOKEN)
