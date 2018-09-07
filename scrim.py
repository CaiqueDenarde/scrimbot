import discord
import asyncio
import random
import chave
import os
import discord.message

client = discord.Client()
chave = chave.n_chave()


@client.event
async def on_ready():
    print('BOT ONLINE')
    print(client.user.name)
    print(client.user.id)




    @client.event
    async def on_message(text, ):

        global time
        global data
        global hora
        qtd = 1

        
            
        for cont in range(qtd):
            for cont1 in range(1):
                if text.content.lower().startswith('addscrim'):
                      info = discord.Embed(
                          title='Informe os dados abaixo!',
                          description=  # '%Qtd Scrim\n'
                                        '- Nome do Time\n'
                                        '. Data\n'
                                        ': Hora',
                      )
                      botmsg = await client.send_message(text.channel, embed=info)

                if text.content.lower().startswith('-'):
                        time = 'Nome do Time ' + text.content
                        print(time)
                        # await client.send_message(text.channel, time)

                elif text.content.lower().startswith('.'):
                        data = 'Data ' + text.content
                        # await client.send_message(text.channel, data)
                        print(data)
                elif text.content.lower().startswith(':'):
                        hora = 'Hora ' + text.content
                        # await client.send_message(text.channel, hora)
                        print(hora)
                if text.content.lower().startswith("confscrim"):
                        info = discord.Embed(
                            title='Scrim Confirmada!\n',
                            description='{}\n {}\n {}\n'.format(time, data, hora)

                        )
                        botmsg = await client.send_message(text.channel, embed=info)


client.run(chave)
