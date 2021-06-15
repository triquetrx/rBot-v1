import discord
from discord.ext import commands
import os
import requests
import json
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from keep_alive import keep_alive


client = commands.Bot(command_prefix="rbot ")

@client.event
async def onReady():
    print("Bot is Ready")


@client.command()
async def ping(ctx):
    await ctx.send(f'pong!! {round(client.latency * 1000)} ms')


@client.command()
async def roast(ctx, arg):
    fName = arg
    lName = ""
    url = ("http://api.icndb.com/jokes/random?firstName=" +
           str(fName)+"&lastName="+str(lName))
    res = requests.get(url)
    jdata = json.loads(res.text)
    joke = jdata["value"]["joke"]
    await ctx.send(joke)

# client.command()
# async def play(ctx, query: str):
#    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
#    api_service_name = "youtube"
#    api_version = "v3"
#    client_secrets_file = "AIzaSyDt5bqT2O3k-YuhKj8rCM6Wv3k0XHc5Fi0.json"
#    await ctx.send("Playing")
#    youtube = build("youtube", "v3", developerKey=key)
#    search_response = youtube.search().list(q== < query >, part="id,snippet", maxResults=5).execute()
#    await ctx.send(search_response)

@ client.command()
async def WTF(ctx):
    await ctx.channel.send("To call me start by typing rbot ;)")


@ client.command()
async def joke(ctx, arg):
  try:
    if arg == '':
      await ctx.send("provide an option dufus!!")
    elif arg == '0':
        response = requests.get(
            "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw&type=single")
        jdata = json.loads(response.text)
        riddle = jdata["joke"]
        await ctx.send(riddle)
    elif arg == 1:
        response = requests.get(
            "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw&type=single")
        jdata = json.loads(response.text)
        riddle = jdata["joke"]
        await ctx.send(riddle)
    elif arg == 2:
        response = requests.get(
            "https://v2.jokeapi.dev/joke/Any?type=single")
        jdata = json.loads(response.text)
        riddle = jdata["joke"]
        await ctx.send(riddle)
    else:
        response = requests.get(
            "https://v2.jokeapi.dev/joke/Any?type=twopart")
        jdata = json.loads(response.text)
        riddle = jdata["setup"]
        answer = jdata["delivery"]
        await ctx.send("Q:"+riddle)
        await ctx.send("A:"+answer)
  except:
    await ctx.send("Provide an option dufus!!!")


@ client.command()
async def meme(ctx):
    response = requests.get("https://reddit-meme-api.herokuapp.com/")
    jdata = json.loads(response.text)
    image = jdata["url"]
    await ctx.send(image)


@ client.command()
async def momma(ctx):
    response = requests.get("https://api.yomomma.info/")
    jdata = json.loads(response.text)
    joke = jdata["joke"]
    await ctx.send(joke)


@ client.command()
async def hello(ctx):
    await ctx.channel.send('Hello!!! \n How to use Commands \n to call me start with rbot \n commands: roast #nameOfUserToRoast \n rbot joke \n rbot meme \n rbot momma \n rbot joke #options(1 to 4)')

keep_alive()
discordToken = os.getenv('TOKEN')
client.run(discordToken)

