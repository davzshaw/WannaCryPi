from utils import clearFiles, uploadSound, uploadTemperature, downloadSound, downloadTemperature, fileToBase64
if __name__ == "__main__":
  base64 = fileToBase64("sound.mp3")
  print(base64)
  del base64
  
