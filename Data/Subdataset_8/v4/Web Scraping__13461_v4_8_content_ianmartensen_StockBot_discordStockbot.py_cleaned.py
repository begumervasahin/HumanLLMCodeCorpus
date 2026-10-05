import discord
import requests
import bs4
client = discord.Client()
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    commands_list = ['!help', '!commands']
    if any(command in message.content.lower() for command in commands_list):
        msg = f'Hello {message.author.mention}, currently the only commands that are active are !price "Insert Ticker Here" which will display the current price of a stock.'
        await message.channel.send(msg)
    elif message.content.startswith('!price'):
        stock = message.content.split(' ')[1]
        url = "https:
        full_url = url + stock
        response = requests.get(full_url).content
        soup = bs4.BeautifulSoup(response, 'html.parser')
        stock_price = soup.find(class_="Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)").text
        await message.channel.send(f"The stock price for {stock.upper()} is ${stock_price} currently.")
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
client.run('INSERT DISCORD TOKEN HERE')