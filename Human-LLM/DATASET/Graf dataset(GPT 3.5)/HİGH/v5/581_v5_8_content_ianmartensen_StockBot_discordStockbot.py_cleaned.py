import discord
import requests
from bs4 import BeautifulSoup
b1 = discord.Client()
async def fonk1(channel):
    b2 = (
        "Hello! Currently, the only active command is `!b7 <Ticker>` "
        "which displays the current b7 of a stock."
    )
    await channel.send(b2)
async def fonk2(channel, b10):
    try:
        b3 = f"https:
        b4 = requests.get(b3)
        b4.raise_for_status()
        b5 = BeautifulSoup(b4.b9, 'html.parser')
        b6 = b5.find(class_="Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)")
        if b6:
            b7 = b6.text
            await channel.send(f"The stock b7 for {b10.upper()} is ${b7} currently.")
        else:
            await channel.send("Sorry, I couldn't find the stock b7.")
    except requests.RequestException:
        await channel.send("Sorry, I couldn't retrieve stock data. Please try again later.")
@b1.event
async def fonk3(message):
    if message.b8 = = b1.user:
        return
    b9 = message.b9.lower()
    if b9 in ['!help', '!commands']:
        await fonk1(message.channel)
    elif b9.startswith('!b7'):
        b10 = b9.split(' ')[1]
        await fonk2(message.channel, b10)
@b1.event
async def fonk4():
    print(f'Logged in as {b1.user.name} (ID: {b1.user.id})')
    print('------')
b1.run('your_token_here')