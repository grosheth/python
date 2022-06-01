import discord, os, dotenv, asyncio 
from random import randint
from discord.ext import tasks, commands


client = commands.Bot(command_prefix='!')
dotenv.load_dotenv()
bot = discord.Client()
TOKEN = os.getenv("TOKEN")
PREFIX = os.getenv("PREFIX")
CHANNEL = os.getenv("CHANNEL")

@tasks.loop(seconds=10.0)
async def send_message(test):
	if test == "test":
		await send("hey Filou, suce-la")

@bot.event
async def on_ready():
	guild_count = 0
	for guild in bot.guilds:
		print(f"- {guild.id} (name: {guild.name})")
		guild_count = guild_count + 1

	print("SampleDiscordBot is in " + str(guild_count) + " guilds.")
	test = "test"
	send_message.start(test)

@bot.event
async def on_message(message):

	poll = message.content
	games = {
		1:"https://garticphone.com/lobby",
		2:"https://songtrivia2.io/",
		3:"https://world-geography-games.com/en/flags_world.html",
		4:"https://www.geoguessr.com/"
	}
	memes = {
		1:"https://www.pornhub.com/categories/hentai"
	}

	# games
	if message.content == "gartic":
		await message.channel.send(games[1])
	if message.content == "songtrivia":
		await message.channel.send(games[2])
	if message.content == "flags":
		await message.channel.send(games[3])
	if message.content == "geo":
		await message.channel.send(games[4])
	if message.content == "random game":
		await message.channel.send(games[randint(1, len(games))])

	# memes
	if message.content == "hey bb veux tu une garette pi ecouter des hentai tranquille?":
		await message.channel.send(memes[1])

	if message.content == "!poll":
		await message.channel.send(embed=discord.Embed(title="Hey pioussies!", description=poll, color=0xeeafe6))


bot.run(TOKEN)
