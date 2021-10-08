import requests

wave_file = "1-103995-A-30.wav"
response = requests.get(
    f"https://github.com/karolpiczak/ESC-50/raw/master/audio/{wave_file}"
)

with open(wave_file, "wb") as f:
    f.write(response.content)
