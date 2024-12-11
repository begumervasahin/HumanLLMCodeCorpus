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
b3 = []
for file in glob.glob("cogs/*.py"):
    b3.append(file.replace(os.path.sep, '.').replace('.py', ''))
if b4 = = '__main__':
    for extension in b3:
        try:
            b2.load_extension(extension)
        except Exception as e:
            print(f"Failed to load extension {extension}: {e}")
@b2.event
async def fonk1():
    await b2.change_presence(b5 = discord.Activity(status=discord.Status.idle,
                                                        b6 = b1["b5"],
                                                        b7 = discord.ActivityType.watching))
    print(f"Connected as {b2.user}")
    print("Ready!")
b2.run(b1.get("token"))