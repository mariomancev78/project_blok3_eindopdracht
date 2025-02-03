from sys import platform




# Functie voor het controlleren of het script op Windows wordt uitgevoerd.
def check_os():
    if platform == "win32":
        return True
    else:
        return False

def main():
    if check_os():
        pass
    else:
        print(f"Dit programma werkt alleen in een Windows omgeving. jouw platform: {platform}")
if __name__ == '__main__':
    main()
