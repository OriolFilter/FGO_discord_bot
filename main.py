#!/usr/bin/env python
# -*- coding: utf-8 -*-
import discord
from discord.ext import commands
from discord.utils import get
from credentials import TOKEN


description = '''Master im waiting for you to summon me!'''


bot = commands.Bot(command_prefix="f.", description=description)
bot.remove_command('help')

@bot.event
async def on_ready():
    print('------')
    print('Logged as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    game = discord.Game("I will help you master, type \"f.help\" if you still need learn to summon me!")
    await bot.change_presence(status=discord.Status.online, activity=game)

@bot.command()
async def test(ctx):
    await ctx.send("testing...")
    #e = discord.Embed(title="FGO active events", description="FGO (USA)", color=0x000000)
    #e.set_image(url="https://discordapp.com/assets/e4923594e694a21542a489471ecffa50.svg")
    #await ctx.send(embed=e)
    #await ctx.send("https://discordapp.com/assets/e4923594e694a21542a489471ecffa50.svg")


## Main_Commands

@bot.command()
async def events(ctx):
    await ctx.send("Hi master, you can check the active and future events at this webpage:\nhttps://fategrandorder.fandom.com/wiki/Event_List_(US)")
    #await ctx.send("Hi master, you can check the active and future events at this webpage:\nLINK")

@bot.command()
async def aevents(ctx): #active events

    ac_ev_list = discord.Embed(title="FGO active events", description="FGO (USA)", color=0x00ff00)
    ac_ev_list.add_field(name="Da Vinci and the 7 Counterfeit Heroic Spirits Revival (US)", value="Event Duration: January 10th 00:00 - January 19th 19:59 PST\nRequisites: Clear Orleans", inline=True)
    ac_ev_list.add_field(name="Fate/Grand Order Absolute Demonic Front: Babylonia Anime Release Campaign Part II (US)", value="Duration: January 20th 20:00 - January 29th 19:59 PST\nRequisites: Clear Fuyuki", inline=True)
    await ctx.send(embed=ac_ev_list)

    ev1 = discord.Embed(title="Da Vinci and the 7 Counterfeit Heroic Spirits Revival", url="https://fategrandorder.fandom.com/wiki/Da_Vinci_and_the_7_Counterfeit_Heroic_Spirits_Revival_(US)", color=0xebeb34)
    ev1.add_field(name="Requisites:", value="Clear Orleans", inline=False)
    ev1.add_field(name="Event Duration:", value="January 10th 00:00 - January 19th 19:59 PST", inline=False)
    await ctx.send(embed=ev1)

    ev2 = discord.Embed(title="Fate/Grand Order Absolute Demonic Front: Babylonia Anime Release Campaign Part II (US)", url="https://fategrandorder.fandom.com/wiki/Fate/Grand_Order_Absolute_Demonic_Front:_Babylonia_Anime_Release_Campaign_Part_II_(US)", color=0x345ceb)
    ev2.add_field(name="Requisites:", value="Clear Fuyuki", inline=False)
    ev2.add_field(name="Exchange period:", value="January 22nd 20:00 - January 29th 19:59 PST", inline=False)
    ev2.add_field(name="Ticket Claiming period:", value="January 20th 20:00 - January 27th 19:59 PST", inline=False)
    ev2.add_field(name="Social Media Campaing:", value="Distribution Period: January 22nd 20:00 - January 29th 19:59 PST", inline=False)
    await ctx.send(embed=ev2)

    #USE THIS IN A FUTURE: https://stackoverflow.com/questions/55075157/discord-rich-embed-buttons


@bot.command()
async def invite(ctx):
    await ctx.send("Master summon me in your own server!\nhttps://discordapp.com/oauth2/authorize?client_id=668594429573070849&scope=bot&permissions=478272")

@bot.command()
async def help(ctx):
    await ctx.send ("In progress")

## extra
bot.run(TOKEN)
