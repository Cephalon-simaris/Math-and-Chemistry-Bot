import random
import datetime
import asyncio
import math
import matplotlib.pyplot as plt
import numpy as np
import os
import json
import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.members = True
intents.reactions = True
intents.messages = True
client = commands.Bot(command_prefix = '//', intents = intents)
client.remove_command("help")

@client.event
async def on_ready():
	print("Bot is ready!")

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")

@client.command()
async def help(ctx):
    embed = discord.Embed(title = ":white_check_mark: **CALC HELP**" , description = "**PREFIX** : `//`" , timestamp=ctx.message.created_at, color = discord.Colour.blue())
    embed.add_field(name = "**//calc <equation>**", value = "evaluates equation", inline = True)
    embed.add_field(name = "**//log <number> <base>**", value = "calculates log with input base", inline = True)
    embed.add_field(name = "**//ln <number>**", value = "calculates log with base e", inline = True)
    embed.add_field(name = "**//power <number> <power>**", value = "calculates the number raised to power", inline = True)
    embed.add_field(name = "**//diff help**", value = "use /diff <equation> from the list", inline = True)
    embed.add_field(name = "**//pt**", value = "Displays Periodic Table",inline = True)
    embed.add_field(name = "**//<sin/cos/tan/cosec/sec/cot> <number in degrees>**", value = "input in degrees", inline = True)
    embed.add_field(name = "**//element <elementnumber or name(first letter capital)>**", value = "Displays information about an element",inline = False)
    embed.set_thumbnail(url = client.user.avatar_url)
    embed.set_footer(text = ctx.guild, icon_url = ctx.guild.icon_url)
    await ctx.send(embed = embed)

@client.command()
async def calc(ctx, query):
    try:
        embed2 = discord.Embed(title = "`Equation`", description = "```"+str(query)+"```", timestamp=ctx.message.created_at, color = discord.Colour.green())
        embed2.add_field(name = "`Solution`", value = "```"+str(eval(query))+"```")
        f = discord.File("calculatoricon.png", filename="calculatoricon.png")
        embed2.set_thumbnail(url = "attachment://calculatoricon.png")
        embed2.set_footer(text = ctx.guild, icon_url = ctx.guild.icon_url)
        await ctx.send(file = f,embed = embed2)
    except:
        await ctx.send("Error : Invalid input! Try using something else!")

@client.command()
async def log(ctx, number : float,*,base : float):
    try:
        ans = math.log(number,base)
        val = str(ans)
        embed3 = discord.Embed(title = "`Equation`", description = "```"+"log("+str(number)+")"+"```", timestamp=ctx.message.created_at, color = discord.Colour.green())
        embed3.add_field(name = "`Solution`", value = "```"+val[0:6]+"```")
        f = discord.File("calculatoricon.png", filename="calculatoricon.png")
        embed3.set_thumbnail(url = "attachment://calculatoricon.png")
        embed3.set_footer(text = ctx.guild, icon_url = ctx.guild.icon_url)
        await ctx.send(file = f,embed = embed3)
    except:
        await ctx.send("Error : Invalid input! Try using something else!")
    
@client.command()
async def ln(ctx, number : float):
    try:
        ans1 = math.log(number)
        val1 = str(ans1)
        embed4 = discord.Embed(title = "`Equation`", description = "```"+"ln("+str(number)+")"+"```", timestamp=ctx.message.created_at, color = discord.Colour.green())
        embed4.add_field(name = "`Solution`", value = "```"+val1[0:6]+"```")
        f = discord.File("calculatoricon.png", filename="calculatoricon.png")
        embed4.set_thumbnail(url = "attachment://calculatoricon.png")
        embed4.set_footer(text = ctx.guild, icon_url = ctx.guild.icon_url)
        await ctx.send(file = f,embed = embed4)
    except:
        await ctx.send("Error : Invalid input! Try using something else!")

