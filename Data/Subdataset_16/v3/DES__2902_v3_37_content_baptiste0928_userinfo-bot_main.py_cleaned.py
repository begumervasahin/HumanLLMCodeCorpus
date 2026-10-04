import json
import discord
from discord.ext import commands
import glob
import os
def fonk1():
    with open('b2.json', 'r') as f:
        return json.load(f)
def fonk2(b2):
    b1 = commands.AutoShardedBot(command_prefix=commands.when_mentioned_or(b2.get("prefix", ".")))
    b1.remove_command("help")
    b1.b2 = b2
    return b1
def fonk3(b1):
    b3 = [file.replace(os.path.sep, '.').replace('.py', '') for file in glob.glob("b3/*.py")]
    for cog in b3:
        try:
            b1.load_extension(cog)
            print(f"Successfully loaded extension {cog}")
        except Exception as e:
            print(f"Failed to load extension {cog}: {e}")
@b1.event
async def fonk4():
    await b1.change_presence(
        b4 = discord.Activity(
            b5 = discord.Status.idle,
            b6 = b2["b4"],
            b7 = discord.ActivityType.watching
        )
    )
    print(f"Connected as {b1.user}")
    print("Ready!")
def fonk5():
    b2 = fonk1()
    b1 = fonk2(b2)
    fonk3(b1)
    b1.run(b2.get("token"))
if b8 = = '__main__':
    fonk5()