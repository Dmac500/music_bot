import os
import discord
from discord.ext import commands
from GoogleNews import GoogleNews
from newspaper import Article
import pandas as pd
import datetime
import random


bot = commands.Bot(command_prefix='.')
@bot.command()
async def hello(ctx):
  await ctx.reply('hello!')

@bot.command()
async def add(ctx,num1:int,num2:int):
  await ctx.reply(num1 + num2)

@bot.command()
async def findArtical(ctx):
  today = datetime.datetime.today()
  weekAgo=datetime.datetime.today() - datetime.timedelta(days=7)
  
  d1 = today.strftime("%m/%d/%Y")
  d2 = weekAgo.strftime("%m/%d/%Y")
  googlenews=GoogleNews(start=d2,end=d1)
  googlenews.search('ufc')
  result=googlenews.result()
  print(len(result))
  df=pd.DataFrame(result)
  await ctx.reply(df['link'][random.randint(0,len(result)-1)])


my_secret = os.environ['Token']
bot.run(my_secret)