@client.command()
async def sin(ctx,number : float):
    try:
        ans2 = math.sin(math.radians(number))
        val2 = str(ans2)
        embed5 = discord.Embed(title = "`Equation`", description = "```"+"Sin("+str(number)+")"+"```", timestamp=ctx.message.created_at, color = discord.Colour.green())
        embed5.add_field(name = "`Solution`", value = "```"+val2[0:6]+"```")
        f = discord.File("calculatoricon.png", filename="calculatoricon.png")
        embed5.set_thumbnail(url = "attachment://calculatoricon.png")
        embed5.set_footer(text = ctx.guild, icon_url = ctx.guild.icon_url)
        await ctx.send(file = f,embed = embed5)
    except:
        await ctx.send("Error : Invalid input! Try using something else!")

@client.command()
async def cos(ctx,number : float):
    try:
        if number%90 == 0:
            mucheck = number/90
            if mucheck%2 == 0:
                ans13 = math.cos(math.radians(number))
                val13 = str(ans13)
                embed10 = discord.Embed(title = "`Equation`", description = "```"+"Cos("+str(number)+")"+"```", timestamp=ctx.message.created_at, color = discord.Colour.green())
                embed10.add_field(name = "`Solution`", value = "```"+val13[0:6]+"```")
                f = discord.File("calculatoricon.png", filename="calculatoricon.png")
                embed10.set_thumbnail(url = "attachment://calculatoricon.png")
                embed10.set_footer(text = ctx.guild, icon_url = ctx.guild.icon_url)
                await ctx.send(file = f,embed = embed10)
            else:
                embed11 = discord.Embed(title = "`Equation`", description = "```"+"Cos("+str(number)+")"+"```", timestamp=ctx.message.created_at, color = discord.Colour.green())
                embed11.add_field(name = "`Solution`", value = "```"+"0.0"+"```")
                f = discord.File("calculatoricon.png", filename="calculatoricon.png")
                embed11.set_thumbnail(url = "attachment://calculatoricon.png")
                embed11.set_footer(text = ctx.guild, icon_url = ctx.guild.icon_url)
                await ctx.send(file = f,embed = embed11)
        else:
            ans3 = math.cos(math.radians(number))
            val3 = str(ans3)
            embed12 = discord.Embed(title = "`Equation`", description = "```"+"Cos("+str(number)+")"+"```", timestamp=ctx.message.created_at, color = discord.Colour.green())
            embed12.add_field(name = "`Solution`", value = "```"+val3[0:6]+"```")
            f = discord.File("calculatoricon.png", filename="calculatoricon.png")
            embed12.set_thumbnail(url = "attachment://calculatoricon.png")
            embed12.set_footer(text = ctx.guild, icon_url = ctx.guild.icon_url)
            await ctx.send(file = f,embed = embed12)
    except:
        await ctx.send("Error : Invalid input! Try using something else!")

@client.command()
async def tan(ctx,number : float):
    try:
        if number%90 == 0:
            mucheck = number/90
            if mucheck%2 == 0:
                embed7 = discord.Embed(title = "`Equation`", description = "```"+"Tan("+str(number)+")"+"```", timestamp=ctx.message.created_at, color = discord.Colour.green())
                embed7.add_field(name = "`Solution`", value = "```"+"0.0"+"```")
                f = discord.File("calculatoricon.png", filename="calculatoricon.png")
                embed7.set_thumbnail(url = "attachment://calculatoricon.png")
                embed7.set_footer(text = ctx.guild, icon_url = ctx.guild.icon_url)
                await ctx.send(file = f,embed = embed7)
            else:
                embed8 = discord.Embed(title = "`Equation`", description = "```"+"Tan("+str(number)+")"+"```", timestamp=ctx.message.created_at, color = discord.Colour.green())
                embed8.add_field(name = "`Solution`", value = "```"+"Infinite"+"```")
                f = discord.File("calculatoricon.png", filename="calculatoricon.png")
                embed8.set_thumbnail(url = "attachment://calculatoricon.png")
                embed8.set_footer(text = ctx.guild, icon_url = ctx.guild.icon_url)
                await ctx.send(file = f,embed = embed8)
        else:
            ans5 = math.tan(math.radians(number))
            val5 = str(ans5)
            embed9 = discord.Embed(title = "`Equation`", description = "```"+"Tan("+str(number)+")"+"```", timestamp=ctx.message.created_at, color = discord.Colour.green())
            embed9.add_field(name = "`Solution`", value = "```"+val5[0:6]+"```")
            f = discord.File("calculatoricon.png", filename="calculatoricon.png")
            embed9.set_thumbnail(url = "attachment://calculatoricon.png")
            embed9.set_footer(text = ctx.guild, icon_url = ctx.guild.icon_url)
            await ctx.send(file = f,embed = embed9)
    except:
        await ctx.send("Error : Invalid input! Try using something else!")

