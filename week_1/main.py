import sys
import subprocess
import click
import pyfiglet
import random
from banners import banner_list
import ctypes


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


def is_admin():
    if ctypes.windll.shell32.IsUserAnAdmin():
        return True
    else:
        return False


def disable_defender_test():
    # poweshell CMDlets voor het uitschakelen van Windows Defender
    disable_defender_cmd = [
        "powershell",
        "-ExecutionPolicy", "Bypass",
        "-NoProfile",
        "-Command",
        "Set-MpPreference -DisableRealtimeMonitoring $true"
    ]

    try:
        subprocess.run(disable_defender_cmd, shell=True, check=True,
                       capture_output=True, text=True)
        print("real-time bescherming is uitgeschakeld")
    except subprocess.CalledProcessError as e:
        print(f"Fout bij het uitschakelen van Defender: {e.stderr}")


def check_defender_status():
    check_defender_status_cmd = [
        "powershell",
        "-ExecutionPolicy", "Bypass",
        "-NoProfile",
        "-Command",
        "Get-MpPreference | Select-Object -ExpandProperty DisableRealtimeMonitoring"
    ]
    try:
        result = subprocess.run(check_defender_status_cmd,
                                shell=True, capture_output=True, text=True)
        status = result.stdout.strip()
        if status == "True":
            return "Defender real-time protection is UITGESCHAKELD"
        else:

            return "Defender real-time protection is  nog INGESCHAKELD, probeer tamper protection uit te zetten."
    except subprocess.CalledProcessError as error:
        print(f"fout bij het uitschakelen van defender: {error}")


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
                click.echo(disable_defender_test())
            else:
                click.echo(f"Dit programma werkt alleen in een Windows omgeving. Jouw OS: {
                           sys.platform}")
        case "ps":
            click.echo(show_running_processes())


if __name__ == '__main__':
    main()

# TODO: wachtwoord vragen en Powershell als administrator runnen
