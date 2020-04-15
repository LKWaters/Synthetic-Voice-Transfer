import discord
from discord.ext import commands
import time
from synthesize import synthesize
import multiprocessing



if __name__ == '__main__':

    TOKEN = 'Njk2Njg2MzM3NTA3NTkwMjQ0.XosV5w.neY-Sgpo8UAHiAzaS6e0b-nIRuY'
    client = commands.Bot(command_prefix='!')

    @client.event
    async def on_ready():
        print('Bot online.')


    @client.command(pass_context = True)
    async def make(ctx,*, sentance):
        sen = str(sentance)
        print(sen)
        p1 = multiprocessing.Process(target = synthesize, args=(sen,))
        p1.start()
        p1.join()
        await ctx.send("Ready")

    @client.command(pass_context = True)
    async def say(ctx):
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        guild = ctx.message.guild
        voice_client = guild.voice_client
        voice_client.play(discord.FFmpegPCMAudio(executable='C:/Users/Leighton Waters/Documents/ffmpeg/bin/ffmpeg.exe',source='C:/Users/Leighton Waters/Desktop/WOWSC/TeoBot/1.wav'), after=lambda e: print('done', e))
        while voice_client.is_playing():
                time.sleep(1)
        voice_client.stop()
        await voice_client.disconnect()



    client.run(TOKEN)

