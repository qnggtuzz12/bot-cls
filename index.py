
from distutils.log import error
from email import message
import typing
import discord
from discord.ext import commands
import datetime
from urllib import parse, request
import re
import random
import os
import youtube_dl
from dotenv import load_dotenv
import asyncio

https://github.com/qnggtuzz12/bot-cls/blob/main/index.py
youtube_dl.utils.bug_reports_message = lambda: ''
ytdl_format_options = {
    'format': 'bestaudio/best',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}
ffmpeg_options = {
    'options': '-vn'
}
ytdl = youtube_dl.YoutubeDL(ytdl_format_options)
class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = ""
    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]
        filename = data['title'] if stream else ytdl.prepare_filename(data)
        return filename

intents = discord.Intents.default()  # All but the two privileged ones
intents.members = True
bot = commands.Bot(command_prefix='>')



async def ching(ctx):
    await ctx.send('chong')

@bot.command()
@commands.is_owner() 
async def Tuấn(ctx):
    await ctx.send('Tuấn Là thằng lồn ')    

@bot.command()
async def cong(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne + numTwo)

@bot.command()
async def tru(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne - numTwo)

@bot.command()
async def chia(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne / numTwo)

@bot.command()
async def nhan(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne * numTwo)



@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Thông Tin Sever", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="📆Tạo vào lúc", value=f"{ctx.guild.created_at}")
    embed.add_field(name='👑Owner', value=f"Cestaa#9608")
    embed.add_field(name="🌎Khu Vực", value=f"VietNam")
    embed.add_field(name="🆔ID Sever", value=f"{ctx.guild.id}")
    embed.add_field(name = '👥Members', value = f'{ctx.guild.member_count} Members', inline = True)
    embed.set_thumbnail(url = ctx.guild.icon_url)   
    
    
    await ctx.send(embed=embed)

@bot.command(name="whois")
async def whois(ctx,user:discord.Member=None):

    if user==None:
        user=ctx.author

    rlist = []
    for role in user.roles:
      if role.name != "@everyone":
        rlist.append(role.mention)

    b = ", ".join(rlist)


    embed = discord.Embed(colour=user.color,timestamp=ctx.message.created_at)

    embed.set_author(name=f"User Info - {user}"),
    embed.set_thumbnail(url=user.avatar_url),
    embed.set_footer(text=f'Requested by - {ctx.author}',
  icon_url=ctx.author.avatar_url)

    embed.add_field(name='ID:',value=user.id,inline=False)
    embed.add_field(name='Name:',value=user.display_name,inline=False)

    embed.add_field(name='Created at:',value=user.created_at,inline=False)
    embed.add_field(name='Joined at:',value=user.joined_at,inline=False)

  
 
    embed.add_field(name='Bot?',value=user.bot,inline=False)

    embed.add_field(name=f'Roles:({len(rlist)})',value=''.join([b]),inline=False)
    embed.add_field(name='Top Role:',value=user.top_role.mention,inline=False)

    await ctx.send(embed=embed)
  
# Events
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Prefix >", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"))
    print('Chạy rồi nhéeeeeeeeeee')


@bot.listen()
async def on_message(message):
    if "tutorial" in message.content.lower():
        # in this case don't respond with the word "Tutorial" or you will call the on_message event recursively
        await message.channel.send('This is that you want http://youtube.com/fazttech')
        await bot.process_commands(message)