@client.command()
async def cot(ctx,number : float):
    try:
        if number%90 == 0:
            mucheck = number/90
            if mucheck%2 == 0:
                embed10 = discord.Embed(title = "`Equation`", description = "```"+"Cot("+str(number)+")"+"```", timestamp=ctx.message.created_at, color = discord.Colour.green())
                embed10.add_field(name = "`Solution`", value = "```"+"Infinite"+"```")
                f = discord.File("calculatoricon.png", filename="calculatoricon.png")
                embed10.set_thumbnail(url = "attachment://calculatoricon.png")
                embed10.set_footer(text = ctx.guild, icon_url = ctx.guild.icon_url)
                await ctx.send(file = f,embed = embed10)
            else:
                embed11 = discord.Embed(title = "`Equation`", description = "```"+"Cot("+str(number)+")"+"```", timestamp=ctx.message.created_at, color = discord.Colour.green())
                embed11.add_field(name = "`Solution`", value = "```"+"0.0"+"```")
                f = discord.File("calculatoricon.png", filename="calculatoricon.png")
                embed11.set_thumbnail(url = "attachment://calculatoricon.png")
                embed11.set_footer(text = ctx.guild, icon_url = ctx.guild.icon_url)
                await ctx.send(file = f,embed = embed11)
        else:
            ans6 = math.tan(math.radians(number))
            val6 = str(1/(ans6))
            embed12 = discord.Embed(title = "`Equation`", description = "```"+"Cot("+str(number)+")"+"```", timestamp=ctx.message.created_at, color = discord.Colour.green())
            embed12.add_field(name = "`Solution`", value = "```"+val6[0:6]+"```")
            f = discord.File("calculatoricon.png", filename="calculatoricon.png")
            embed12.set_thumbnail(url = "attachment://calculatoricon.png")
            embed12.set_footer(text = ctx.guild, icon_url = ctx.guild.icon_url)
            await ctx.send(file = f,embed = embed12)
    except:
        await ctx.send("Error : Invalid input! Try using something else!")

@client.command()
async def cosec(ctx,number : float):
    try:
        if number%90 == 0:
            mucheck = number/90
            if mucheck%2 == 0:
                embed13 = discord.Embed(title = "`Equation`", description = "```"+"Cosec("+str(number)+")"+"```", timestamp=ctx.message.created_at, color = discord.Colour.green())
                embed13.add_field(name = "`Solution`", value = "```"+"Infinite"+"```")
                f = discord.File("calculatoricon.png", filename="calculatoricon.png")
                embed13.set_thumbnail(url = "attachment://calculatoricon.png")
                embed13.set_footer(text = ctx.guild, icon_url = ctx.guild.icon_url)
                await ctx.send(file = f,embed = embed13)
            else:
                ans10 = math.sin(math.radians(number))
                val10 = str(1/ans10)
                embed17 = discord.Embed(title = "`Equation`", description = "```"+"Cosec("+str(number)+")"+"```", timestamp=ctx.message.created_at, color = discord.Colour.green())
                embed17.add_field(name = "`Solution`", value = "```"+val10[0:6]+"```")
                f = discord.File("calculatoricon.png", filename="calculatoricon.png")
                embed17.set_thumbnail(url = "attachment://calculatoricon.png")
                embed17.set_footer(text = ctx.guild, icon_url = ctx.guild.icon_url)
                await ctx.send(file = f,embed = embed17)
        else:
            ans11 = math.sin(math.radians(number))
            val11 = str(1/ans11)
            embed18 = discord.Embed(title = "`Equation`", description = "```"+"Cosec("+str(number)+")"+"```", timestamp=ctx.message.created_at, color = discord.Colour.green())
            embed18.add_field(name = "`Solution`", value = "```"+val11[0:6]+"```")
            f = discord.File("calculatoricon.png", filename="calculatoricon.png")
            embed18.set_thumbnail(url = "attachment://calculatoricon.png")
            embed18.set_footer(text = ctx.guild, icon_url = ctx.guild.icon_url)
            await ctx.send(file = f,embed = embed18)
    except:
        await ctx.send("Error : Invalid input! Try using something else!")

