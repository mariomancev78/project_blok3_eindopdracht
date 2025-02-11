import sys
import subprocess
import click
import pyfiglet
import random
from week_1.banners import banner_list
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


def disable_defender():
    # poweshell CMDlets voor het uitschakelen van Windows Defender
    disable_defender_cmd = [
        "powershell",
        "-ExecutionPolicy", "Bypass",
        "-NoProfile",
        "-Command",
        "Set-MpPreference -DisableRealtimeMonitoring $true"
    ]
    if is_admin():
        try:
            subprocess.run(disable_defender_cmd, shell=True, check=True,
                           capture_output=True, text=True)
            return "real-time bescherming is uitgeschakeld"

        except subprocess.CalledProcessError as e:
            return f"Fout bij het uitschakelen van Defender: {e.stderr}"
    else:
        return "voer dit script in een admin venster uit."


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

            return "Defender real-time protection is nog INGESCHAKELD"
    except subprocess.CalledProcessError as error:
        return f"fout bij het uitschakelen van defender: {error}"


def show_running_processes():
    show_ps_command = "gps"
    try:
        return "de draaiende processen:"
        subprocess.call(f"powershell.exe {show_ps_command}", shell=True)
    except Exception as e:
        return f"er ging iets mis: {e}"
