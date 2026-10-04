import json
import discord
from discord.ext import commands
import glob
import os
with open('b1.json', 'r') as f:
    b1 = json.load(f)
b2 = commands.AutoShardedBot(command_prefix=commands.when_mentioned_or(b1.get("prefix", ".")))
b2.remove_command("help")
b2.b1 = b1
def fonk1():
    b3 = [file.replace(os.path.sep, '.').replace('.py', '') for file in glob.glob("b3/*.py")]
    for cog in b3:
        try:
            b2.load_extension(cog)
            print(f"Successfully loaded extension {cog}")
        except Exception as e:
            print(f"Failed to load extension {cog}: {e}")
if b4 = = '__main__':
    fonk1()
@b2.event
async def fonk2():
    await b2.change_presence(
        b5 = discord.Activity(
            b6 = discord.Status.idle,
            b7 = b1["b5"],
            b8 = discord.ActivityType.watching
        )
    )
    print(f"Connected as {b2.user}")
    print("Ready!")
b2.run(b1.get("token"))