@client.command()
async def sec(ctx,number : float):
    try:
        if number%90 == 0:
            mucheck = number/90
            if mucheck%2 == 1:
                embed14 = discord.Embed(title = "`Equation`", description = "```"+"Sec("+str(number)+")"+"```", timestamp=ctx.message.created_at, color = discord.Colour.green())
                embed14.add_field(name = "`Solution`", value = "```"+"Infinite"+"```")
                f = discord.File("calculatoricon.png", filename="calculatoricon.png")
                embed14.set_thumbnail(url = "attachment://calculatoricon.png")
                embed14.set_footer(text = ctx.guild, icon_url = ctx.guild.icon_url)
                await ctx.send(file = f,embed = embed14)
            else:
                ans9 = math.cos(math.radians(number))
                val9 = str(1/ans9)
                embed15 = discord.Embed(title = "`Equation`", description = "```"+"Sec("+str(number)+")"+"```", timestamp=ctx.message.created_at, color = discord.Colour.green())
                embed15.add_field(name = "`Solution`", value = "```"+val9[0:6]+"```")
                f = discord.File("calculatoricon.png", filename="calculatoricon.png")
                embed15.set_thumbnail(url = "attachment://calculatoricon.png")
                embed15.set_footer(text = ctx.guild, icon_url = ctx.guild.icon_url)
                await ctx.send(file = f,embed = embed15)
        else:
            ans8 = math.cos(math.radians(number))
            val8 = str(1/ans8)
            embed16 = discord.Embed(title = "`Equation`", description = "```"+"Sec("+str(number)+")"+"```", timestamp=ctx.message.created_at, color = discord.Colour.green())
            embed16.add_field(name = "`Solution`", value = "```"+val8[0:6]+"```")
            f = discord.File("calculatoricon.png", filename="calculatoricon.png")
            embed16.set_thumbnail(url = "attachment://calculatoricon.png")
            embed16.set_footer(text = ctx.guild, icon_url = ctx.guild.icon_url)
            await ctx.send(file = f,embed = embed16)
    except:
        await ctx.send("Error : Invalid input! Try using something else!")

@client.command()
async def power(ctx,number : float,*,power : float):
    try:
        val12 = str(math.pow(number,power))
        embed19 = discord.Embed(title = "`Equation`", description = "```("+str(number)+")^("+str(power)+")```", timestamp=ctx.message.created_at, color = discord.Colour.green())
        embed19.add_field(name = "`Solution`", value = "```"+val12+"```")
        f = discord.File("calculatoricon.png", filename="calculatoricon.png")
        embed19.set_thumbnail(url = "attachment://calculatoricon.png")
        embed19.set_footer(text = ctx.guild, icon_url = ctx.guild.icon_url)
        await ctx.send(file = f,embed = embed19)
    except:
        await ctx.send("Error : Invalid input! Try using something else!")

