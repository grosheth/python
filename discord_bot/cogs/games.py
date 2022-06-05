from ast import alias
import asyncio, os, discord
from discord.ext import commands
from random import randint

class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="!gamelink et spécifier le jeu")
    async def gamelink(self, ctx, arg):
        games = {
            1:"https://garticphone.com/lobby",
            2:"https://songtrivia2.io/",
            3:"https://world-geography-games.com/en/flags_world.html",
            4:"https://www.geoguessr.com/"
        }
        if arg == "all":
            await ctx.send(games)
        if arg == "gartic":
            await ctx.send(games[1])
        if arg == "songtrivia":
            await ctx.send(games[2])
        if arg == "flags":
            await ctx.send(games[3])
        if arg == "geo":
            await ctx.send(games[4])
        if arg == "random game":
            await ctx.send(games[randint(1, len(games))])
    

    @commands.command(brief="!coinflip <pile> <face>")
    async def coinflip(self, ctx, arg):
        arg = arg.lower()
        if arg != "pile" and arg != "face":
            await ctx.send(f"{arg} n'est pas un choix à Pile ou face. Bravo")
            return
        
        guesses = {
            1:"pile",
            2:"face"
        }
        guess = randint(1,2)
        await ctx.send("...")
        await asyncio.sleep(1)
        await ctx.send("...La tension monte...")
        if ctx.author.id == 388902413358071819:
            await ctx.send("...")
            await asyncio.sleep(1)
            await ctx.send("...pas comme la molle a Filou...")
        await asyncio.sleep(1)
        await ctx.send(guesses[guess])
        if guesses[guess] == arg:
            await asyncio.sleep(1)
            await ctx.send("Bravo, Pussi Conqueror")
        else:
            await asyncio.sleep(1)
            await ctx.send("Hélas, la maison l'emporte")

    @commands.command(brief="!russianroulette")
    async def russianroulette(self, ctx):
        voice_channel = ctx.guild.voice_channels
        members = []
        
        for member in voice_channel[0].members:
            members.append(member)
            print(members)

        await ctx.send("Roulette Russe")
        await asyncio.sleep(1)
        for i in range(len(members)):
                
            luck = 1
            await ctx.send(f"{members[i]} prend le gun")
            await asyncio.sleep(1)
            await ctx.send(f"...")
            await asyncio.sleep(1)
            await ctx.send(f"...")
            await asyncio.sleep(1)
            if luck == 1:
                await ctx.send(f"Skidipopop")
                await member[i].voice_channel.disconnect()
                await asyncio.sleep(1)
                await ctx.send(f"Fin du jeu")
                return
            else:
                await ctx.send(f"click...")
                await asyncio.sleep(1)
                await ctx.send(f"...")

        await asyncio.sleep(1)
        await ctx.send(f"Parsonne est mort")                
        return

def setup(bot):
    bot.add_cog(Games(bot))