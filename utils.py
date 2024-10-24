import requests
import ubinascii
from data import server

BASE_URL = server["url"]

def fileToBase64(filePath: str) -> str:
    try:
        base64_str = ""
        with open(filePath, "rb") as file:
            while True:
                chunk = file.read(1024//100)# Read 0.01KB chunks at a time
                if not chunk:
                    break
                base64_str += ubinascii.b2a_base64(chunk).decode("utf-8").strip()
        return base64_str
    except Exception as e:
        print(f"Error reading file {filePath}: {e}")
        return ""

def clearFiles() -> None:
  try:
    response = requests.post(f"{BASE_URL}/clearfiles")
    print(f"Clear Files - Status Code: {response.status_code}, Response: {response.text}")
  except requests.RequestException as e:
    print(f"Error clearing files: {e}")

def uploadTemperature(temp: str) -> None:
  try:
    response = requests.post(f"{BASE_URL}/uploadtemperature/{temp}")
    print(f"Upload Temperature - Status Code: {response.status_code}, Response: {response.text}")
  except requests.RequestException as e:
    print(f"Error uploading temperature: {e}")

def uploadSound(base64String: str) -> None:
  payload = {"base64": base64String}
  headers = {'Content-Type': 'application/json'}
  try:
    response = requests.post(f"{BASE_URL}/uploadsound", json=payload, headers=headers)
    print(f"Upload Sound - Status Code: {response.status_code}, Response: {response.text}")
  except requests.RequestException as e:
    print(f"Error uploading sound: {e}")

def downloadTemperature() -> str:
  try:
    response = requests.get(f"{BASE_URL}/downloadtemperature")
    print(f"Download Temperature - Status Code: {response.status_code}, Response: {response.text}")
    return response.text
  except requests.RequestException as e:
    print(f"Error downloading temperature: {e}")
    return ""

def downloadSound() -> str:
  try:
    response = requests.get(f"{BASE_URL}/downloadsound")
    print(f"Download Sound - Status Code: {response.status_code}, Response: {response.text[:10]}...")
    return response.text
  except requests.RequestException as e:
    print(f"Error downloading sound: {e}")
    return ""
