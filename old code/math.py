import random
import asyncio
import math
import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.members = True
intents.reactions = True
intents.messages = True
client = commands.Bot(command_prefix = 'm!', intents = intents)
client.remove_command("help")

@client.event
async def on_ready():
	activity = discord.Activity(name="<discord guild name>", type=3)
	await client.change_presence(status=discord.Status.online, activity=activity)
	print("Bot is ready!")

@client.command()
async def help(ctx):
    embed = discord.Embed(title = ":white_check_mark: calc help" , description = "calc commands (use prefix -> m! )" , color = discord.Colour.blue())
    embed.add_field(name = "/calc <equation>", value = "enter equation here", inline = False)
    embed.add_field(name = "/log <number> <base>", value = "Use to find logarithm of a number with base and the number as input", inline = False)
    embed.add_field(name = "/ln <number>", value = "Use to find logarithm of a number with base e", inline = False)
    embed.add_field(name = "/<sin/cos/tan/cosec/sec/cot> <number in degrees>", value = "Use to find the value of the trigonometric functions at the input number in degrees", inline = False)
    embed.set_thumbnail(url = client.user.avatar_url)
    await ctx.send(embed = embed)

@client.command()
async def calc(ctx, query):
    try:
        embed2 = discord.Embed(title = "`Equation`", description = "```"+str(query)+"```", color = discord.Colour.green())
        embed2.add_field(name = "`Solution`", value = "```"+str(eval(query))+"```")
        embed2.set_thumbnail(url = "https://icons-for-free.com/iconfiles/png/512/calculating+calculation+calculator+finance+calculator-1320167738639982551.png")
        await ctx.send(embed = embed2)
    except:
        await ctx.send("Error : Invalid input! Try using something else!")

@client.command()
async def log(ctx, number : float,*,base : int):
    try:
        ans = math.log(number,base)
        val = str(ans)
        embed3 = discord.Embed(title = "`Equation`", description = "```"+"log("+str(number)+")"+"```", color = discord.Colour.green())
        embed3.add_field(name = "`Solution`", value = "```"+val[0:6]+"```")
        embed3.set_thumbnail(url = "https://icons-for-free.com/iconfiles/png/512/calculating+calculation+calculator+finance+calculator-1320167738639982551.png")
        await ctx.send(embed = embed3)
    except:
        await ctx.send("Error : Invalid input! Try using something else!")
    
@client.command()
async def ln(ctx, number : float):
    try:
        ans1 = math.log(number)
        val1 = str(ans1)
        embed4 = discord.Embed(title = "`Equation`", description = "```"+"ln("+str(number)+")"+"```", color = discord.Colour.green())
        embed4.add_field(name = "`Solution`", value = "```"+val1[0:6]+"```")
        embed4.set_thumbnail(url = "https://icons-for-free.com/iconfiles/png/512/calculating+calculation+calculator+finance+calculator-1320167738639982551.png")
        await ctx.send(embed = embed4)
    except:
        await ctx.send("Error : Invalid input! Try using something else!")

@client.command()
async def sin(ctx,number : int):
    try:
        ans2 = math.sin(math.radians(number))
        val2 = str(ans2)
        embed5 = discord.Embed(title = "`Equation`", description = "```"+"Sin("+str(number)+")"+"```", color = discord.Colour.green())
        embed5.add_field(name = "`Solution`", value = "```"+val2[0:6]+"```")
        embed5.set_thumbnail(url = "https://icons-for-free.com/iconfiles/png/512/calculating+calculation+calculator+finance+calculator-1320167738639982551.png")
        await ctx.send(embed = embed5)
    except:
        await ctx.send("Error : Invalid input! Try using something else!")

@client.command()
async def cos(ctx,number : int):
    try:
        ans3 = math.cos(math.radians(number))
        val3 = str(ans3)
        embed6 = discord.Embed(title = "`Equation`", description = "```"+"Cos("+str(number)+")"+"```", color = discord.Colour.green())
        embed6.add_field(name = "`Solution`", value = "```"+val3[0:6]+"```")
        embed6.set_thumbnail(url = "https://icons-for-free.com/iconfiles/png/512/calculating+calculation+calculator+finance+calculator-1320167738639982551.png")
        await ctx.send(embed = embed6)
    except:
        await ctx.send("Error : Invalid input! Try using something else!")