@client.command()
async def diff(ctx,equation : str):
    try:
        if equation == "help":
            embed20 = discord.Embed(title = ":white_check_mark: List of identities to input in the command :-" , description = "`x` , `ax` , `x^n` , `x^x` , `a^x` , `e^x` , `ln(x)` \n`sinx` , `cosx` , `tanx` , `secx` , `cosecx` , `cotx`\n`sin^-1(x)` , `cos^-1(x)` , `tan^-1(x)`\n`sec^-1(x)` , `cosec^-1(x)` , `cot^-1(x)`", timestamp = ctx.message.created_at, color = discord.Colour.red())
            embed20.set_thumbnail(url = client.user.avatar_url)
            embed20.set_footer(text = ctx.guild, icon_url = ctx.guild.icon_url)
            await ctx.send(embed = embed20)
        elif equation == "x":
            embed21 = discord.Embed(title = f"differentiation of ({equation}) w.r.t. (x) is", timestamp = ctx.message.created_at, color = discord.Colour.red())
            f = discord.File("id1.png", filename = "id1.png")
            embed21.set_image(url = "attachment://id1.png")
            embed21.set_footer(text = ctx.guild, icon_url = ctx.guild.icon_url)
            await ctx.send(file = f,embed = embed21)
        elif equation == "ax":
            embed22 = discord.Embed(title = f"differentiation of ({equation}) w.r.t. (x) is", timestamp = ctx.message.created_at, color = discord.Colour.red())
            f = discord.File("id2.png", filename = "id2.png")
            embed22.set_image(url = "attachment://id2.png")
            embed22.set_footer(text = ctx.guild, icon_url = ctx.guild.icon_url)
            await ctx.send(file = f,embed = embed22)
        elif equation == "sinx":
            embed23 = discord.Embed(title = f"differentiation of ({equation}) w.r.t. (x) is", timestamp = ctx.message.created_at, color = discord.Colour.red())
            f = discord.File("id3.png", filename = "id3.png")
            embed23.set_image(url = "attachment://id3.png")
            embed23.set_footer(text = ctx.guild, icon_url = ctx.guild.icon_url)
            await ctx.send(file = f,embed = embed23)
        elif equation == "cosx":
            embed24 = discord.Embed(title = f"differentiation of ({equation}) w.r.t. (x) is", timestamp = ctx.message.created_at, color = discord.Colour.red())
            f = discord.File("id4.png", filename = "id4.png")
            embed24.set_image(url = "attachment://id4.png")
            embed24.set_footer(text = ctx.guild, icon_url = ctx.guild.icon_url)
            await ctx.send(file = f,embed = embed24)
        elif equation == "x^n":
            embed25 = discord.Embed(title = f"differentiation of ({equation}) w.r.t. (x) is", timestamp = ctx.message.created_at, color = discord.Colour.red())
            f = discord.File("id5.png", filename = "id5.png")
            embed25.set_image(url = "attachment://id5.png")
            embed25.set_footer(text = ctx.guild, icon_url = ctx.guild.icon_url)
            await ctx.send(file = f,embed = embed25)
        elif equation == "tanx":
            embed26 = discord.Embed(title = f"differentiation of ({equation}) w.r.t. (x) is", timestamp = ctx.message.created_at, color = discord.Colour.red())
            f = discord.File("id6.png", filename = "id6.png")
            embed26.set_image(url = "attachment://id6.png")
            embed26.set_footer(text = ctx.guild, icon_url = ctx.guild.icon_url)
            await ctx.send(file = f,embed = embed26)
        elif equation == "secx":
            embed27 = discord.Embed(title = f"differentiation of ({equation}) w.r.t. (x) is", timestamp = ctx.message.created_at, color = discord.Colour.red())
            f = discord.File("id7.png", filename = "id7.png")
            embed27.set_image(url = "attachment://id7.png")
            embed27.set_footer(text = ctx.guild, icon_url = ctx.guild.icon_url)
            await ctx.send(file = f,embed = embed27)
        elif equation == "cosecx":
            embed28 = discord.Embed(title = f"differentiation of ({equation}) w.r.t. (x) is", timestamp = ctx.message.created_at, color = discord.Colour.red())
            f = discord.File("D:/Kunj Personal/Programming (source code)/study bot/id8.png", filename = "id8.png")
            embed28.set_image(url = "attachment://id8.png")
            embed28.set_footer(text = ctx.guild, icon_url = ctx.guild.icon_url)
            await ctx.send(file = f,embed = embed28)
        elif equation == "cotx":
            embed29 = discord.Embed(title = f"differentiation of ({equation}) w.r.t. (x) is", timestamp = ctx.message.created_at, color = discord.Colour.red())
            f = discord.File("id9.png", filename = "id9.png")
            embed29.set_image(url = "attachment://id9.png")
            embed29.set_footer(text = ctx.guild, icon_url = ctx.guild.icon_url)
            await ctx.send(file = f,embed = embed29)
        elif equation == "sin^-1(x)":
            embed30 = discord.Embed(title = f"differentiation of ({equation}) w.r.t. (x) is", timestamp = ctx.message.created_at, color = discord.Colour.red())
            f = discord.File("id10.png", filename = "id10.png")
            embed30.set_image(url = "attachment://id10.png")
            embed30.set_footer(text = ctx.guild, icon_url = ctx.guild.icon_url)
            await ctx.send(file = f,embed = embed30)
        elif equation == "cos^-1(x)":
            embed31 = discord.Embed(title = f"differentiation of ({equation}) w.r.t. (x) is", timestamp = ctx.message.created_at, color = discord.Colour.red())
            f = discord.File("id11.png", filename = "id11.png")
            embed31.set_image(url = "attachment://id11.png")
            embed31.set_footer(text = ctx.guild, icon_url = ctx.guild.icon_url)
            await ctx.send(file = f,embed = embed31)
        elif equation == "tan^-1(x)":
            embed32 = discord.Embed(title = f"differentiation of ({equation}) w.r.t. (x) is", timestamp = ctx.message.created_at, color = discord.Colour.red())
            f = discord.File("id12.png", filename = "id12.png")
            embed32.set_image(url = "attachment://id12.png")
            embed32.set_footer(text = ctx.guild, icon_url = ctx.guild.icon_url)
            await ctx.send(file = f,embed = embed32)
        elif equation == "sec^-1(x)":
            embed33 = discord.Embed(title = f"differentiation of ({equation}) w.r.t. (x) is", timestamp = ctx.message.created_at, color = discord.Colour.red())
            f = discord.File("id13.png", filename = "id13.png")
            embed33.set_image(url = "attachment://id13.png")
            embed33.set_footer(text = ctx.guild, icon_url = ctx.guild.icon_url)
            await ctx.send(file = f,embed = embed33)
        elif equation == "cosec^-1(x)":
            embed34 = discord.Embed(title = f"differentiation of ({equation}) w.r.t. (x) is", timestamp = ctx.message.created_at, color = discord.Colour.red())
            f = discord.File("id14.png", filename = "id14.png")
            embed34.set_image(url = "attachment://id14.png")
            embed34.set_footer(text = ctx.guild, icon_url = ctx.guild.icon_url)
            await ctx.send(file = f,embed = embed34)
        elif equation == "cot^-1(x)":
            embed35 = discord.Embed(title = f"differentiation of ({equation}) w.r.t. (x) is", timestamp = ctx.message.created_at, color = discord.Colour.red())
            f = discord.File("id15.png", filename = "id15.png")
            embed35.set_image(url = "attachment://id15.png")
            embed35.set_footer(text = ctx.guild, icon_url = ctx.guild.icon_url)
            await ctx.send(file = f,embed = embed35)
        elif equation == "e^x":
            embed36 = discord.Embed(title = f"differentiation of ({equation}) w.r.t. (x) is", timestamp = ctx.message.created_at, color = discord.Colour.red())
            f = discord.File("id16.png", filename = "id16.png")
            embed36.set_image(url = "attachment://id16.png")
            embed36.set_footer(text = ctx.guild, icon_url = ctx.guild.icon_url)
            await ctx.send(file = f,embed = embed36)
        elif equation == "x^x":
            embed37 = discord.Embed(title = f"differentiation of ({equation}) w.r.t. (x) is", timestamp = ctx.message.created_at, color = discord.Colour.red())
            f = discord.File("id17.png", filename = "id17.png")
            embed37.set_image(url = "attachment://id17.png")
            embed37.set_footer(text = ctx.guild, icon_url = ctx.guild.icon_url)
            await ctx.send(file = f,embed = embed37)
        elif equation == "a^x":
            embed38 = discord.Embed(title = f"differentiation of ({equation}) w.r.t. (x) is", timestamp = ctx.message.created_at, color = discord.Colour.red())
            f = discord.File("id18.png", filename = "id18.png")
            embed38.set_image(url = "attachment://id18.png")
            embed38.set_footer(text = ctx.guild, icon_url = ctx.guild.icon_url)
            await ctx.send(file = f,embed = embed38)
        elif equation == "lnx":
            embed39 = discord.Embed(title = f"differentiation of ({equation}) w.r.t. (x) is", timestamp = ctx.message.created_at, color = discord.Colour.red())
            f = discord.File("id19.png", filename = "id19.png")
            embed39.set_image(url = "attachment://id19.png")
            embed39.set_footer(text = ctx.guild, icon_url = ctx.guild.icon_url)
            await ctx.send(file = f,embed = embed39)
    except:
        await ctx.send("Error : Invalid input! Try using something else!")

