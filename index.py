from discord.ext import commands
from decouple import config
import discord
import os

intents = discord.Intents.default()
intents.message_content = True
intents.members = True  
bot = commands.Bot(command_prefix='!', intents=intents)

import asyncio

async def carregar_cogs():

    await bot.load_extension('Commands.coordenador')
    await bot.load_extension('Commands.aluno')

    


@bot.event
async def on_member_join(member):
    print(f"{member.name} entrou no servidor {member.guild.name}.")
    await member.send(
    f"🎉 **Olá, {member.name}!** Bem-vindo(a) ao bot ifrn! Estou á disposição!🎉\n\n"
        "Bem-vindo(a) mais uma vez, e que você tenha uma ótima jornada por aqui! 😄"
    )

    
        

@bot.event
async def on_ready():
    await carregar_cogs()
    await bot.tree.sync() 
    print(f'Bot está conectado.')
            


        

TOKEN = config("TOKEN")

bot.run(TOKEN)
