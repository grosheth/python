from curses.panel import bottom_panel
from email import message
import os, discord, dotenv, asyncio
from random import randint
from discord.ext import tasks, commands

# Env variables
dotenv.load_dotenv()
intents = discord.Intents.all() 
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print('------')
	print(f"Chu pra")

@bot.event
async def on_voice_state_update(member, before, after):
	channel = bot.get_channel(os.getenv("TXTCHANNEL"))
	message = f"tyl {member.name}"
	print("test")
	if not before.channel:
		print(f"{member.name} joined {after.channel.name}")
		await bot.send_message(channel, message)
	if before.channel and not after.channel:
		print(f"user left channel")


@bot.event
async def on_member_join(member):
	channel = bot.get_channel(os.getenv("TXTCHANNEL"))
	await channel.send(f"Salut {member.display_name} bo bb sucre")

@bot.command(pass_context=True)
async def join(ctx):
    author = ctx.message.author
    channel = author.voice_channel
    await bot.join_voice_channel(channel)


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

	if message.content == "poll":
		await message.channel.send(embed=discord.Embed(title="Hey pioussies!", description=poll, color=0xeeafe6))

bot.run(os.getenv("TOKEN"))