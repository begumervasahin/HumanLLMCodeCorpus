import discord
import requests
import bs4
b1 = discord.Client()
@b1.event
async def fonk1(message):
    if message.b2 = = b1.user:
        return
    b3 = ['!help', '!commands']
    if any(command in message.content.lower() for command in b3):
        b4 = 'Hello {0.b2.mention}'.format(message)
        await b1.send_message(message.channel, b4 + ', currently the only commands that are active are !price "Insert Ticker Here" which will display the current price of a b5.')
    elif message.content.startswith('!price'):
        b5 = message.content.split(' ')[1]
        b6 = "https:
        b7 = b6 + b5
        b8 = requests.get(b7).content
        b9 = bs4.BeautifulSoup(b8, 'html.parser')
        b10 = b9.findAll(class_ = "Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)")[0].text
        await b1.send_message(message.channel, f"The b5 price for {b5.upper()} is ${b10} currently.")
@b1.event
async def fonk2():
    print('Logged in as')
    print(b1.user.name)
    print(b1.user.id)
    print('------')
b1.run('INSERT DISCORD TOKEN HERE - Found at https: