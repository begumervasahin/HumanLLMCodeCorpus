import json
import discord
from discord.ext import commands
import glob
import os
with open('config.json', 'r') as config_file:
    bot_config = json.load(config_file)
bot = commands.AutoShardedBot(command_prefix=commands.when_mentioned_or(bot_config.get("prefix", ".")))
bot.remove_command("help")
bot.config = bot_config
cog_modules = []
for file_path in glob.glob("cogs/*.py"):
    module_name = file_path.replace(os.path.sep, '.').replace('.py', '')
    cog_modules.append(module_name)
if __name__ == '__main__':
    for extension in cog_modules:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f"Failed to load extension {extension}: {e}")
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(status=discord.Status.idle,
                                                        name=bot.config["activity"],
                                                        type=discord.ActivityType.watching))
    print(f"Connected as {bot.user}")
    print("Ready!")
bot.run(bot_config.get("token"))