@bot.command()  
async def Thụ(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/944142203595415572/945512166906269736/Untitled.png')
    help="Gửi ảnh em thụ"
@bot.command()
async def summonNam(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/937706032321429567/945557454408810536/dcac_nam.png')
    help="Gửi ảnh nam"
@bot.command()
async def nam(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/937736801383227513/945571409067900988/Capture_2022-01-16-20-55-00.jpg')
    help="Gửi ảnh nam"

@bot.command()
async def membercount(ctx):
    embed = discord.Embed(title=f"Membercount", description="Membercount", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name = '👥Members', value = f'{ctx.guild.member_count} Members', inline = True)
        

    await ctx.send(embed=embed)
    "Xem lượng Member"
    
@bot.command()  
async def tim(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/884437847984201738/943131398032740402/272231297_1299286753873407_4370729423163804723_n.png')
    "Gửi ảnh Thụ thả tim"
@bot.command()
@commands.is_owner()  
async def gaisalime(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/937706032321429567/946002068903186452/video_1645456937717.mp4')
help="Gửi ảnh thằng Tú"

    
@bot.command(name='vaovoice', help='Tells the bot to join the voice channel')
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name))
        return
    else:
        channel = ctx.message.author.voice.channel
    await channel.connect()
@bot.command(name='outvoice', help='To make the bot leave the voice channel')
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_connected():
        await voice_client.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")
            
@bot.command(name='choinhac', help='To play song')
async def choi(ctx,url):
    try :
        server = ctx.message.guild
        voice_channel = server.voice_client
        async with ctx.typing():
            filename = await YTDLSource.from_url(url, loop=bot.loop)
            voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source=filename))
        await ctx.send('**Now playing:** {}'.format(url))
    except:
        await ctx.send("The bot is not connected to a voice channel.")
@bot.command(name='dunglai', help='This command pauses the song')
async def pause(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        await voice_client.pause()
    else:
        await ctx.send("The bot is not playing anything at the moment.")
    

@bot.command(name='tiep', help='Resumes the song')
async def resume(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_paused():
        await voice_client.resume()
    else:
        await ctx.send("The bot was not playing anything before this. Use play_song command")
@bot.command(name='dunghan', help='Stops the song')
async def stop(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        await voice_client.stop()
    else:
        await ctx.send("The bot is not playing anything at the moment.")

@bot.command()  
@commands.is_owner()
async def LamNam(ctx):
     await ctx.send('https://cdn.discordapp.com/attachments/923931352435417088/942105205586149396/1.jpg')

@bot.command()
@commands.is_owner()  
async def tusngoaymui(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/937706032321429567/946001428802076703/unknown.png')

@bot.command(aliases=['role'])
@commands.has_permissions(manage_roles=True) # Check if the user executing the command can manage roles
async def taorole(ctx, *, name):
	guild = ctx.guild
	await guild.create_role(name=name)
	await ctx.send(f'Role `{name}` has been created')

@bot.command(name="delete_role", pass_context=True)
@commands.has_permissions(manage_roles=True)
async def xoarole(ctx, role_name):
    #find role object
    role_object = discord.utils.get(ctx.message.guild.roles, name=role_name)
    #delete role
    await role_object.delete()
    await ctx.send(f'Role `{role_name}` has been deleted')


@bot.command(name='quyen')
@commands.has_permissions(administrator=True) #permissions
async def role(ctx, user : discord.Member, *, role : discord.Role):
  if role.position > ctx.author.top_role.position: #if the role is above users top role it sends error
    return await ctx.send('**:x: | That role is above your top role!**') 
  if role in user.roles:
      await user.remove_roles(role) #removes the role if user already has
      await ctx.send(f"Removed `{role}` from {user.mention}")
  else:
      await user.add_roles(role) #adds role if not already has it
      await ctx.send(f"Added `{role}` to {user.mention}") 

@bot.command()
async def feed(ctx, member:discord.Member = None):
    feedGIF = [    
        "https://i.imgur.com/1vC0R20.gif",
        "https://data.whicdn.com/images/81561319/original.gif",
        "https://thumbs.gfycat.com/EagerSpectacularHoverfly-max-14mb.gif",
        "https://64.media.tumblr.com/4d160635539ef31d8b058bc3e35a907c/tumblr_p4e113SOw91wn2b96o1_400.gifv",
        "https://i.pinimg.com/originals/7a/cb/20/7acb209c594f42e0d56b87d70421c85d.gif",
    ]  

    if (member == ctx.author or member == None):
        feedSelfResponse = [
            f"{ctx.author.mention} feeds them selves. So eating?",
            f"{ctx.author.mention} feeds themselves yum!",
            f"{ctx.author.mention} is feeding their hungry stomach",
            f"{ctx.author.mention} is being fed by... themselves",
        ]
        feed = random.choice(feedSelfResponse)
        embed = discord.Embed(color=0x9b59b6)
        embed.set_image(url=random.choice(feedGIF))
        embed.add_field(name="Feed", value=(feed))
        await ctx.send(embed=embed)
    else:
        feedResponse = [ 
            f"{ctx.author.mention} feeds {member.mention}",
            f"{member.mention} is being feed by {ctx.author.mention}. Open wide!",
            f"Yum! {ctx.author.mention} feeds {member.mention}. Here comes the airplane!",    
        ]  
        feed = random.choice(feedResponse)
        embed = discord.Embed(color=0x9b59b6)
        embed.set_image(url=random.choice(feedGIF))
        embed.add_field(name="Feed", value=(feed))
        await ctx.send(embed=embed)

@bot.command()
async def punch(ctx, member:discord.Member = None):
    feedGIF = [    
        "https://i.pinimg.com/originals/8d/50/60/8d50607e59db86b5afcc21304194ba57.gif",
        "https://c.tenor.com/_Oc464iCoDYAAAAC/my-hero-punch.gif",
        "https://thumbs.gfycat.com/GrandAlertCaimanlizard-max-1mb.gif",
        "https://i.pinimg.com/originals/ad/2f/a1/ad2fa117882b2a5a1171c21678d13268.gif",
        "https://i.gifer.com/8XAW.gif",
    ]  

    if (member == ctx.author or member == None):
        feedSelfResponse = [
            f"{ctx.author.mention} Xem ta đâyyy",
            f"{ctx.author.mention} Một đấm nhéeeee!",
            f"{ctx.author.mention} Aaaaaaa! Chết con mẹ mày!",
            f"{ctx.author.mention} Đmm! Chết nha con!",
        ]
        feed = random.choice(feedSelfResponse)
        embed = discord.Embed(color=0x9b59b6)
        embed.set_image(url=random.choice(feedGIF))
        embed.add_field(name="Feed", value=(feed))
        await ctx.send(embed=embed)
    else:
        feedResponse = [ 
            f"{ctx.author.mention} Đấm {member.mention}",
            f"{member.mention}  đã bị đấm bởi {ctx.author.mention}. Vỡ mồm con chó!",
            f"Yum! {ctx.author.mention} Đấm {member.mention}. Chết mẹ mày đi!",    
        ]  
        feed = random.choice(feedResponse)
        embed = discord.Embed(color=0x9b59b6)
        embed.set_image(url=random.choice(feedGIF))
        embed.add_field(name="Đấm", value=(feed))
        await ctx.send(embed=embed)


@bot.command()
async def kiss(ctx, member:discord.Member = None):
    feedGIF = [    
        "https://i.pinimg.com/originals/f1/5c/77/f15c774e5c58a9f210c7f7647da796f1.gif",
        "https://www.icegif.com/wp-content/uploads/2021/10/icegif-1008.gif",
        "https://thumbs.gfycat.com/WarpedSlightFrigatebird-max-1mb.gif",
        "https://i.pinimg.com/originals/d0/cd/64/d0cd64030f383d56e7edc54a484d4b8d.gif",
        "https://i.gifer.com/YQzo.gif",
    ]  

    if (member == ctx.author or member == None):
        feedSelfResponse = [
            f"{ctx.author.mention} Hônnnnn nè",
            f"{ctx.author.mention} Tôi hôn bạn nè !",
            f"{ctx.author.mention} Moaaaaaaaaaa",
            f"{ctx.author.mention} Moaaaaaaa",
        ]
        feed = random.choice(feedSelfResponse)
        embed = discord.Embed(color=0x9b59b6)
        embed.set_image(url=random.choice(feedGIF))
        embed.add_field(name="Kiss", value=(feed))
        await ctx.send(embed=embed)
    else:
        feedResponse = [ 
            f"{ctx.author.mention} hôn {member.mention}",
            f"{member.mention} Đã hôn  {ctx.author.mention}. Moaaaaaaaaaa!",
            f"Yum! {ctx.author.mention} Moa moa {member.mention}. chụt chụt",    
        ]  
        feed = random.choice(feedResponse)
        embed = discord.Embed(color=0x9b59b6)
        embed.set_image(url=random.choice(feedGIF))
        embed.add_field(name="Kiss", value=(feed))
        await ctx.send(embed=embed)




@bot.command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx, channel : discord.TextChannel=None):
    overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send(ctx.channel.mention + " ***Bị khoá mõm rồiii.***")

@bot.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
    await ctx.send(ctx.channel.mention + " ***has been unlocked.***")
    
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass in all requirements :rolling_eyes:.')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(ctx.author.mention + "***Bạn không có quyền*** ")

@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)

    await ctx.send(f'User `{member}` has been ban')

#The below code unbans player.
@bot.command()
@commands.has_permissions(administrator = True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.id}')
            return

@bot.command()
@commands.has_permissions(ban_members = True)
async def kick(ctx, member : discord.Member, *, reason = None):
    await member.kick(reason = reason)

    await ctx.send(f'User ***{member}*** has been kick')

bot.run('ur token')
