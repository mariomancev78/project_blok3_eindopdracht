import sys
import click
from week_1.disable_defender import disable_defender, show_running_processes, show_banner, check_defender_status, check_os
from week_2.discord_bot import start_bot
from week_3.screenshot.take_screenshot import take_screenshot
from week_3.mic.record_mic import record_mic, list_audio_devices


accepted_functions = ["disable_defender",
                      "ps",
                      "check_defender_status",
                      "start_discord_bot",
                      "take_screenshot",
                      "record_mic",
                      "list_audio_devices"]


@click.command()
@click.option("--action", help="De actie die uitgevoerd moet worden.", type=click.Choice(accepted_functions))
def main(action):
    if not action:
        show_banner()
        action = click.prompt("Welke actie wil je uitvoeren?",
                              type=click.Choice(accepted_functions))
    match action:
        case "disable_defender":
            if check_os():
                click.echo(disable_defender())
            else:
                click.echo(f"Deze functie werkt alleen in een Windows omgeving. Jouw OS: {
                           sys.platform}")
        case "ps":
            click.echo(show_running_processes())
        case "check_defender_status":
            if check_os():
                click.echo(check_defender_status())
            else:
                click.echo(f"Deze functie werkt alleen in een Windows omgeving. Jouw OS: {
                           sys.platform}")
        case "start_discord_bot":
            start_bot()
        case "take_screenshot":
            click.echo(take_screenshot())
        case "record_mic":
            click.echo(record_mic())
        case "list_audio_devices":
            result = list_audio_devices()
            if type(result) is dict:
                for id, name in result.items():
                    print(f"Id:{id}, naam: {name} ")
            else:
                click.echo(
                    f"er ging iets mis tijdens het ophalen van apparaten: {result}")


if __name__ == '__main__':
    main()


# TODO: Implement check for the available audio devices
# TODO: Implement info on available monitors, and make it possible for end user to select a monitor to capture
# TODO make it possible to specify the amount of seconds to record.
