import discord
import asyncio
import random
import chave
import os
import discord.message

client = discord.Client()
chave = chave.n_chave()



cont = 0

@client.event
async def on_ready():
    print('BOT ONLINE')
    print(client.user.name)
    print(client.user.id)

@client.event
async def on_message(text,):

    if text.content.lower().startswith('addscrim'):
       info =discord.Embed(
       title='Informe os dados abaixo!',
       description='- Nome do Time\n'
                             '. Data\n'
                             ': Hora',
       )
       botmsg = await client.send_message(text.channel, embed=info)


    @client.event
    async def on_message (text,):

        global time
        global data
        global hora
        
        while cont == 0:
            for cont in range (1):
                if text.content.lower().startswith('-'):
                    time = 'Nome do Time '+text.content
                    print(time)
                    # await client.send_message(text.channel, time)

                elif text.content.lower().startswith('.'):
                    data = 'Data '+text.content
                    # await client.send_message(text.channel, data)
                    print(data)
                elif text.content.lower().startswith(':'):
                    hora = 'Hora '+text.content
                    # await client.send_message(text.channel, hora)
                    print(hora)
                if text.content.lower().startswith("confscrim"):
                    info = discord.Embed(
                        title='Scrim Confirmada!\n',
                        description='{}\n {}\n {}\n'.format(time,data,hora)

                    )
                    botmsg = await client.send_message(text.channel, embed=info)


               










client.run(chave)