@client.command()
@commands.has_role("Owner") #requires a role named Owner in the server , you can change it to has_permission
async def clear(ctx,number : int):
    await ctx.channel.purge(limit=number)

@client.command()
async def pt(ctx):
    embed = discord.Embed(title = "Periodic Table", color = discord.Colour.green())
    embed.set_image(url = "https://pubchem.ncbi.nlm.nih.gov/periodic-table/Periodic_Table.png")
    await ctx.send(embed = embed)

@client.command()
async def element(ctx, element):
    res = isinstance(element, str)
    with open('periodic_elements.json','r',encoding='utf-8') as f:
        data = json.load(f)
        if element.isdigit() == True:
            enum = int(element)
            if enum < 120:
                name = str(data['elements'][enum-1]["name"])
                appearance = str(data['elements'][enum-1]["appearance"])
                atomic_mass = str(data['elements'][enum-1]["atomic_mass"])
                category = str(data['elements'][enum-1]["category"])
                density = str(data['elements'][enum-1]["density"])
                atomic_number = str(data['elements'][enum-1]["number"])
                period = str(data['elements'][enum-1]["period"])
                phase = str(data['elements'][enum-1]["phase"])
                summary = str(data['elements'][enum-1]["summary"])
                symbol = str(data['elements'][enum-1]["symbol"])
                shells = data['elements'][enum-1]["shells"]
                ionization_energies = data['elements'][enum-1]["ionization_energies"]
                electron_configuration_semantic = data['elements'][enum-1]["electron_configuration_semantic"]
                embed = discord.Embed(title = f":white_check_mark: **ELEMENT {atomic_number} -> {name.upper()} AND IT'S PROPERTIES**",description = f"**SYMBOL {symbol}**" , timestamp = ctx.message.created_at, color = discord.Colour.green())
                embed.set_thumbnail(url = "https://i.pinimg.com/originals/22/72/2b/22722b33f4d7e9d810c6bce2fe678128.jpg")
                embed.add_field(name = "**Atomic mass**" , value = atomic_mass, inline = True)
                embed.add_field(name = "**Shells**", value = shells, inline = True)
                embed.add_field(name = "**Electronic Config**", value = electron_configuration_semantic, inline = True)
                embed.add_field(name = "**Phase**", value = phase, inline = True)
                embed.add_field(name = "**Period**", value = period, inline = True)
                embed.add_field(name = "**Appearance**", value = appearance, inline = True)
                embed.add_field(name = "**Density (Kg/m3)**", value = density, inline = True)
                embed.add_field(name = "**Category**", value = category, inline = True)
                embed.add_field(name = "**Ionization Energies (KJ/mol)**", value = ionization_energies, inline = True)
                embed.add_field(name = "**Summary**", value = summary, inline = False)
                embed.set_footer(text = ctx.guild, icon_url = ctx.guild.icon_url)
                await ctx.send(embed = embed)
            else:
                embed = discord.Embed(title = ":white_check_mark: **ERROR 404, ELEMENT NOT FOUND**", description = "**Please provide a valid number!**", timestamp=ctx.message.created_at, color = discord.Colour.green())
                embed.set_footer(text = ctx.guild, icon_url = ctx.guild.icon_url)
                await ctx.send(embed = embed)
        elif res == True:
            for i in range (1,120):
                if element == data['elements'][i-1]["name"]:
                    name = str(data['elements'][i-1]["name"])
                    appearance = str(data['elements'][i-1]["appearance"])
                    atomic_mass = str(data['elements'][i-1]["atomic_mass"])
                    category = str(data['elements'][i-1]["category"])
                    density = str(data['elements'][i-1]["density"])
                    atomic_number = str(data['elements'][i-1]["number"])
                    period = str(data['elements'][i-1]["period"])
                    phase = str(data['elements'][i-1]["phase"])
                    summary = str(data['elements'][i-1]["summary"])
                    symbol = str(data['elements'][i-1]["symbol"])
                    shells = data['elements'][i-1]["shells"]
                    ionization_energies = data['elements'][i-1]["ionization_energies"]
                    electron_configuration_semantic = data['elements'][i-1]["electron_configuration_semantic"]
                    embed = discord.Embed(title = f":white_check_mark: **ELEMENT {atomic_number} -> {name.upper()} AND IT'S PROPERTIES**",description = f"**SYMBOL {symbol}**" , timestamp = ctx.message.created_at, color = discord.Colour.green())
                    embed.set_thumbnail(url = "https://i.pinimg.com/originals/22/72/2b/22722b33f4d7e9d810c6bce2fe678128.jpg")
                    embed.add_field(name = "**Atomic mass**" , value = atomic_mass, inline = True)
                    embed.add_field(name = "**Shells**", value = shells, inline = True)
                    embed.add_field(name = "**Electronic Config**", value = electron_configuration_semantic, inline = True)
                    embed.add_field(name = "**Phase**", value = phase, inline = True)
                    embed.add_field(name = "**Period**", value = period, inline = True)
                    embed.add_field(name = "**Appearance**", value = appearance, inline = True)
                    embed.add_field(name = "**Density (Kg/m3)**", value = density, inline = True)
                    embed.add_field(name = "**Category**", value = category, inline = True)
                    embed.add_field(name = "**Ionization Energies (KJ/mol)**", value = ionization_energies, inline = True)
                    embed.add_field(name = "**Summary**", value = summary, inline = False)
                    embed.set_footer(text = ctx.guild, icon_url = ctx.guild.icon_url)
                    await ctx.send(embed = embed)
                    break
                elif element != data['elements'][i-1]["name"]:
                    i+=1
                    continue
                else:
                    embed = discord.Embed(title = ":cyclone: **ERROR 404, ELEMENT NOT FOUND**", description = "**Please provide a valid element!**", timestamp=ctx.message.created_at, color = discord.Colour.green())
                    embed.set_footer(text = ctx.guild, icon_url = ctx.guild.icon_url)
                    await ctx.send(embed = embed)
                    break

