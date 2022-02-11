import discord
import json

with open("discBot.json", 'r') as f:
        data = json.load(f)



class MyClient(discord.Client):

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        
        if message.content == '/hello':
            await message.channel.send(f'Hey! {message.author}\n Have a good day!')
        if message.content == 'bing':
            await message.channel.send('bong')
        


client = MyClient()
client.run(data["token"])