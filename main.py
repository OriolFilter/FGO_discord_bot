#!/usr/bin/env python
# -*- coding: utf-8 -*-
import discord
import os
from discord.ext import commands
from discord.utils import get
from credentials import TOKEN
from datetime import datetime
from pytz import timezone, utc

description = '''Master im waiting for you to summon me!'''


bot = commands.Bot(command_prefix="f.", description=description)
bot.remove_command('help')

#Variables
where_i_im=os.path.dirname(os.path.abspath(__file__)) #where is the file/folder of this python document...
help_p1_file_location=where_i_im+"/help_pt1.txt"

@bot.event
async def on_ready():
    print('------')
    print('Logged as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    game = discord.Game("I will help you master, type \"f.help\" if you still need learn to summon me!")
    await bot.change_presence(status=discord.Status.online, activity=game)

## Main_Commands

#Events
@bot.command()
async def events(ctx):
    await ctx.send("Hi master, you can check the active and future events at this webpage:\nhttps://fategrandorder.fandom.com/wiki/Event_List_(US)")

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
async def fevents(ctx): #future events

    fe_ev_list = discord.Embed(title="FGO future events", description="FGO (USA)", color=0x03c6da)
    fe_ev_list.add_field(name="The Tale of Setsubun (US)", value="Duration: January 27th 00:00 - February 2nd 19:59 PST\nRequisites: Clear Solomon", inline=True)
    await ctx.send(embed=fe_ev_list)

    tale_of_setsubun = discord.Embed(title="The Tale of Setsubun (US)", description="Duration: January 27th 00:00 - February 2nd 19:59 PST\nRequisites: Clear Solomon", url="https://fategrandorder.fandom.com/wiki/The_Tale_of_Setsubun_(US)", color=0xcf1f33)
    tale_of_setsubun.set_thumbnail(url="https://vignette.wikia.nocookie.net/fategrandorder/images/d/dc/SetsubunEventUS.png/revision/latest/scale-to-width-down/680?cb=20200120050724")
    tale_of_setsubun.add_field(name="Requisites:", value="Clear Solomon", inline=False)
    tale_of_setsubun.add_field(name="Duration:", value="January 27th 00:00 - February 2nd 19:59 PST", inline=False)
    await ctx.send(embed=tale_of_setsubun)


#Class
@bot.command()
async def classes(ctx):
    await ctx.send("Master i see you are in a search of knowledge, let me help you with this books!\n\nSaber:\t\t         <https://fategrandorder.fandom.com/wiki/Saber>\nLancer:\t\t       <https://fategrandorder.fandom.com/wiki/Lancer>\nArcher:\t\t       <https://fategrandorder.fandom.com/wiki/Archer>\nRider:\t\t          <https://fategrandorder.fandom.com/wiki/Rider>\nCaster:\t\t        <https://fategrandorder.fandom.com/wiki/Caster>\nAssassin:\t\t    <https://fategrandorder.fandom.com/wiki/Assassin>\nBerserker:\t\t   <https://fategrandorder.fandom.com/wiki/Berserker>\nShielder:\t\t      <https://fategrandorder.fandom.com/wiki/Shielder>\nRuler:\t\t\t       <https://fategrandorder.fandom.com/wiki/Ruler>\nAvenger:\t\t\t <https://fategrandorder.fandom.com/wiki/Avenger>\nMoon Cancer:\t<https://fategrandorder.fandom.com/wiki/Moon_Cancer>\nForeigner:\t\t    <https://fategrandorder.fandom.com/wiki/Foreigner>\nBeast:\t\t\t       <https://fategrandorder.fandom.com/wiki/Beast>")

@bot.command()
async def saber(ctx):
    await ctx.send("Here is what you asked for master!\nhttps://fategrandorder.fandom.com/wiki/Saber")

@bot.command()
async def lancer(ctx):
    await ctx.send("Here is what you asked for master!\nhttps://fategrandorder.fandom.com/wiki/Lancer")

@bot.command()
async def archer(ctx):
    await ctx.send("Here is what you asked for master!\nhttps://fategrandorder.fandom.com/wiki/Archer")

@bot.command()
async def caster(ctx):
    await ctx.send("Here is what you asked for master!\nhttps://fategrandorder.fandom.com/wiki/Caster")

@bot.command()
async def assassin(ctx):
    await ctx.send("Here is what you asked for master!\nhttps://fategrandorder.fandom.com/wiki/Assassin")

@bot.command()
async def rider(ctx):
    await ctx.send("Here is what you asked for master!\nhttps://fategrandorder.fandom.com/wiki/Rider")

@bot.command()
async def berserker(ctx):
    await ctx.send("Here is what you asked for master!\nhttps://fategrandorder.fandom.com/wiki/Berserker")

@bot.command()
async def shielder(ctx):
    await ctx.send("Here is what you asked for master!\nhttps://fategrandorder.fandom.com/wiki/Shielder")

@bot.command()
async def ruler(ctx):
    await ctx.send("Here is what you asked for master!\nhttps://fategrandorder.fandom.com/wiki/Ruler")

@bot.command()
async def avenger(ctx):
    await ctx.send("Here is what you asked for master!\nhttps://fategrandorder.fandom.com/wiki/Avenger")

@bot.command()
async def mooncancer(ctx): #moon cancer
    await ctx.send("Here is what you asked for master!\nhttps://fategrandorder.fandom.com/wiki/Moon_Cancer")

@bot.command()
async def alterego(ctx):
    await ctx.send("Here is what you asked for master!\nhttps://fategrandorder.fandom.com/wiki/Alter_Ego")

@bot.command()
async def foreigner(ctx):
    await ctx.send("Here is what you asked for master!\nhttps://fategrandorder.fandom.com/wiki/Foreigner")

@bot.command()
async def beast(ctx):
    await ctx.send("Here is what you asked for master!\nhttps://fategrandorder.fandom.com/wiki/Beast")

#Misc
@bot.command()
async def help(ctx):
    help_p1 = open((help_p1_file_location), "r")
    help_msp1 = help_p1.read()
    help_p1.close()
    await ctx.author.send(help_msp1)



@bot.command()
async def time(ctx):
    time_format='%H:%M %Z'
    time = datetime.now(tz=utc)
    time = time.astimezone(timezone('US/Pacific'))
    pstTime=time.strftime(time_format)
    await ctx.send("PST time: "+pstTime)


@bot.command()
async def invite(ctx):
    await ctx.send("Master use this to summon me!\nhttps://discordapp.com/oauth2/authorize?client_id=668594429573070849&scope=bot&permissions=478272")

## extra
bot.run(TOKEN)