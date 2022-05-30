import discord, os, dotenv
from random import randint


dotenv.load_dotenv()
# GETS THE CLIENT OBJECT FROM DISCORD.PY. CLIENT IS SYNONYMOUS WITH BOT.
bot = discord.Client()
TOKEN = os.getenv("TOKEN")
# EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.
@bot.event
async def on_ready():
	# CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
	guild_count = 0

	# LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
	for guild in bot.guilds:
		# PRINT THE SERVER'S ID AND NAME.
		print(f"- {guild.id} (name: {guild.name})")

		# INCREMENTS THE GUILD COUNTER.
		guild_count = guild_count + 1

	# PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
	print("SampleDiscordBot is in " + str(guild_count) + " guilds.")

# EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL.
@bot.event
async def on_message(message):

	games = {
		1:"https://garticphone.com/lobby",
		2:"https://songtrivia2.io/",
		3:"https://world-geography-games.com/en/flags_world.html",
		4:"https://www.geoguessr.com/"
	}
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
	

	
bot.run(TOKEN)