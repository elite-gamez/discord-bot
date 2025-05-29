import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"✅ Logged in as {bot.user.name}")

@bot.tree.command(name="hello", description="Say hello!")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("👋 Hello from Render!")

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong!")

bot.run(os.environ["DISCORD_TOKEN"])
