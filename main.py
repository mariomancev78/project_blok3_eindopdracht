@click.command()
@click.option("--action", help="De actie die uitgevoerd moet worden.", type=click.Choice(
    ["disable_defender", "ps", "check_defender_status", "start_discord_bot", "take_screenshot"]))
def main(action):
    if not action:
        show_banner()
        action = click.prompt('Welke actie wil je uitvoeren?',
                              type=click.Choice(["disable_defender", "ps", "check_defender_status", "start_discord_bot", "take_screenshot"]))
    match action:
        case "disable_defender":
            if check_os():
                click.echo(disable_defender())
            else:
                click.echo(f"Deze functie werkt alleen in een Windows omgeving. Jouw OS: {sys.platform}")
        case "ps":
            click.echo(show_running_processes())
        case "check_defender_status":
            if check_os():
                click.echo(check_defender_status())
            else:
                click.echo(f"Deze functie werkt alleen in een Windows omgeving. Jouw OS: {sys.platform}")
        case "start_discord_bot":
            start_bot()
        case "take_screenshot":
            take_screenshot()  # Call the PowerShell screenshot function

if __name__ == '__main__':
    main()

