import discord
import asyncio
import random
import chave
import os
import discord.message

client = discord.Client()
chave = chave.n_chave()

qtd = 1

@client.event
async def on_ready():
    print('BOT ONLINE')
    print(client.user.name)
    print(client.user.id)

    @client.event
    async def on_message(text, ):


            for cont1 in range (qtd):

                if text.content.lower().startswith('addscrim') :
                    info = discord.Embed(
                        title='Informe os dados abaixo!',
                        description=
                        '- Nome do Time\n'
                        '. Data\n'
                        ': Hora',
                    )
                    botmsg = await client.send_message(text.channel, embed=info)
                    
                    print('Iniciando Gravação...')
                    #if text.author.id == '455265787226357760':  # Permissao

                    @client.event
                    async def on_message(text, ):
                        global time
                        global data
                        global hora
                        global info

                        if text.content.lower().startswith('-'):
                                time = 'Nome do Time ' + text.content
                                print(time)
                                # await client.send_message(text.channel, time)

                        if text.content.lower().startswith('.'):
                                data = 'Data ' + text.content
                                # await client.send_message(text.channel, data)
                                print(data)
                        if text.content.lower().startswith(':'):
                                hora = 'Hora ' + text.content
                                # await client.send_message(text.channel, hora)
                                print(hora)


                        if text.content.lower().startswith('confscrim'):
                            info = discord.Embed(
                                title='Scrim Confirmada!\n',
                                description='{}\n {}\n {}\n'.format(time, data, hora)

                            )
                            botmsg = await client.send_message(text.channel, embed=info)
                            print(time, data, hora)


            #else:
                #await client.send_message(text.channel, 'Você não tem permissão!')

            for cont2 in range(1):

                    if text.content.lower().startswith('helpbot'):
                        info = discord.Embed(
                            title='Lista de Comandos',
                            description=
                            'Gravar dados (addscrim)\n'
                            'Add Time ( - )\n'
                            'Add Data ( . )\n'
                            'Add Hora ( : )\n'
                            'Confirmar dados (confscrim)\n'
                            '\nUtilize os comandos sem parênteses'
                        )
                        botmsg = await client.send_message(text.channel, embed=info)
                        # print(cont2)


client.run(chave)