@client.command()
async def tan(ctx,number : int):
    try:
        if number%90 == 0:
            mucheck = number/90
            if mucheck%2 == 0:
                embed7 = discord.Embed(title = "`Equation`", description = "```"+"Tan("+str(number)+")"+"```", color = discord.Colour.green())
                embed7.add_field(name = "`Solution`", value = "```"+"0.0"+"```")
                embed7.set_thumbnail(url = "https://icons-for-free.com/iconfiles/png/512/calculating+calculation+calculator+finance+calculator-1320167738639982551.png")
                await ctx.send(embed = embed7)
            else:
                embed8 = discord.Embed(title = "`Equation`", description = "```"+"Tan("+str(number)+")"+"```", color = discord.Colour.green())
                embed8.add_field(name = "`Solution`", value = "```"+"Infinite"+"```")
                embed8.set_thumbnail(url = "https://icons-for-free.com/iconfiles/png/512/calculating+calculation+calculator+finance+calculator-1320167738639982551.png")
                await ctx.send(embed = embed8)
        else:
            ans5 = math.tan(math.radians(number))
            val5 = str(ans5)
            embed9 = discord.Embed(title = "`Equation`", description = "```"+"Tan("+str(number)+")"+"```", color = discord.Colour.green())
            embed9.add_field(name = "`Solution`", value = "```"+val5[0:6]+"```")
            embed9.set_thumbnail(url = "https://icons-for-free.com/iconfiles/png/512/calculating+calculation+calculator+finance+calculator-1320167738639982551.png")
            await ctx.send(embed = embed9)
    except:
        await ctx.send("Error : Invalid input! Try using something else!")

@client.command()
async def cot(ctx,number : int):
    try:
        if number%90 == 0:
            mucheck = number/90
            if mucheck%2 == 0:
                embed10 = discord.Embed(title = "`Equation`", description = "```"+"Cot("+str(number)+")"+"```", color = discord.Colour.green())
                embed10.add_field(name = "`Solution`", value = "```"+"Infinite"+"```")
                embed10.set_thumbnail(url = "https://icons-for-free.com/iconfiles/png/512/calculating+calculation+calculator+finance+calculator-1320167738639982551.png")
                await ctx.send(embed = embed10)
            else:
                embed11 = discord.Embed(title = "`Equation`", description = "```"+"Cot("+str(number)+")"+"```", color = discord.Colour.green())
                embed11.add_field(name = "`Solution`", value = "```"+"0.0"+"```")
                embed11.set_thumbnail(url = "https://icons-for-free.com/iconfiles/png/512/calculating+calculation+calculator+finance+calculator-1320167738639982551.png")
                await ctx.send(embed = embed11)
        else:
            ans6 = math.tan(math.radians(number))
            val6 = str(1/(ans6))
            embed12 = discord.Embed(title = "`Equation`", description = "```"+"Cot("+str(number)+")"+"```", color = discord.Colour.green())
            embed12.add_field(name = "`Solution`", value = "```"+val6[0:6]+"```")
            embed12.set_thumbnail(url = "https://icons-for-free.com/iconfiles/png/512/calculating+calculation+calculator+finance+calculator-1320167738639982551.png")
            await ctx.send(embed = embed12)
    except:
        await ctx.send("Error : Invalid input! Try using something else!")

@client.command()
async def cosec(ctx,number : int):
    try:
        ans7 = math.sin(math.radians(number))
        val7 = str(1/ans7)
        embed13 = discord.Embed(title = "`Equation`", description = "```"+"Cosec("+str(number)+")"+"```", color = discord.Colour.green())
        embed13.add_field(name = "`Solution`", value = "```"+val7[0:6]+"```")
        embed13.set_thumbnail(url = "https://icons-for-free.com/iconfiles/png/512/calculating+calculation+calculator+finance+calculator-1320167738639982551.png")
        await ctx.send(embed = embed13)
    except:
        await ctx.send("Error : Invalid input! Try using something else!")

@client.command()
async def sec(ctx,number : int):
    try:
        ans8 = math.cos(math.radians(number))
        val8 = str(1/ans8)
        embed14 = discord.Embed(title = "`Equation`", description = "```"+"Sec("+str(number)+")"+"```", color = discord.Colour.green())
        embed14.add_field(name = "`Solution`", value = "```"+val8[0:6]+"```")
        embed14.set_thumbnail(url = "https://icons-for-free.com/iconfiles/png/512/calculating+calculation+calculator+finance+calculator-1320167738639982551.png")
        await ctx.send(embed = embed14)
    except:
        await ctx.send("Error : Invalid input! Try using something else!")

@client.command()
@commands.has_role("Owner") #requires a role named Owner in the server
async def clear(ctx,number : int):
    await ctx.channel.purge(limit=number)    

client.run("<bot token>")
