import os, dotenv, asyncio
from random import randint
from discord.ext import tasks, commands

# initier le bot
bot = commands.Bot(commands_prefix="!")

dotenv.load_dotenv()
TOKEN = os.getenv("TOKEN")
PREFIX = os.getenv("PREFIX")
TXTCHANNEL = os.getenv("TXTCHANNEL")

@bot.event
async def on_ready():
	print(f"Chu pra")

	@tasks.loop(seconds=10.0)
	async def send_message():
		bot.get_channel(TXTCHANNEL)
		await channel.typing()
		await channel.send("hey Filou, suce-la")

	send_message.start()


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
