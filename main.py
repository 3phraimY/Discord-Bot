# team1 = "key"
# team2 = "key"
team3 = "Key"
 #IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.

import discord
import requests
import random

# {"conversationId":"073a6739-fb40-4ea5-b63d-f2bf78287150","source":"instruct"}

 #GETS THE CLIENT OBJECT FROM DISCORD.PY. CLIENT IS SYNONYMOUS WITH BOT.
bot = discord.Client(intents=discord.Intents.all())

 #EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.
@bot.event
async def on_ready():
    # CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
    guild_count = 0

    # LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
    for guild in bot.guilds:
        # PRINT THE SERVER'S ID AND NAME.
        print(f"- {guild.id} (name: {guild.name})")

        # INCREMENTS THE GUILD COUNTER.
        guild_count = guild_count + 1

    # PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
    print(bot.guilds)

 #EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL.
@bot.event
async def on_message(message):
    #stop if bot is posting to prevent infinite looping
    if(message.author.bot):
        return
    currentMessage = message.content
    words = []
    prevStartingPosition = 0
    currentPostion = -1

    currentMessage += " "

    for i in range(0, len(currentMessage)):
        currentPostion = currentPostion + 1
        if(currentMessage[i] == ' '):
            words += [currentMessage[prevStartingPosition:i]]
            # add the previous word to the words list
            prevStartingPosition = i
        
    # send random word
    # await get_top_gifs(random.choice(words), message)

    # search for full message
    await get_top_gifs(currentMessage, message)



# set the apikey and limit
TENOR_API_KEY = 'AIzaSyDYcqJ9p0yqJ-uIF0hdY57EcVt3Rw4AikQ'

client = discord.Client(intents=discord.Intents.default())

# Function to get the top 8 GIF URLs from Tenor for a search term
async def get_top_gifs(search_term, message):
        # set the apikey and limit
    apikey = "AIzaSyDYcqJ9p0yqJ-uIF0hdY57EcVt3Rw4AikQ"  # click to set to your apikey
    lmt = 1
    ckey = "my_test_app"  # set the client_key for the integration and use the same value for all API calls


    # get the top 8 GIFs for the search term
    r = requests.get(
        "https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" % (search_term, apikey, ckey,  lmt))

    if r.status_code == 200:
        # load the GIFs using the urls for the smaller GIF sizes
        json = r.json()
        gif_url = json['results'][0]['url']
        print(gif_url)
        await message.channel.send(gif_url)

        # Print found URLs
        print("Found URLs:")
    else:
        print("error")

@client.event
async def on_ready():
    print(f'Bot {client.user} is now online.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Use the user's entire message as the search term
    search_term = message.content.strip()
    if search_term:
        gif_urls = get_top_gifs(search_term)
        if gif_urls:
            # Send the top GIF URLs to the Discord channel
            for gif_url in gif_urls:
                await message.channel.send(gif_url)
        else:
            await message.channel.send("Sorry, I couldn't find any GIFs for that search term.")
    else:
        await message.channel.send("Please type something to search for GIFs.")

bot.run(team3)
