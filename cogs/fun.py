import discord
from discord.ext import commands
import requests
class Fun(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
    @commands.command(aliases=['genjoke'])
    async def joke(self, ctx):
        response = requests.get(
                "https://christmascountdown.live/api/joke")
        data = response.json()
        result = "Question: " + data["question"] + "\nAnswer: " + data["answer"]
        embed=discord.Embed(title="Joke Generator", url="https://github.com/TheGamer3514/Christmas-Bot", description=result, color=0xFCBA03)
        await ctx.send(embed=embed)
async def setup(bot):
    await bot.add_cog(Fun(bot))
