import discord
from discord.ext import commands
from PIL import Image
from funkcja import detect_mushroom

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'You logged in as {bot.user}')

@bot.command()
async def image(ctx):
    if len(ctx.message.attachments) > 0:
        for attachment in ctx.message.attachments:
            print(attachment.filename)
            print(attachment.url)
            file_path = f"./Images/{attachment.filename}"
            await attachment.save(file_path)
            image=Image.open(file_path)
            detected_class = detect_mushroom("keras_model.h5", "labels.txt", image)
            await ctx.send(f"I recognized {detected_class[0]} mushrooms in the attached image.")
    else:
        await ctx.send("There was no image attached!")

bot.run("YOUR TOKEN")
