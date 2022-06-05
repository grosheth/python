import asyncio
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
            await ctx.send("C'est Pile ou c'est face le gros")
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

    @commands.command(brief="!guessnumber <nombre> <nombre>")
    async def guessnumber(self, ctx, arg):

        return

def setup(bot):
    bot.add_cog(Games(bot))