@client.command()
async def create_tag(ctx, title : str ,*, description : str):
    if title == None or description == None:
        await ctx.send("Please provide a title/description!")
    elif len(title) > 150:
        await ctx.send("Too long title!")
    else:
        try:
            with open('tags.json', 'r') as f:
                data3 = json.load(f)

                data3[str(title)] = description

            with open('tags.json', 'w') as f:
                json.dump(data3,f,indent=4)

            await ctx.send(f"Tag successfully added! To use it type `bs!tag {title}`")
        except:
            await ctx.send("There was an error while creating the tag D:")

@client.command()
async def delete_tag(ctx, title : str):
    if title ==  None:
        await ctx.send("Please provide a title to delete!")
    else:
        try:
            with open('tags.json','r') as f:
                data4 = json.load(f)

                del data4[str(title)]

            with open('tags.json','w') as f:
                json.dump(data4,f,indent=4)

                await ctx.send(f"{title} tag successfully deleted!")
        except:
            await("No such tag exists!")


@client.command()
async def tag(ctx , title : str):
    try:
        with open('tags.json', 'r') as f:
            data4 = json.load(f)

            sending = data4[str(title)]
            await ctx.send(f"**__TAG TITLE:__** `{title}`\n\n__DESCRIPTION:__{sending}")

    except:
        await ctx.send("Either there was an error or the tag was not found!!")

client.run("bot token here")
