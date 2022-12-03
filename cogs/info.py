import discord
from discord.ext import commands
class Info(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def stats(self, ctx):
        embed=discord.Embed(title="Bot Stats", url="https://github.com/TheGamer3514/Christmas-Bot", description=f"Servers: {len(self.bot.guilds)}\nPing: {round (self.bot.latency * 1000)} ms\nUptime: 99.99%", color=0xFCBA03)
        await ctx.send(embed=embed)
    @commands.command(aliases=['bothelp'])
    async def help(self, ctx):
        embed=discord.Embed(title="Bot Help", url="https://github.com/TheGamer3514/Christmas-Bot", description="**Info:**\n``c!help`` - Shows The Help Embed\n**Fun:**\n``c!joke`` - Generate A Christmas Joke!", color=0xFCBA03)
        await ctx.send(embed=embed)
    @commands.command(aliases=['botcredits'])
    async def credits(self, ctx):
        embed=discord.Embed(title="Credits", url="https://github.com/TheGamer3514/Christmas-Bot", description="``Bot Creator:`` Gamer3514#7679\n``Github`` - [Link](https://github.com/TheGamer3514/Christmas-Bot)\n``Support Server`` - [Link](https://discord.gg/WeQ3TpdfZM)", color=0xFCBA03)
        await ctx.send(embed=embed)
async def setup(bot):
    await bot.add_cog(Info(bot))
