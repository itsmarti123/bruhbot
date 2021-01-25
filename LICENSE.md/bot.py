import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print('Bruh im Ready')
  
@client.event
async def on_message():
  if message.author == client.user:
    return

  if message.content.startswith('.help'):
    embedVar = discord.Embed(title="Help", description="Bruh Help", color=0xff0000)
    embedVar.add_field(name=".Vote - Vote this Discord Server on top.gg, .invite - sends you an invite link to invite more people to this server", value="Help", inline=False)
    await message.channel.send(embed=embedVar)
