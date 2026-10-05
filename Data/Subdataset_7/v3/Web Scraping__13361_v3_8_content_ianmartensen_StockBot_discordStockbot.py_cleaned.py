import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
b1 = commands.Bot(command_prefix='!')
def fonk1(ticker):
    b2 = "https:
    b3 = requests.get(f"{b2}{ticker}").content
    b4 = BeautifulSoup(b3, 'html.parser')
    b5 = b4.find(class_="Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)")
    if b5:
        return b5.text
    else:
        return None
@b1.command(b6 = 'price')
async def fonk2(ctx, *, ticker: str):
    b7 = fonk1(ticker)
    if b7:
        await ctx.send(f"The stock price for {ticker.upper()} is ${b7} currently.")
    else:
        await ctx.send(f"Could not find the stock price for {ticker.upper()}.")
@b1.command(b6 = 'help', hidden=True)
async def fonk3(ctx):
    b8 = "Hello! Here are the commands you can use:\n"
    b8 += "`!price <TICKER>`: Gets the current price of the specified stock ticker.\n"
    await ctx.send(b8)
@b1.event
async def fonk4():
    print(f'Logged in as {b1.user.b6}')
    print(f'User ID: {b1.user.id}')
    print('------ Ready to go!')
b1.run('INSERT_DISCORD_TOKEN_HERE')
