import discord
from discord.ext import commands
import locale
import random
import datetime


# Set la langue de la date
locale.setlocale(locale.LC_ALL, 'fr_FR')

# Set le token du bot
TOKEN = 'NTA0ODI2NDEzMDY1NDM3MTg1.DrKsGA.-L4vyU7XJ6RtIXSJz8dKpBONAXc'

# Set le prefix
client = discord.Client()

# Set un event lors de l'envoi de message
@client.event
async def on_message(message):

    # Le bot ne se réponds pas
    if message.author == client.user:
        return

    #region Everyone
    # Commande help
    if message.content.lower().startswith('!help'):
        msgHelp = '''Salut {0.author.mention}! 
        Les commandes sont les suivantes:
        !rolldice: Lance un dé
        !date: Montre la date d'aujourd'hui
        [...]
        '''.format(message)
        await client.send_message(message.channel, msgHelp)

    # Commande Date
    if message.content.lower().startswith('!date'):
        time = datetime.date.today().strftime('%d %B %Y')
        await client.send_message(message.channel,f'On est le {time}')
    
    # Commande Roll a Dice
    if message.content.lower().startswith('!rolldice'):
        choix = ['1','2','3','4','5','6']
        choix_random = random.choice(choix)
        if choix_random == '1':
            await client.send_message(message.channel, f'Le dé est tombé sur la face à {choix_random} point.')
        else:
            await client.send_message(message.channel, f'Le dé est tombé sur la face à {choix_random} points.')
         
    #endregion

    #region Mods
    if "god" in [y.name.lower() for y in message.author.roles]:

        #Commande help pour les mods
        if message.content.lower().startswith('!mods'):
            msgHelp = '''Salut {0.author.mention}! 
            Les commandes pour les mods sont les suivantes:
            [En cours de création]
            !clear: Supprime les 5 derniers messages
                --> Bientôt: Décider le nombre de message
            [...]
            '''.format(message)
            await client.send_message(message.channel, msgHelp)
        
        #Commande clear
        if message.content.lower().startswith('!clear'):
            async for msg in client.logs_from(message.channel, limit=6):
                await client.delete_message(msg)     
            await client.send_message(message.channel, 'Les 5 derniers messages ont été supprimé')

    #endregion



# Set un event lorsque le programe est partie    
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)