import json
import discord
from discord.ext import commands
import glob
import os
def fonk1(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)
def fonk2(b2):
    b1 = commands.AutoShardedBot(command_prefix=commands.when_mentioned_or(b2.get("prefix", ".")))
    b1.remove_command("help")
    b1.b2 = b2
    return b1
def fonk3(path_pattern):
    return [file.replace(os.path.sep, '.').replace('.py', '') for file in glob.glob(path_pattern)]
def fonk4(b1, b7):
    for extension in b7:
        try:
            b1.load_extension(extension)
            print(f"Successfully loaded extension {extension}")
        except Exception as e:
            print(f"Failed to load extension {extension} : {e}")
@b1.event
async def fonk5():
    await b1.change_presence(
        b3 = discord.Activity(
            b4 = discord.Status.idle,
            b5 = b2["b3"],
            b6 = discord.ActivityType.watching
        )
    )
    print(f"Connected as {b1.user}")
    print("Ready!")
def fonk6():
    b2 = fonk1('b2.json')
    b1 = fonk2(b2)
    b7 = fonk3("cogs/*.py")
    fonk4(b1, b7)
    b1.run(b2.get("token"))
if b8 = = '__main__':
    fonk6()