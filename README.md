# discordBots
A collection of discord bots I built. They don't do much, just a couple small things to make my servers more interesting
Each one uses a seperate config.py file to change the token and other details that change from server to server.
For each instance of each bot, it's important that you get your own token and add it to the config file or it will not work.
You can get a token from the discord developer portal.

Here's a breakdown of each bot:

Bread Bot:
Bread Bot is a joke bot that selects a random a random type of bread and grabs the link to the wikipedia page about it.
Then, at 8 am, it send a message reading "Rise and grind, let's get this bread. Today's bread is..." then proceeds to post the bread type and link.
Also, if anyone says the word "bread" it will react to the message with the bread emoji.

Charles Chortle:
The Charles Chortle Bot is named after my friend Charles. It allows you to rate memes that people send to the server.
It should automatically detect whenever someone sends a meme and start accepting ratings, which are messages starting with a "+".
Example valid rating messages: "+0", "+10 good meme", "+-5", "+-10 I hate it."
It will create files to remember these ratings to create an average, however the bot is currently in development, so not everything works
exactly as I would like it to.

Bet Bot:
I'm not sure how well this one will work for anyone else. It reacts to messages that say "bet" with a bet emoji and a tts bet message.
Because it uses my emoji, it wouldn't necesarily work for anyone else. If you want me to, I can move the emoji reaction to the config
file so you can have it react with a different emoji of your choice.

Savage Bot:
A bot built to do some of the functions of Savage Worlds (a ttrpg). It has deck management as well as a raise calculator.
I don't remember finishing it, I don't remember what all it can do. Try !help.

Translate Bot:
This bot translates messages. By sending "!translate", it will delete your message and dm you a translation.
That way it doesn't clutter the server with translations and just the person who needed it will receive the translation. 
If you missed the message, you can add a number to the message to get a translation of an old message, for example
"!translate 3" will translate the third most recent message, not including the translation request message
