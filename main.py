#!/usr/bin/env python
# -*- coding: utf-8 -*-
import discord
from discord.ext import commands
from discord.utils import get
from credentials import TOKEN
from datetime import datetime
from pytz import timezone, utc

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

## Main_Commands

@bot.command()
async def events(ctx):
    await ctx.send("Hi master, you can check the active and future events at this webpage:\nhttps://fategrandorder.fandom.com/wiki/Event_List_(US)")
    #await ctx.send("Hi master, you can check the active and future events at this webpage:\nLINK")

@bot.command()
async def aevents(ctx): #active events

    ac_ev_list = discord.Embed(title="FGO active events", description="FGO (USA)", color=0x00ff00)
    ac_ev_list.add_field(name="Fate/Grand Order Absolute Demonic Front: Babylonia Anime Release Campaign Part II (US)", value="Duration: January 20th 20:00 - January 29th 19:59 PST\nRequisites: Clear Fuyuki", inline=True)
    await ctx.send(embed=ac_ev_list)

    ev1 = discord.Embed(title="Fate/Grand Order Absolute Demonic Front: Babylonia Anime Release Campaign Part II (US)", url="https://fategrandorder.fandom.com/wiki/Fate/Grand_Order_Absolute_Demonic_Front:_Babylonia_Anime_Release_Campaign_Part_II_(US)", color=0x345ceb)
    ev1.set_thumbnail(url="https://vignette.wikia.nocookie.net/fategrandorder/images/8/85/BabyloniaCampaignTicketUS.png/revision/latest/scale-to-width-down/680?cb=20200117051322")
    ev1.add_field(name="Requisites:", value="Clear Fuyuki", inline=False)
    ev1.add_field(name="Exchange period:", value="January 22nd 20:00 - January 29th 19:59 PST", inline=False)
    ev1.add_field(name="Ticket Claiming period:", value="January 20th 20:00 - January 27th 19:59 PST", inline=False)
    ev1.add_field(name="Social Media Campaing:", value="Distribution Period: January 22nd 20:00 - January 29th 19:59 PST", inline=False)
    await ctx.send(embed=ev1)

    #USE THIS IN A FUTURE: https://stackoverflow.com/questions/55075157/discord-rich-embed-buttons


@bot.command()
async def invite(ctx):
    await ctx.send("Master summon me in your own server!\nhttps://discordapp.com/oauth2/authorize?client_id=668594429573070849&scope=bot&permissions=478272")

@bot.command()
async def help(ctx):
    await ctx.send ("In progress")

@bot.command()
async def time(ctx):
    time_format='%H:%M %Z'
    time = datetime.now(tz=utc)
    time = time.astimezone(timezone('US/Pacific'))
    pstTime=time.strftime(time_format)
    await ctx.send("PST time: "+pstTime)

## extra
bot.run(TOKEN)