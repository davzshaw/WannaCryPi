import requests
import base64
from data import server

baseUrl = server["url"]

def fileToBase64(filePath: str) -> str:
  try:
    with open(filePath, "rb") as file:
      base64String = base64.b64encode(file.read()).decode("utf-8")
    return base64String
  except Exception as e:
    print(f"Error reading file {filePath}: {e}")
    return ""

def clearFiles() -> None:
  try:
    response = requests.post(f"{baseUrl}/clearfiles")
    print(f"Clear Files - Status Code: {response.status_code}, Response: {response.text}")
  except requests.RequestException as e:
    print(f"Error clearing files: {e}")

def uploadTemperature(temp: str) -> None:
  try:
    response = requests.post(f"{baseUrl}/uploadtemperature/{temp}")
    print(f"Upload Temperature - Status Code: {response.status_code}, Response: {response.text}")
  except requests.RequestException as e:
    print(f"Error uploading temperature: {e}")

def uploadSound(base64String: str) -> None:
  payload = {"base64": base64String}
  headers = {'Content-Type': 'application/json'}
  try:
    response = requests.post(f"{baseUrl}/uploadsound", json=payload, headers=headers)
    print(f"Upload Sound - Status Code: {response.status_code}, Response: {response.text}")
  except requests.RequestException as e:
    print(f"Error uploading sound: {e}")

def downloadTemperature() -> str:
  try:
    response = requests.get(f"{baseUrl}/downloadtemperature")
    print(f"Download Temperature - Status Code: {response.status_code}, Response: {response.text}")
    return response.text
  except requests.RequestException as e:
    print(f"Error downloading temperature: {e}")
    return ""

def downloadSound() -> str:
  try:
    response = requests.get(f"{baseUrl}/downloadsound")
    print(f"Download Sound - Status Code: {response.status_code}, Response: {response.text[:10]}...")
    return response.text
  except requests.RequestException as e:
    print(f"Error downloading sound: {e}")
    return ""


