import os
import subprocess


def take_screenshot():
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))

        screenshot_script = os.path.join(script_dir, "screenshot.ps1")

        result = subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", screenshot_script],
                                capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        print(f"Fout tijdens het maken van screenshot: {e}")
