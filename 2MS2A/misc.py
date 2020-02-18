import random

import numpy as np
from discord.ext import commands


class MISC(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="Roll a die. (1d6 by default)", usage="<amount>d<size>")
    async def roll(self, ctx, type="1d6"):
        amount = int(type.split("d")[0])
        size = int(type.split("d")[1])
        results = []
        big = False
        total = 0
        out = []

        for die in range(amount):
            roll = random.randint(1, size)
            results.append(roll)
            total += roll

        out.append("Rolled %sd%s" % (amount, size))
        out.append("Total: %s" % total)
        out.append("Mean: %s" % np.mean(results))
        out.append("\nAll Rolls:")

        if (len("\n".join(out)) + len(", ".join([str(num) for num in results]))) > 2000:
            big = True

        if big:
            await ctx.send("\n".join(out) + "\nThe rolls are too big to display!")
        else:
            await ctx.send("\n".join(out) + "\n" + (", ".join([str(num) for num in results])))
        print("%s ROLLED %s." % (ctx.author.name, type))


def setup(bot):
    bot.add_cog(MISC(bot))
