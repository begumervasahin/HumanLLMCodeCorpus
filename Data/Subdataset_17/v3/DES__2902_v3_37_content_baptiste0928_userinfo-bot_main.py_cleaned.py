import json
import discord
from discord.ext import commands
import glob
import os
def load_config():
    with open('config.json', 'r') as f:
        return json.load(f)
def initialize_bot(config):
    bot = commands.AutoShardedBot(command_prefix=commands.when_mentioned_or(config.get("prefix", ".")))
    bot.remove_command("help")
    bot.config = config
    return bot
def load_cogs(bot):
    cogs = [file.replace(os.path.sep, '.').replace('.py', '') for file in glob.glob("cogs/*.py")]
    for cog in cogs:
        try:
            bot.load_extension(cog)
            print(f"Successfully loaded extension {cog}")
        except Exception as e:
            print(f"Failed to load extension {cog}: {e}")
@bot.event
async def on_ready():
    await bot.change_presence(
        activity=discord.Activity(
            status=discord.Status.idle,
            name=config["activity"],
            type=discord.ActivityType.watching
        )
    )
    print(f"Connected as {bot.user}")
    print("Ready!")
def main():
    config = load_config()
    bot = initialize_bot(config)
    load_cogs(bot)
    bot.run(config.get("token"))
if __name__ == '__main__':
    main()