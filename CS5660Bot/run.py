from app.discord_bot.discord_api import client, discord_token

# it ensures the code is run as the main code
if __name__ == "__main__":
    client.run(discord_token)
    