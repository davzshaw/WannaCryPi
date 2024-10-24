from connection import Connection
from device import printInfo
from utils import clearFiles, uploadSound, uploadTemperature, downloadSound, downloadTemperature, fileToBase64
if __name__ == "__main__":
  # Print device information
  printInfo()
  
  # Connect device to the network
  #conn = Connection()
  #conn.scan()
  #conn.injectData()
  #conn.connect()
  
  base64 = fileToBase64("sound96trimmed.mp3")
  
  # Comunicate with the server
  uploadSound(base64)
  
  del base64
  
