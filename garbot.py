import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random


Client = discord.Client() #Initialise Client
prefix = "?"
client = commands.Bot(command_prefix=prefix) #Initialise client bot
time = time.time( )



@client.event 
async def on_ready():
    print("Bot is online and connected to Discord %s" %(time))  #This will be called when the bot connects t


@client.event
async def on_message(message):
     if message.content.upper().startswith('!SAY'):
        if message.author.id == "478881608531968004" or message.author.id == "477846372884807682":
            return
        elif message.author.id == "0" or message.author.id == "299154817354301440":
            await client.send_message(client.get_channel('472769528363745300'),"https://www.youtube.com/watch?v=QiFBgtgUtfw" , tts=True)
        else:
            args = message.content.split(" ")
            await client.send_message(client.get_channel('472769528363745300'), "%s" % (" ".join(args[1:])), tts=True)


async def background_loop():
    await client.wait_until_ready()
    while not client.is_closed:
        channel = client.get_channel("407251474771607570")
        messages = ["derr`mo", "suka", "otva`li","zatk`nis","b`lyad'!","`tchyo za ga`lima?", "po'shyol 'na hui", "mu'dak","`khu i","piz`da","ebat'","okhu`el?","eto piz`dets"]
        await client.send_message(channel, random.choice(messages), tts=True)
        await asyncio.sleep(600)

client.loop.create_task(background_loop())

client.run("NDc4ODgxNjA4NTMxOTY4MDA0.DlRJAw.XyQW8x1ycBTjfbxgqDsX0OtIh0w") 
