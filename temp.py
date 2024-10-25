import spidev
import time

def readTemperature(channel=0):
  spi = spidev.SpiDev()
  spi.open(0, 0)
  spi.max_speed_hz = 1350000
  
  adcResponse = spi.xfer2([1, (8 + channel) << 4, 0])
  adcValue = ((adcResponse[1] & 1) << 8) + adcResponse[2]
  
  print(f"Raw ADC Value: {adcValue}")  # Añadido para depuración
  
  voltage = adcValue * 3.3 / 255
  temperatureC = voltage * 100
  
  spi.close()
  return temperatureC

if __name__ == "__main__":
  while True:
    tempC = readTemperature(channel=0)
    print(f"Temperature: {tempC:.2f} °C")
    time.sleep(1)
