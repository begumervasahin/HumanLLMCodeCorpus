import discord
import requests
from bs4 import BeautifulSoup
client = discord.Client()
async def send_help_message(channel):
    help_msg = (
        "Hello! Currently, the only active command is `!price <Ticker>` "
        "which displays the current price of a stock."
    )
    await channel.send(help_msg)
async def send_stock_price(channel, ticker):
    try:
        url = f"https:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        price_element = soup.find(class_="Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)")
        if price_element:
            price = price_element.text
            await channel.send(f"The stock price for {ticker.upper()} is ${price} currently.")
        else:
            await channel.send("Sorry, I couldn't find the stock price.")
    except requests.RequestException:
        await channel.send("Sorry, I couldn't retrieve stock data. Please try again later.")
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    content = message.content.lower()
    if content in ['!help', '!commands']:
        await send_help_message(message.channel)
    elif content.startswith('!price'):
        ticker = content.split(' ')[1]
        await send_stock_price(message.channel, ticker)
@client.event
async def on_ready():
    print(f'Logged in as {client.user.name} (ID: {client.user.id})')
    print('------')
client.run('your_token_here')