import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

files = os.listdir('./code')
questionDict = {}
for each in files:
    ind = each.index('.')
    questionDict[each[0:ind]] = each[ind+2:-3]


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    


@bot.command(name='list', help='Lists all questions')
async def displayList(ctx):
    response = questionDict
    await ctx.send(response)


@bot.command(name='getq', help='Usage: !q question#')
async def questionQuery(ctx, num):
    if num not in questionDict:
        response = "Question not found."
    else:
        path = "./code/" + num + ". " + questionDict[num] + ".py"
        content = readFile(path)        
        question = ""

        for each in content:
            if "#" in each:
                question += each[2:-1] + "\n"

        response = question

    await ctx.send(response)

@bot.command(name='getsh', help='Get small hint')
async def smallHintQuery(ctx, num):
    if num not in questionDict:
        response = "Question not found."
    else:
        path = "./code/" + num + ". " + questionDict[num] + ".py"
        content = readFile(path)        
        hints = ""

        for each in content:
            if "##" in each:
                hints += each[3:-1]
        response = hints

  
    await ctx.send(response)

@bot.command(name='getbh', help='Get big hint')
async def bigHintQuery(ctx, num):
    if num not in questionDict:
        response = "Question not found."
    else:
        path = "./code/" + num + ". " + questionDict[num] + ".py"
        content = readFile(path)        
        hints = ""

        for each in content:
            if "###" in each:
                hints += each[4:-1]
        response = hints
    await ctx.send(response)

def readFile(filepath):
    f = open(filepath, "r")
    content = f.readlines()
    content = [i.strip() for i in content]
    f.close()
    return content

bot.run(TOKEN)