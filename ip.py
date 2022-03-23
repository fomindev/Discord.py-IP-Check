import discord
from discord.ext import commands
import asyncio
from pyrsistent import field
import requests
import datetime

class ip(commands.Cog):
  def __init__(self, client):
    self.client = client    

  @commands.command()
  async def ip(self, ctx, *, ip: str = '9.9.9.9'):
    r = requests.get(f"https://extreme-ip-lookup.com/json/{ip}?key='Тут свой ключ'")
    geo = r.json()
    em = discord.Embed()
    fields = [
      {'name': 'IP', 'value': geo['query']},
      {'name': 'Тип IP', 'value': geo['ipType']},
      {'name': 'Страна', 'value': geo['country']},
      {'name': 'Город', 'value': geo['city']},
      {'name': 'Континент', 'value': geo['continent']},
      {'name': 'IP Имя', 'value': geo['ipName']},
      {'name': 'ISP', 'value': geo['isp']},
      {'name': 'Lat', 'value': geo['lat']},
      {'name': 'lot', 'value': geo['lot']},
      {'name': 'Org', 'value': geo['org']},
      {'name': 'Регион', 'value': geo['region']},
      {'name': 'Статус', 'value': geo['status']},
    ]
    
    for field in fields:
      if field['value']:
        em.set_footer(text='\u200b')
        em.timestamp = datetime.datetime.utcnow()
        em.add_field(name = field['name'], value = field['value'], inline = True)
    return await ctx.send(embed = em)


def setup(client):
  client.add_cog(ip(client))
