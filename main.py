import discord
import json 

with open("config.json") as f:
    config = json.load(f)

TOKEN = config.get("TOKEN")
PREFIX = config.get("PREFIX")
AS = config.get("Anigame Sniper")
IS = config.get("Izzi Sniper")

client = discord.Client() 

@client.event
async def on_ready():
    print(f"logged in as {client.user}")
    if config.get('Anigame Sniper') == "y":
        a = "ON"
    else:
        a = "OFF"
    print(f"Anigame Sniper - {a}") 
    if config.get('Izzi Sniper') == "y":
        a = "ON"
    else:
        a = "OFF"
    print(f"Izzi Sniper - {a}")
    

@client.event
async def on_message(msg):
    if AS == "y":
        if msg.author.id == 571027211407196161:
            try:
                embeds = msg.embeds
                for embed in msg.embeds:
                        d = (embed.to_dict()['description'])
                        if d == "*A wild anime card appears!*": 
                            a = (embed.to_dict()['footer'])
                            text = (a['text'])
                        else:
                            return  
                r = text.split()
                li = [r[1] , r[2]]
                kek = ' '.join([str(elem) for elem in li])
                await msg.channel.send(kek)
            except:
                pass
    
    if IS == "y":
        if msg.author.id == 784851074472345633:
            try:
                if msg.author.id == 784851074472345633:
                    embeds = msg.embeds
                    for embed in msg.embeds:
                        d = (embed.to_dict()['description'])
                        if d.endswith("appeared._"):
                            a = (embed.to_dict()['footer'])
                            text = (a['text'])
                        
                        else:
                            return 
                        r = text.split()
                        li = [r[1] , r[2] , r[5]]
                        kek = ' '.join([str(elem) for elem in li])
                        await msg.channel.send(kek)
            except:
                pass

client.run(TOKEN, bot=False)