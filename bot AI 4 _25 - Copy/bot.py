import discord
import asyncio
import os 
import random
from bot_logic import gen_pass
from discord.ext import commands
from clasificador import clasf

intents = discord.Intents.default()

intents.message_content = True


bot = commands.Bot(command_prefix = "$",intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send("HI!")

@bot.command()
async def basura(ctx):
    with open('imagen/basura1.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send("Basurero Amarillo:")
    await ctx.send(file=picture)
    await ctx.send("Está destinado a los plásticos y los envases. Esto incluye botellas de plástico, bolsas, envases de comida, y envases de productos como detergentes o cosméticos.")
    with open('imagen/basura2.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send("Basurero Azul:")
    await ctx.send(file=picture)
    await ctx.send("Se utiliza para recoger papel y cartón. Estos materiales son fácilmente reciclables y se reutilizan en la fabricación de nuevos productos.")
    with open('imagen/basura3.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send("Basurero Verde:")
    await ctx.send(file=picture)
    await ctx.send(" Está destinado al reciclaje de vidrio. El vidrio es un material que se puede reciclar infinitamente sin perder calidad.")
    with open('imagen/basura4.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send("Basurero Marrón:")
    await ctx.send(file=picture)
    await ctx.send(" Es utilizado para los residuos orgánicos que se pueden descomponer biológicamente, como restos de comida, cáscaras de frutas, vegetales, y otros desechos biodegradables.")
    with open('imagen/basura5.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send("Basurero Gris o Negro:")
    await ctx.send(file=picture)
    await ctx.send("Este basurero es para los residuos que no se pueden reciclar ni compostar. Todo lo que no encaje en los otros contenedores debe ir aquí.")
    with open('imagen/basura6.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send("Basurero Naranja:")
    await ctx.send(file=picture)
    await ctx.send("En algunos países o regiones, el basurero naranja se usa para residuos peligrosos, como baterías, bombillas, medicamentos caducados, productos químicos, y otros elementos que requieren un manejo especial.")



@bot.command()
async def dato_ecologico(ctx):
    datos_ecologicos = [
        "Según la Unión Internacional para la Conservación de la Naturaleza (UICN), más de 42,100 especies están en peligro de extinción.",
        "Cada año, el mundo pierde aproximadamente 18 millones de acres de bosques tropicales, lo que equivale a la desaparición de un campo de fútbol cada segundo.",
        "El 70% de los océanos están aún inexplorados, y muchos ecosistemas marinos siguen siendo un misterio.",
        "Más de 1,000 especies de animales y plantas han desaparecido en los últimos 500 años debido a actividades humanas.",
        "Las áreas protegidas en el planeta solo cubren alrededor del 15% de la superficie terrestre, aunque se necesita más para preservar la biodiversidad.",
    ]
    
    dato_aleatorio = random.choice(datos_ecologicos)
    await ctx.send(dato_aleatorio)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            image_estensions = ('.jpg','.jpeg','.png')

            if file_name.endswith(image_estensions):
                await attachment.save (f'./images/{file_name}')
                await ctx.send(clasf(f"./images/{file_name}"))
            else:
                await ctx.send(f'el archivo no es una imagen valida')
    else:
        await ctx.send(f'no se ha selecionado ningun archivo')    

bot.run("token")

