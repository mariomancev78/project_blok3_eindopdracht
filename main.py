import sys
import click
from week_1.disable_defender import disable_defender, check_os, check_defender_status, show_banner, show_running_processes


@click.command()
@click.option("--action", help="De actie die uitgevoerd moet worden.", type=click.Choice(["disable_defender", "ps", "check_defender_status"]))
# disable_defender voor het uitzetten van defender. ps voor het tonen van draaiende processen.
# Main functie
def main(action):
    if not action:
        show_banner()
        action = click.prompt('Welke actie wil je uitvoeren?',
                              type=click.Choice(["disable_defender", "ps", "check_defender_status"]))
    match action:
        case "disable_defender":
            # Is dit een windows omgeving?
            if check_os():
                click.echo(disable_defender())
            else:
                click.echo(f"Deze functie werkt alleen in een Windows omgeving. Jouw OS: {
                           sys.platform}")
        case "ps":
            click.echo(show_running_processes())
        case "check_defender_status":
            if check_os:
                click.echo(check_defender_status())
            else:
                click.echo(f"Deze functie werkt alleen in een Windows omgeving. Jouw OS: {
                           sys.platform}")


if __name__ == '__main__':
    main()

# TODO: wachtwoord vragen en Powershell als administrator runnen
