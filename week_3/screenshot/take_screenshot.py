import subprocess

def take_screenshot():
    """Runs a PowerShell script to take a screenshot and save it."""
    try:
        result = subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", "screenshot.ps1"],
                                capture_output=True, text=True)
        print(result.stdout)  # Output the saved screenshot path
    except Exception as e:
        print(f"Error taking screenshot: {e}")

