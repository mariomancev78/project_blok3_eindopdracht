
import wave
import pyaudio


def record_mic() -> "str":
    """ Neemt audio op van de microfoon en returnt het pad waar het is opgeslagen."""
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 1024
    RECORD_SECONDS = 10
    WAVE_OUTPUT_FILENAME = "output.wav"

    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

    print("Aan het opnemen...")
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Opnemen voltooid.")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    print(f"Audio opgeslagen als: {WAVE_OUTPUT_FILENAME}")
    return WAVE_OUTPUT_FILENAME


def list_audio_devices() -> dict["str", "str"]:
    """ De functie geeft eerst het ID van het audio apparaat, daarna de naam"""
    available_devices = {}
    try:
        audio = pyaudio.PyAudio()
        info = audio.get_host_api_info_by_index(0)
        num_devices = info.get('deviceCount')
        for i in range(num_devices):
            device_info = audio.get_device_info_by_host_api_device_index(0, i)
            if device_info.get('maxInputChannels') > 0:
                available_devices[i] = device_info.get('name')
        audio.terminate()
        return available_devices

    except Exception as e:
        return f"er ging iets mis tijdens het ophalen van audio apparaten: {e}"
