import discord
import os
import requests
import json
import random
from replit import db
client = discord.Client()


ListThatContainsF=["Fuck","fuck","fuq","fok","fuckk","fucking"]
ListYourMom=["Your Mom", "mom", "ur mom"]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

def update_anything(any_message):
  if 

@client.event
async def on_ready():
 print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  


  if message.content.startswith('hoiya quote'):
    quotecmd = get_quote()
    await message.channel.send(quotecmd)
  if any(word in message.content for word in ListThatContainsF):
    await message.channel.send("Why you fuck me I fuck you bloody")
  if any(word in message.content for word in ListYourMom):
    await message.channel.send("No YOUR Momfrom replit import db")

client.run(os.getenv('TOKEN2'))