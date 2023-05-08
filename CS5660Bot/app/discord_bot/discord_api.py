from dotenv import load_dotenv
import discord
import os
from app.chatbot_ai.openai import chatbot_response


load_dotenv()

discord_token = os.getenv("DISCORD_TOKEN")

class MyClient(discord.Client):
    async def on_ready(self):
        print("Successfully logged in as: ", self.user)

    async def on_message(self, message):
        print(message.content)
        # if the author of the message is the bot itself, we just return to avoid the bot chatting to itself
        if (message.author == self.user):
            return  
        
        command, user_message = None, None

        # check if the start text matches either of the following starters
        for text in ["/judge"]:
            if message.content.startswith(text):
                command=message.content.split(" ")[0]
                user_message=message.content.replace(text, '')
                print(command, user_message)

        if (command == "/judge"):
            bot_response = chatbot_response(prompt=user_message)
            await message.channel.send(f"Answer: {bot_response}")


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)