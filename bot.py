import discord
import os

client = discord.Client()

token = 'Nzk3MzY1ODgxNzA1MjAxNjc0.X_la2A.MZZ2_a1_fQhs_3TYN02rK1w5_D0'

@client.event
async def on_ready():
  print('Bruh im Ready')
  
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('.help'):
    embedVar = discord.Embed(title="Help", description="Bruh Bot Help", color=0xff0000)
    embedVar.add_field(name=".cat - Shows you some cute cats, .invite - Sends you an invite link for the server, .vote vote this server", value="Help", inline=False)
    await message.channel.send(embed=embedVar)
        
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=".help"))
      
client.run(token)
