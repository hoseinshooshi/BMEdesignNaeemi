from pathlib import Path
from urllib.request import urlopen, Request

DATA_DIR = Path(__file__).resolve().parents[1] / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

FILES = {
    "ANSUR II MALE Public.csv": "https://raw.githubusercontent.com/senihberkay/US-Army-ANSUR-II/master/ANSUR%20II%20MALE%20Public.csv",
    "ANSUR II FEMALE Public.csv": "https://raw.githubusercontent.com/senihberkay/US-Army-ANSUR-II/master/ANSUR%20II%20FEMALE%20Public.csv",
}

for filename, url in FILES.items():
    destination = DATA_DIR / filename
    print(f"Downloading {filename} ...")
    request = Request(url, headers={"User-Agent": "BMEdesignNaeemi/1.0"})
    with urlopen(request, timeout=60) as response, destination.open("wb") as f:
        f.write(response.read())
    print(f"Saved: {destination}")

print("ANSUR II files downloaded successfully.")
