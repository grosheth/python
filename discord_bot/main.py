import os, discord, dotenv, asyncio
from random import randint
from discord.ext import tasks, commands
import my_messages

# Env variables
dotenv.load_dotenv()
TOKEN = os.getenv("TOKEN")
PREFIX = os.getenv("PREFIX")
TXTCHANNEL = os.getenv("TXTCHANNEL")
VOICECHANNEL = os.getenv("VOICECHANNEL")

# importer les intents
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

messages = my_messages()

@bot.event
async def on_ready():
	print(f"Chu pra")

@bot.event
async def on_member_join(member):
	channel = bot.get_channel(TXTCHANNEL)
	await channel.send(f"Salut {member.display_name} bo bb sucre")




bot.run(TOKEN)
