import json
import discord
from discord.ext import commands
import glob
import os
with open('b3.json', 'r') as config_file:
    b1 = json.load(config_file)
b2 = commands.AutoShardedBot(command_prefix=commands.when_mentioned_or(b1.get("prefix", ".")))
b2.remove_command("help")
b2.b3 = b1
b4 = []
for file_path in glob.glob("cogs/*.py"):
    b5 = file_path.replace(os.path.sep, '.').replace('.py', '')
    b4.append(b5)
if b6 = = '__main__':
    for extension in b4:
        try:
            b2.load_extension(extension)
        except Exception as e:
            print(f"Failed to load extension {extension}: {e}")
@b2.event
async def fonk1():
    await b2.change_presence(b7 = discord.Activity(status=discord.Status.idle,
                                                        b8 = b2.b3["b7"],
                                                        b9 = discord.ActivityType.watching))
    print(f"Connected as {b2.user}")
    print("Ready!")
b2.run(b1.get("token"))